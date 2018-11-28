#include<cstring>
#include<fstream>
#include<iostream>
#include<iomanip>
#include<cstdio>
#include<cctype>
#include<algorithm>
#include<queue>
#include<vector>
#include<stack>
#include<ctime>
#include<cstdlib>
using namespace std;
#define PI acos(-1.0)
#define MAXN 100005
#define eps 1e-5
#define INF 0x7FFFFFFF

double ans[500000];
int main()
{
    freopen ("B-large.in", "r", stdin);
    freopen ("B-large.out", "w", stdout);
    int t,i,kk=1;
    double c,f,x;
    scanf("%d",&t);
    while(t--){
        double step = 2.0;
        scanf("%lf%lf%lf",&c,&f,&x);
        if(c>=x)    printf("Case #%d: %.7lf\n",kk++,x/2.0);
        else{
            double pos = x/2.0;
            int p = 0;
            double sum = 0;
            ans[p++] = pos;
            while(1){
                sum += c/step;
                step += f;
                ans[p++] = sum + x/step;
                if(ans[p-1]>pos)    break;
                if(p>100000)    break;
            }
            double minm = INF;
            for(i=0;i<p;i++)
                if(minm>ans[i]) minm = ans[i];
            printf("Case #%d: %.7lf\n",kk++,minm);
        }
    }
    return 0;
}
