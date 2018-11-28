#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define FOR(i, n) for(int i = 0; i<n; i++)
#define MP make_pair
#define PB push_back
int main()
{
	int t;
	scanf("%d", &t);
	FOR(case1, t)
	{
		int n;
		scanf("%d", &n);
		n--;
		int arr[17];
		memset(arr, 0, sizeof arr);
		FOR(i, 4)
		{
			FOR(j, 4)
			{
				int x;
				cin >> x;
				if(n == i)
				{
					arr[x]++;
				}
			}
		}
		cin >> n;
		n--;
		FOR(i, 4)
		{
			FOR(j, 4)
			{
				int x;
				cin >> x;
				if(n == i)
				{
					arr[x]++;
				}
			}
		}
		int ans = 0;
		FOR(i, 17)
		{
			if(ans != 0 && arr[i] == 2)
				ans = -1;
			else if(arr[i] == 2)
				ans = i;
		}
		if(ans == 0)
			cout << "Case #"<< case1 + 1 << ": Volunteer cheated!" << endl;
		else if(ans == -1)
			cout << "Case #"<< case1 + 1 << ": Bad magician!" << endl;
		else
			cout << "Case #"<< case1 + 1 << ": " << ans << endl;
	}
}
