#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
const int N = 3005;
struct Point {
    LL x , y;
    Point () {}
    Point (int _x , int _y) {
        x = _x , y = _y;
    }
    Point operator + (const Point& R) const {
        return Point(x + R.x , y + R.y);
    }
    Point operator - (const Point& R) const {
        return Point(x - R.x , y - R.y);
    }
    LL operator ^ (const Point& R) const {
        return (LL)x * R.y - (LL)y * R.x;
    }
    LL operator % (const Point& R) const {
        return (LL)x * R.x + (LL)y * R.y;
    }
    bool operator == (const Point& R) const {
        return R.x == x && R.y == y;
    }
    int quad() const {
        if (y != 0) {
            return y > 0;
        }
        return x > 0;
    }
    LL len() const {
        return (LL)x * x + (LL)y * y;
    }
};

bool operator < (const Point& A , const Point& B) {
    int x = A.quad() , y = B.quad();
    if (x != y)
        return x < y;
    LL Cross = A ^ B;
    if (Cross != 0)
        return Cross > 0;
    return A.len() < B.len();
}

int n , ca;
Point p[N];
int res[N];

bool check(const pair<Point , int>& A , const pair<Point , int>& B) {
    LL C = A.first ^ B.first;
    return C >= 0;
}

void work() {
    int i , j , k , x , y , z;
    scanf("%d",&n);
    for (i = 0 ; i < n ; ++ i) {
        scanf("%d%d" , &x , &y);
        p[i] = Point(x , y);
        res[i] = n - 1;
    }
    for (i = 0 ; i < n ; ++ i) {
        vector< pair<Point , int> > V;
        for (j = 0 ; j < n ; ++ j)
            if (i != j)
                V.push_back(make_pair(p[j] - p[i] , j));
        sort(V.begin() , V.end());
        int m = V.size();
        for (j = 0 , k = 1 ; j < m ; ++ j) {
            while (k < m && check(V[j] , V[(j + k) % m]))
                ++ k;
            res[i] = min(res[i] , m - k);
            //res[V[j].second] = min(res[V[j].second] , m - k);
            if (k > 1)
                -- k;
        }        
    }
    printf("Case #%d:\n" , ++ ca);
    for (i = 0 ; i < n ; ++ i)
        printf("%d\n" , res[i]);
}

int main() {
    freopen("1.in" , "r" , stdin);
    freopen("1" , "w" , stdout);
    int T;
    scanf("%d" , &T);
    while (T --)
        work();
    return 0;
}
