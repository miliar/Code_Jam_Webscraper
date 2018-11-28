#include <bits/stdc++.h>
using namespace std;
#define ll long long
int t;
ll n;
int vis[10];
int main()
{
    FILE *ip,*out;
    ip=fopen("A-large.in","r");
    out=fopen("output_file.txt","w");
    fscanf(ip,"%d",&t);
    for(int i=1;i<=t;i++)
    {
        fscanf(ip,"%lld",&n);
        if(n==0)
            fprintf(out,"Case #%d: INSOMNIA\n",i);
        else
        {
            memset(vis,0,sizeof(vis));
            ll digit,ones,mul=1,cnt=0;
            while(1)
            {
                digit=mul*n;
                while(digit)
                {
                    ones=digit%10;
                    if(vis[ones]==0)
                    {
                        vis[ones]=1;
                        cnt++;
                    }
                    digit/=10;
                }
                digit=mul*n;
                mul++;
                if(cnt==10)
                    break;
            }
            fprintf(out,"Case #%d: %lld\n",i,digit);
        }
    }
    return 0;
}
