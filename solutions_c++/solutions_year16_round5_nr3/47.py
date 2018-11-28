#include <bits/stdc++.h>
using namespace std;
const int N = 1005;

int ca;

int n , S;
int X[N] , Y[N] , Z[N];
int f[N];
int getf(int x) {
    return f[x] == x ? x : f[x] = getf(f[x]);
}
void work() {
    scanf("%d%d" , &n , &S);
    for (int i = 0 ; i < n ; ++ i) {
        scanf("%d%d%d" , &X[i] , &Y[i] , &Z[i]);
        int x , y , z;
        scanf("%d%d%d" , &x , &y , &z);
        f[i] = i;
    }
    vector< pair< int , pair<int , int> > > E;
    for (int i = 0 ; i < n ; ++ i) {
        for (int j = i + 1 ; j < n ; ++ j) {
            int dx = X[i] - X[j];
            int dy = Y[i] - Y[j];
            int dz = Z[i] - Z[j];
            E.push_back(make_pair(dx * dx + dy * dy + dz * dz , make_pair(i , j)));
            //printf("%d %d : %d\n" , i , j ,  E.back().first);
        }
    }
    sort(E.begin() , E.end());
    for (int i = 0 ; i < E.size() ; ++ i) {
        int x = E[i].second.first;
        int y = E[i].second.second;
        if (getf(x) != getf(y)) {
            f[getf(x)] = getf(y);
        }
        if (getf(0) == getf(1)) {
            printf("%.10f\n" , sqrt(E[i].first));
            return;
        }
    }

}

int main() {
    int T;
    scanf("%d" , &T);
    while (T --) {
        printf("Case #%d: " , ++ ca);
        work();
    }
    return 0;
}
