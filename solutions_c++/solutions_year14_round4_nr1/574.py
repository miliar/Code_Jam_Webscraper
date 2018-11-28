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

#define pb push_back 
#define mp make_pair 
#define float long double 
#define ll long long 
#define abracadabra next 
#define pii pair<int, int> 

using namespace std; 

int a[11111];

int main(){ 
	int T;
	cin >> T;
	for(int test = 0; test < T; test++)
	{
		printf("Case #%d: ", test + 1);
		int n, x;
		cin >> n >> x;
		for(int i = 0; i < n; i++)
		{
			cin >> a[i];
		}
		sort(a, a + n);
		int i = 0, j = n - 1, ans = 0;
		while (i <= j)
		{
			if (i == j) {
				ans++;
				break;
			}
			if (a[i] + a[j] > x)
			{
				ans++;
				j--;
			} else {
				ans++;
				i++, j--;
			}
		}
		cout << ans << endl;
		
		
	}
	
	
	return 0; 
} 
