#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;
const int MAX = 1000 + 10;

double dis[MAX][MAX];
double x[MAX], y[MAX], z[MAX];

struct pr{
    int x, y;
    double dis;
}rec[MAX*MAX];

bool cmp(pr a, pr b){return a.dis<b.dis;}

int p[MAX];
int find(int x){return x == p[x] ? x : p[x] = find(p[x]);}

int main(){
    int TN;
    scanf("%d", &TN);
    for(int casen = 1 ; casen <= TN ; casen++){
        printf("Case #%d: ", casen);
        int n, s;
        scanf("%d %d", &n, &s);
        for(int i = 0 ; i < n ; i++){
            scanf("%lf %lf %lf %*d %*d %*d", &x[i], &y[i], &z[i]);
        }
        int cnt = 0;
        for(int i = 0 ; i < n ; i++){
            for(int j = i+1 ; j < n ; j++){
                rec[cnt].x = i;
                rec[cnt].y = j;
                rec[cnt++].dis = sqrt( pow(fabs(x[i]-x[j]), 2) + 
                                  pow(fabs(y[i]-y[j]), 2) +
                                  pow(fabs(z[i]-z[j]), 2));
            }
        }
        sort(rec, rec+cnt, cmp);
        for(int i = 0 ; i < n ; i++) p[i] = i;
        double ans = 0;
        for(int i = 0 ; i < cnt ; i++){
            p[find(rec[i].x)] = find(rec[i].y);
            ans = rec[i].dis;
            if(find(p[0]) == find(p[1]))break;
        }
        printf("%.9f\n", ans);
    }
    return 0;
}
