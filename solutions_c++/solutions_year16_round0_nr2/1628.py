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

int n,i,ans;
string s;
int main()
{
	freopen("B-larg.in", "r", stdin);
  	freopen("B-larg.out", "w", stdout);
	ios_base::sync_with_stdio(false);
	cin.tie(0);
  	int t,l=1;
	cin>>t;
	while(t--)
	{
	    cin>>s;
	    cout<<"Case #"<<l++<<": ";
	    n=s.length();
	    i=n-1;
	    while(i>=0 && s[i]=='+')
            i--;
        ans=0;
        for(;i>=0;i--)
        {
            ans++;
            while(i>=1 && s[i]==s[i-1])
                i--;
        }
        cout<<ans<<"\n";
	}
	return 0;
}
