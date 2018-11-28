#include <bits/stdc++.h>
using namespace std;
//defines-general
typedef long long ll;
typedef long double ld;
#define to(a) __typeof(a)
#define fill(a,val) memset(a,val,sizeof(a))
#define repi(i,a,b) for(__typeof((b)) i = a;i<(b);i++)
//defines-pair
typedef pair<int, int> pii;
typedef pair<long long, long long> pll;
#define ff first
#define ss second
#define mp make_pair
//defines-vector
typedef vector<int> vi;
typedef vector<long long> vll;
#define all(vec) vec.begin(),vec.end()
#define tr(vec,it) for(__typeof(vec.begin()) it = vec.begin();it!=vec.end();++it)
#define pb push_back
#define sz size()
#define contains(vec,x) (find(vec.begin(),vec.end(),x)!=vec.end())

#define MOD 1000000007

int main()
{
	std::ios::sync_with_stdio(false);
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t;
	cin >> t;
	for(int loop = 1; loop <= t; loop++)
	{
		int smax;
		cin >> smax;
		string s;
		cin >> s;
		int count = 0;
		int ans = 0;
		for(int i = 0 ; i < s.length(); i++ )
		{
			if(i>0)
			{
				int req = s[i]-'0';
				if(count>=i)
				{
					count+=req;
				}
				else
				{
					if(s[i]>'0')
					{
						ans+=i-count;
						count += i-count;
						count+=req;
					}
				}
			}
			else
			{
				count = s[0]-'0';
			}
			//cout << count << " "<<ans<<endl;
		}
		cout << "Case #"<<loop<<": "<<ans<<endl;
	}
    return 0;
}