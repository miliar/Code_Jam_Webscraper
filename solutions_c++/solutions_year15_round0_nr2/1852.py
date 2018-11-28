#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<queue>

#define INF 1000000000
#define endl '\n'
#define ll long long


using namespace std;


int main()
{
//	ios::sync_with_stdio(false);
//	cin.tie(0);

	int a[2048];
	
	int t;
	cin >> t;
	for(int time = 1 ; time <= t ; time++)
	{
		int most = -1;
		
		int n;
		cin >> n;
		for(int i = 0 ; i < n ; i++)
		{
			cin >> a[i];
			most = max(most,a[i]);
		}
					
		/*
		for(int i = 1 ; i <= n ; i++)
			prefix[i] = a[i];
		prefix[0] = 0;
		for(int i = 1 ; i <= n ; i++)
			prefix[i] += prefix[i-1];
			*/
		
		int ans = most;
		for(int i = 1 ; i < most ; i++)
		{
			int move = 0;
			
			for(int j = 0 ; j < n ; j++)
			{
				if(a[j] > i)
					move += (a[j]-1)/i;
			}
			
			ans = min(ans, i+move );
		} 
		
		cout << "Case #" << time << ": " << ans << endl;
	}
	
	return 0;
}

