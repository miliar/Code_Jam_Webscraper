#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pi;

#define MP make_pair
#define PB push_back
#define F first
#define S second
#define MOD 1000000007
#define INF (1 << 30)

int main()
{
    ios :: sync_with_stdio(false);
    cin.tie(0);
    freopen("large1.in", "r", stdin);
	freopen("large1out.txt", "w", stdout);
	ll t, n, i, j, cur, ans, temp;
	int cases = 0;
	cin >> t;
	while(t--)
	{
		cases++;
		cin >> n;
		if(!n)
			cout << "Case #" << cases << ": " << "INSOMNIA" << endl;
		else
		{
			bool a[10];
			bool flag = false;
			memset(a, false, sizeof a);
			for(i = 1; ; i++)
			{
				cur = i * n;
				ans = cur;
				while(cur > 0)
				{
					temp = cur%10;
					cur /= 10;
					a[temp] = true;
				}
				for(j = 0; j < 10; j++)
				{
					if(!a[j])
						break;
				}
				if(j == 10)
					flag = true;
				if(flag)
					break;
			}
			cout << "Case #" << cases << ": " << ans << endl;
		}
	}
    return 0;
}

