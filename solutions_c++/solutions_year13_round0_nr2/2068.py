#include<stdio.h>
#include<iostream>
#include<vector>
#include<math.h>
#include<algorithm>

#define pb push_back
#define mp make_pair
#define fr first
#define se second
#define sc scanf
#define pr printf

const double eps = 1e-12;
const double PI = 3.1415926535898;
const int alphabet = 256;
const int MN = 110;
const long long inf = (1LL<<60);

using namespace std;
struct pt{
    double x, y;
};
inline double sqr(double X){
    return (X*X);
}
inline double dist(pt a, pt b){
    return sqrt( sqr(a.x-b.x) + sqr(a.y-b.y) + eps);
}
inline double vector_m(pt a, pt b, pt c){
    return (b.x-a.x)*(c.y-a.y) - (c.x-a.x)*(b.y-a.y);
}
inline double scalar_m(pt a, pt b, pt c){
    return (b.x-a.x)*(c.x-a.x) + (b.y-a.y)*(c.y-a.y);
}
pt IntersectionOfLines(double A1, double B1, double C1, double A2, double B2, double C2){
    double D = A2*B1 - A1*B2;
    pt ans;
    if(fabs(D)<eps){
        ans.x = -inf;
        ans.y = -inf;
    }
    else{
        ans.x = (C1*B2 - C2*B1)/D;
        ans.y = (A1*C2 - A2*C1)/D;
    }
    return ans;
}
inline bool intersect(double a, double b, double c, double d){
    if(a>b)swap(a, b);
    if(c>d)swap(c, d);
    return (max(a, c)-min(b, d))<eps;
}
inline bool cmp (pt a, pt b) {
	return a.x < b.x || a.x == b.x && a.y < b.y;
}

int t, n, m, b[MN][MN], row[MN], col[MN];

string solve(){
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            if(b[i][j] != min(row[i], col[j])){
                return "NO";
            }
        }
    }
    return "YES";
}

void Init(){
    sc("%d", &t);
    for(int k=1; k<=t; k++){
        pr("Case #%d: ", k);
        sc("%d%d", &n, &m);
        for(int i=0; i<n; i++){
            row[i] = 0;
        }
        for(int j=0; j<m; j++){
            col[j] = 0;
        }
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                sc("%d", &b[i][j]);
                row[i] = max(row[i], b[i][j]);
                col[j] = max(col[j], b[i][j]);
            }
        }
        cout<<solve()<<endl;
    }
}

main(){
	freopen("input.txt", "r", stdin);	freopen("output.txt", "w", stdout);
	//freopen("paint.in", "r", stdin);	freopen("paint.out", "w", stdout);
    Init();
	return 0;
}
