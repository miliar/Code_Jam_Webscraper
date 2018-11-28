#include <bits/stdc++.h>

#define F(i,a,b) for(int i = a; i < b; i++)
#define pb push_back
#define mp make_pair
#define all(a) a.begin(), a.end()


using namespace std;

typedef vector<int> vi;
typedef vector<vi> vii;
typedef pair<int,int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<vs> vvs;
typedef  long long ll;

int main()
{
	std::ios_base::sync_with_stdio(false);
	int T;
	cin >> T;
	
	F(k,0,T)
	{
		int S;
		string inp;
		cin >> S >> inp;
		long long total = 0,ans = 0;
		F(i,0,inp.length())
		{
			if(i == 0)
				total += (inp[i] - '0');
			else
			{
				if(total >= i)
					total += (inp[i] - '0');
				else
				{
					int temp = (i - total);
					ans += (i - total);
					total += (inp[i] - '0') + temp;
				}
			}
		}
		cout << "Case #" << k+1 << ": " << ans << endl;
	}
	
	return 0;
}
