#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<climits>
#include<cctype>
#include<iostream>
#include<algorithm>
#include<queue>
#include<vector>
#include<map>
#include<string>
#include<set>
#include<stack>
#define ll long long
#define MAX 1000
#define INF INT_MAX
#define eps 1e-6
#define REP(i,n) for (int i=0; i<n; i++)
#define FOR(i,s,t) for (int i=(s); i<=(t); i++)

using namespace std;


int main(){
    int T;
    double c,f,x;
    FILE *fp = fopen("out.txt", "w");
    scanf("%d",&T);
    for (int cas = 1; cas<=T; cas++){
        scanf("%lf%lf%lf",&c,&f,&x);
        double ans = 0.0,cnt = 0.0,rate;
        if (x < c){
            ans = x / 2;
        }
        else{
            cnt = c;
            ans = c / 2;
            rate = 2;
            while (fabs(cnt - x) > 1e-6){
                if ((x - cnt)/rate > (x - (cnt-c)) / (rate+f)){
                    rate += f;
                    ans += c / rate;
                    cnt = c;
                }
                else{
                    ans += (x-cnt) / rate;
                    cnt = x;
                }
            }
        }
       // printf("%.7lf\n",ans);
        fprintf(fp,"Case #%d: %.7lf\n",cas,ans);
    }
    return 0;
}
