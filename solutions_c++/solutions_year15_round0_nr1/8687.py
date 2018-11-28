#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<string>
#include<queue>
#include<map>
#include<iostream>
#include<vector>
#define MAX 100
#define MOD 1000003
#define pb push_back
#define mp make_pair
#define scll(t) scanf("%lld",&t)
#define scl(t) scanf("%ld",&t)
#define sc(t) scanf("%d",&t)
#define max(a,b) a>b?a:b
#define min(a,b) a<b?a:b
#define ll long long
#define fre freopen("in.txt","r",stdin),freopen("out.txt","w",stdout)
using namespace std;
int main()
{
fre;
    int t,n,i,j;
    sc(t);
    int req,ma,su=0;
    string s;
    for(int k=1;k<=t;k++)
    {
        sc(n);
        su=0;
        ma=0;
        cin>>s;
        for(i=0;i<=n;i++)
        {
            if(i<=su)
            {
                su+=s[i]-'0';
            }
            else
            {
                req=i-su;
                su=su+req+s[i]-'0';
                ma+=req;
            }
        }
        printf("Case #%d: %d\n",k,ma);
    }
    return 0;
}
