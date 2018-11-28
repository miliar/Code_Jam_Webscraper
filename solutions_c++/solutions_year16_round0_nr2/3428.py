#include<bits/stdc++.h>
#define ll long long int
#define sd(n) scanf("%d",&n)
#define sl(n) scanf("%lld",&n)
#define slf(n) scanf("%lf",&n)
#define ss(n) scanf("%s",n)
int Set(int n,int pos) {return n | (1<<pos);}
int Reset(int n,int pos){return n & ~(1<<pos);}
int Check(int n,int pos){return n & (1<<pos);}
using namespace std;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,T=0,len,z,i,j,k,ans;
    char a[102];
    sd(t);
    while(t--)
    {
        ans=0;
        ss(a);
        int len=strlen(a);
        int z=len;
        while(z--)
        {
            for(j=1;j<len;j++)
            {
                if(a[j]!=a[0])
                {
                    for(k=0;k<j;k++)
                    {
                        a[k]=a[j];
                    }
                    break;
                }
            }
            if(j==len)
            {
                if(a[0]=='-')
                    ans++;
                break;
            }
            ans++;
        }
        printf("Case #%d: %d\n",++T,ans);
    }
    return 0;
}
