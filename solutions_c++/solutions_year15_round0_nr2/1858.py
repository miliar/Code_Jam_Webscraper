#include <iostream> 
#include <fstream> 
#include <cmath> 
#include <algorithm> 
#include <cassert> 
#include <string> 
#include <cstdlib> 
#include <cstdio> 
#include <vector> 
#include <map> 
#include <set> 
#include <stack> 
#include <iomanip> 
#include <queue> 

#define pb push_back 
#define mp make_pair 
#define ll long long 
#define abracadabra next 
#define pii pair<int, int> 

using namespace std; 

int a[1111];

int main(){ 
	ios_base::sync_with_stdio(false); 
	
	int T;
	cin >> T;
	for(int test = 1; test <= T; test++)
	{
		int n;
		cerr << test << endl;
		cin >> n;
		for(int i = 0; i < n; i++)
			cin >> a[i];
		int ans = 1000;
		
		for(int i = 1; i < ans; i++)
		{
			int sum = 0;
			for(int j = 0; j < n; j++)
			{
				sum += max(0, ((a[j]/i) + (a[j] % i > 0)) - 1);
			}
			ans = min(ans, i + sum);
		}
		
		printf("Case #%d: %d\n", test, ans);
	}
	
	return 0; 
} 
