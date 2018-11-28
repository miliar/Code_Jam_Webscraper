/*
jai shree ram _/\_
A hacker from NITP
*/

#include<bits/stdc++.h>
using namespace std;

#define mod 1000000007
typedef set<string> ss;
typedef vector<int> vs;
typedef map<int,char> msi;
typedef pair<int,int> pa;
typedef long long int ll;

bool vis[10];
ll n,k,p,i;
int main()
{
	freopen("A-larg.in", "r", stdin);
  	freopen("A-larg.out", "w", stdout);
	ios_base::sync_with_stdio(false);
	cin.tie(0);
  	int t,l=1;
	cin>>t;
	while(t--)
	{
	    cin>>n;
	    cout<<"Case #"<<l++<<": ";
	    if(n==0)
        {
            cout<<"INSOMNIA\n";
            continue;
        }
        memset(vis,0,sizeof(vis));
        p=n;
        while(1)
        {
            k=n;
            while(k>0)
            {
                vis[k%10]=1;
                k/=10;
            }
            for(i=0;i<10;i++)
                if(!vis[i])
                    break;
            if(i==10)
            {
                cout<<n<<"\n";
                break;
            }
            n+=p;
        }
	}
	return 0;
}
