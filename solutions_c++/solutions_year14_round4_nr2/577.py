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

pii a[1111];
int p[1111];

bool cmp(pii a, pii b)
{
	return a.second < b.second;
}

int main(){ 
			int T;
	cin >> T;
	for(int test = 0; test < T; test++)
	{
		int n;
		printf("Case #%d: ", test + 1);
		cin >> n;
		for(int i = 0; i < n; i++)
		{
			cin >> a[i].first;
			a[i].second = i;
		}
		sort(a, a + n);
		for(int i = 0; i < n; i++)
			a[i].first = i;
		sort(a, a + n, cmp);
		for(int i = 0; i < n; i++)
			p[a[i].first] = i;
			
		int l = 0, r = n - 1,ans = 0;
		for(int i = 0; i < n - 1; i++)
		{
			if (p[i] - l <= r - p[i])
			{
				for(int j = p[i]; j > l; j--)
				{
					p[a[j - 1].first]++;
					swap(a[j], a[j - 1]);ans++;
				}
				l++;
			} else {
				for(int j = p[i]; j < r; j++)
				{
					p[a[j + 1].first]--;
					swap(a[j + 1], a[j]);
					ans++;
				}
				r--;
			}
		}
		cout << ans << endl;
		
	
	}
	
	
	return 0; 
} 
