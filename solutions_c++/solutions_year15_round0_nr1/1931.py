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
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	string a;
	
	int t;
	cin >> t;
	for(int time = 1 ; time <= t ; time++)
	{
		int n;
		cin >> n;
		
		cin >> a;
		
		int sum = 0;
		int ans = 0;
		for(int i = 0 ; i <= n ; i++)
		{
			if(a[i] > '0' && sum < i)
			{
				ans += i-sum;
				sum = i;
			}
			
			sum += a[i]-'0';
			
//			cout << "ans = " << ans << endl;
		}
		
		
		cout << "Case #" << time << ": " << ans << endl;
	}

	return 0;
}

