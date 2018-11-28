
/* 
Take yourself as work in progress.
-Bhai
*/

#include<bits/stdc++.h>
using namespace std;

#define M 1000000007
#define LL long long
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define VI vector<int>
#define SZ(a) int(a.size())
#define TR(c, it) for(typeof((c).begin()) it=(c).begin(); it!=(c).end(); it++ )
#define SET(a, b) memset(a, b, sizeof(a))

int k;
char st[1005];
bool arr[1005];

int main()
{
	ios_base::sync_with_stdio(0);
	int t;
	cin >> t;
	int nahoy = 1;
	while(t--)
	{
		cin >> st >> k;		
		int l = strlen(st);
		for(int i=0; i<l; i++)
			arr[i] = (st[i]=='+');

		int ans=0;
		for(int i=0; i<l-k+1; i++)
			if(!arr[i])
			{
				for(int j=i; j<i+k; j++)
					arr[j] = !arr[j];
				ans++;
				/*
				for(int j=0; j<l; j++)
					cout << arr[j] << endl;
				cout << endl;
				*/
			}

		bool ok = true;
		for(int i=l-k; i<l; i++)
			if(!arr[i])
			{
				ok = false;
				break;
			}

		if(ok)cout << "Case #" << nahoy << ": " << ans << endl;
		else cout << "Case #" << nahoy << ": " << "IMPOSSIBLE" << endl;
 
		nahoy++;
	}
	return 0;
}
