// Author: thecodekaiser
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
#define MXN 1005

char str[MXN];

void solve(int CS)
{
	int mx;
	cin >> mx;
	scanf("%s", str);
		
	int total = 0, req, curr;
	int ans = 0;
	
	for(int i = 0; i < mx+1; i++)
	{
		req = i;
		curr = str[i] - '0';
		
		if(curr)
		{
			if(total >= req) 
			{
				total += curr;
			}
			else
			{
			//	cout << "i: " << i << " req-total: " << req-total << endl;
				ans += (req - total);
				total += (req - total + curr);
			
			}
		}
	}
	
	printf("Case #%d: %d\n", CS, ans);
	return;
}

int main()
{
	int t, CS = 1;
	cin >> t;
	
	while(t--)
		solve(CS++);
		
	return 0;
}
