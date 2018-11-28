#pragma warning(disable:4786)
#include<iostream>
#include<algorithm>
#include<cmath>
#include<stdio.h>
#include<time.h>
#include<stdlib.h>
#include<queue>
#include<set>
#include<vector>
#include<string>
#include<ctime>
#include<string.h>
using namespace std;
#define pi acos(-1.0)
//#define LL __int64
typedef long long LL;
#define INF 0x7fffffffffffffff
#define bug puts("hear!")
#define inf 0x7fffffff
#define eps 1e-10
#define FRE freopen("A-small-attamp1.in","r",stdin)
#define E exp(1.0)
#define mod 1000000007
#include<stdio.h>
#include<string.h>
#include<stdbool.h>
int main()
{
    freopen("2.in","r",stdin);
    freopen("2.out","w",stdout);
    int t;
    double ans;
    cin>>t;
    for(int zo=1; zo<=t; zo++)
    {
        ans=0;
        double s1,s2,s3;
        scanf("%lf %lf %lf",&s1,&s2,&s3);
        //printf("%lf %lf %lf\n",s1,s2,s3);
        double nio=0;
        double farm=0.0,ko=2.0;
        while(((double)s3/ko)>((double)(s1/ko)+(double)(s3/(ko+s2))))
        {
            ans+=(double)s1/ko;
            farm++;
            ko+=s2;
            //cout<<(double)s1/ko<<endl;
        }
        ans+=(double)s3/ko;
        printf("Case #%d: %.7lf\n",zo,ans);
    }
    return 0;
}
