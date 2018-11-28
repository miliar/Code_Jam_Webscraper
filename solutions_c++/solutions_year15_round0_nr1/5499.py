#include <bits/stdc++.h>

#define li long int
#define lli long long int
#define loop(i, a, b) for(i=a; i<b; i++)
#define loope(i, a, b) for(i=a; i<=b; i++)
#define loopr(i, a, b) for(i=a; i>b; i--)
#define loopre(i, a, b) for(i=a; i>=b; i--)
#define fill(arr, val) memset(arr, val, sizeof(arr))
#define MOD 1000000007
#define vi vector<int>
#define vpi vector< pair<int, int> >
#define pi pair<int, int>
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define endl '\n'
#define cin fin
#define cout fout

using namespace std;

ifstream fin ("2015qAi.txt");
ofstream fout ("2015qAo.txt");

int main()
{
    //ios_base::sync_with_stdio(false); cin.tie(0);
	int i, j, t, n, ans, sum;
	string s;
	cin>>t;
	loope(j, 1, t)
	{
		cin>>n;
		cin>>s;
		ans=sum=0;
		loop(i, 0, s.length())
		{
			if(s[i]=='0') continue;
			else
			{
				if(ans>=i) ans+=s[i]-'0';
				else
				{
					sum+=(i-ans); ans+=(i-ans)+s[i]-'0';
				}
			}
			//cout<<ans<<" "<<i<<" "<<sum<<endl;
		}
		cout<<"Case #"<<j<<": "<<sum<<endl;
	}
	return 0;
}
