//Copyright of code reserved with Arpit Bajaj
//Date : 07-04-2015
#include<bits/stdc++.h>
#define pii pair<int,int>
#define ll long long
#define pb push_back
#define mp make_pair
#define f first
#define s second
#define MOD 1000000007
using namespace std;
int main()
{
	ios_base::sync_with_stdio(false);
    	cin.tie(NULL);
    freopen("input.in","r",stdin);
    freopen("out.txt","w",stdout);
	int t,k;
	cin>>t;
	for(k=1;k<=t;k++)
	{
		int n,i,ans=0;
		cin>>n;
		n++;
		string s;
		cin>>s;
		int cnt=s[0]-'0';
		for(i=1;i<=n;i++)
        {
            if(i>cnt && s[i]!='0')
            {
                ans+=(i-cnt);
                cnt+=(i-cnt);
            }
            cnt+=(s[i]-'0');
        }
        cout<<"Case #"<<k<<": "<<ans<<endl;
	}
	return 0;
}
