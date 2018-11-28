#include<iostream>
#include<stdio.h>
#include<string>
#include<math.h>
#include<vector>
#include<queue>
#include<string.h>
#include<algorithm>
using namespace std;
#define N 1000000
#define mod 1000000007
#define ll long long
#define ex 2.7182818284590452354
#define pi 3.141592653589793239
#define INFF 999999999
#include<stdio.h>
#include<string.h>
#include<iostream>
using namespace std;
int a[5][5],b[5][5];
double ti[5000],sum[5000];
int main()
{
    int t;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    for(int Case=1;Case<=t;Case++)
    {
        double c,f,x;
        double xx,time=0;
        scanf("%lf %lf %lf",&c,&f,&x);
        printf("Case #%d: ",Case);
        double add=2.0,su=0.0;
        sum[0]=x/add;
        for(int i=1;;i++)
        {
            ti[i]=c/add;
            su+=c/add;
            add+=f;
            xx=x/add;
            sum[i]=su+xx;
            if(sum[i]>sum[i-1])
            {
                printf("%.7lf\n",sum[i-1]);
                break;
            }
        }
    }
    return 0;
}
