#include <algorithm>
#include <string>
#include <stdio.h>
#include <iostream>
#include <vector>
#include <math.h>
using namespace std;
#define rep(i,a,b) for(int i=(a);i<(b);i++)
#define repm(i,a,b) for(int i=(a);i>(b);i--)
#define f(i,n) rep(i,0,n)
#define pin(n) printf("%d\n",n)
#define si(n) scanf("%d",&n)
#define sii(m,n) scanf("%d %d",&m,&n)
#define pb push_back
#define ff first
#define ss second
typedef long long ll;
#define mod 1000000007

int main()  
{
    freopen("A-large.in","r",stdin);
    freopen("output.out","w",stdout);
    string al="ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    int q;
    si(q);
    f(t,q)
    {
        cout<<"Case #"<<t+1<<": ";
        int n;
        si(n);
        int p[n];
        f(i,n) si(p[i]);
        int maxi,maxi2,temp;
        while(true)
        {
            maxi=0;
            maxi2=0;
            temp=0;
            f(i,n)
            {
                if(temp<p[i])
                {
                    temp=p[i];
                    maxi=i;
                }
            }
            if(temp==0) break;
            temp=0;
            f(i,n)
            {
                if(temp<p[i] && i!=maxi)
                {
                    temp=p[i];
                    maxi2=i;
                }
            }
            // cout<<maxi<<" "<<maxi2<<endl;
            if(p[maxi]==p[maxi2] && p[maxi]>1)
            {
                cout<<al[maxi]<<al[maxi2]<<" ";
                p[maxi]--;
                p[maxi2]--;
            }
            else if(p[maxi]==p[maxi2])
            {
                int rem=0;
                f(i,n) if(p[i]>0) rem++;
                if(rem%2==1)
                {
                    cout<<al[maxi]<<" ";
                    p[maxi]--;
                }
                else
                {
                    cout<<al[maxi]<<al[maxi2]<<" ";
                    p[maxi]--;
                    p[maxi2]--;
                }
            }
            else if(p[maxi]>1)
            {
                cout<<al[maxi]<<al[maxi]<<" ";
                p[maxi]-=2;
            }
            else
            {
                cout<<al[maxi]<<" ";
                p[maxi]--;
            }
        }
        cout<<endl;
    }
    return 0;
}


































