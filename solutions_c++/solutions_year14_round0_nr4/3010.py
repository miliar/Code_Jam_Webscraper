#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <limits>
#include<stack>
#include<queue>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <algorithm>
#include <sstream>
using namespace std;
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define sz size()
#define ln length()
#define rep(i,n)  for(int i=0;i<n;i++)
#define fu(i,a,n) for(int i=a;i<=n;i++)
#define fd(i,n,a) for(int i=n;i>=a;i--)
#define all(a)    a.begin(),a.end()
#define si(n) scanf("%d",&n)
#define sl(n) scanf("%lld",&n)
#define gl(n) cin >> n
#define pi(n) printf("%d",n)
#define pl(n) cout << n
#define ps printf(" ")
#define pn printf("\n")
int main()
{
    freopen("D-large.in","rt",stdin);
    freopen("D-large.out","wt",stdout);
    int T;
    si(T);
    for(int t=1;t<=T;t++)
    {
        int Q,dw=0,w=0;
        double na[1007],ke[1007],keu[1007];
        si(Q);
        rep(i,Q)
            cin>>na[i];
        rep(i,Q)
            cin>>ke[i];
        sort(na,na+Q);
        sort(ke,ke+Q);
        memset(keu,0,sizeof keu);
        for(int i=0;i<Q;i++)
        {
            int f=1;
            for(int j=0;j<Q;j++)
            {
                if(na[i] < ke[j] && keu[j]==0)
                {
                    keu[j]=1;
                    f=0;
                    break;
                }
            }
            if(f)
                w++;

        }
        memset(keu,0,sizeof keu);
        int i=0;
        while(i!=Q)
        {
            int f=1;
            for(int j=Q-1;j>=0;j--)
            {
                if(na[i] < ke[j] && keu[j]==0)
                {
                    f=0;keu[j]=1;break;
                }
            }
            if(f)
            {
                dw++;
            }
            i++;
        }
        i=Q-1;
        int dw1=0;
        memset(keu,0,sizeof keu);
        while(i>=0)
        {
            for(int j=Q-1;j>=0;j--)
            {
                if(na[i] > ke[j] && keu[j]==0)
                {
                    keu[j]=1;dw1++;break;
                }
            }
            i--;
        }
        dw=max(dw,dw1);
        cout<<"Case #"<<t<<": "<<dw<<" "<<w<<endl;
    }
    return 0;
}
