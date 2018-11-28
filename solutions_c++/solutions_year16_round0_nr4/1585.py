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

ll k,c,s,i;
int main()
{
	freopen("D-smal.in", "r", stdin);
  	freopen("D-smal.out", "w", stdout);
	ios_base::sync_with_stdio(false);
	cin.tie(0);
  	int t,l=1;
	cin>>t;
	while(t--)
	{
	    cin>>k>>c>>s;
	    cout<<"Case #"<<l++<<": ";
        for(i=1;i<k;i++)
            cout<<i<<" ";
        cout<<i<<"\n";
	}
	return 0;
}
