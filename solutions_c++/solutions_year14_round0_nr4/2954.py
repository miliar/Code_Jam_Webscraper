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
double s[1010],f[1010],k[1010],z[1010];
int main()
{
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
    int t;
    cin>>t;
    for(int zs=1;zs<=t;zs++)
    {
        memset(s,0,sizeof(s));
        memset(f,0,sizeof(f));
        memset(k,0,sizeof(k));
        memset(z,0,sizeof(z));
        int n,win=0,ans=0,j=0,kn=n;
        cin>>n;
        for(int i=0;i<n;i++)
        {
            cin>>s[i];
            f[i]=s[i];
        }
        for(int i=0;i<n;i++)
        {
            cin>>k[i];
            z[i]=k[i];
        }
        sort(s,s+n);
        sort(f,f+n);
        sort(k,k+n);
        sort(z,z+n);
         for (int i=0;i<n;)
        {
            if(s[i]>k[j])
            {
                i++;
                win++;
                j++;
            }
            else if(s[i]<k[j])
            {
                kn--;
                i++;
            }
            else if(s[i]==k[j])
            {
                if (s[n-1]>k[kn-1])
                {
                    n--;
                    kn--;
                    win++;
                }
                else if(s[n-1]<k[kn-1])
                {
                    i++;
                    kn--;
                }
                else if(s[n-1]==k[kn-1])
                {
                    kn--;
                    i++;
                }
            }
        }
        kn=n;j=0;
         for (int i=0;i<n;)
        {
            if(z[i]>f[j])
            {
                i++;
                ans++;
                j++;
            }
            else if(z[i]<f[j])
            {
                kn--;
                i++;
            }
            else if(z[i]==f[j])
            {
                if (z[n-1]>f[kn-1])
                {
                    n--;
                    kn--;
                    ans++;
                }
                else if(z[n-1]<f[kn-1])
                {
                    i++;
                    kn--;
                }
                else if(z[n-1]==f[kn-1])
                {
                    kn--;
                    i++;
                }
            }
        }
        ans=n-ans;
        cout<<"Case #"<<zs<<": "<<win<<" "<<ans<<endl;
    }
    return 0;
}
