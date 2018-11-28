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

const long double eps = 1e-11;
pair<long double, long double> a[111];
int n;
long double v;
long double good;

bool can(long double m)
{
	long double v0 = good * m;
	int i = 0, j = n - 1;
	long double v1 = m, v2 = m;
	while (a[i].first < 0 && a[j].first > 0) {
		if (-a[i].first * a[i].second * v1 > a[j].first * a[j].second * v2) {
			long double delta = (a[j].first * a[j].second * v2) / (-a[i].first * a[i].second);
			v1 -= delta;
			v0 += a[j].second * v2 + a[i].second * delta;
			v2 = m;
			j--;
		} else {
			long double delta = (-a[i].first * a[i].second * v1) / (a[j].first * a[j].second);
			v2 -= delta;
			v0 += a[i].second * v1 + a[j].second * delta;
			v1 = m;
			i++;
		}
	}
	return v0 > v;
}

double check()
{
	long double l = 0;
	long double r = 1e15;
	while (r - l > eps)
	{
		long double m = (l + r) / 2;
		if (can(m))
			r = m;
		else
			l = m;
	}
	return (l + r) / 2;
}

int main(){ 
	ios_base::sync_with_stdio(false); 
	int T;
	cin >> T;
	for(int test = 1; test <= T; test++)
	{
		cerr << test << endl;
		long double x;
		cin >> n >> v >> x;
		
		for(int i = 0; i < n; i++)
		{
			cin >> a[i].second >> a[i].first;
			a[i].first -= x;
		}
		sort(a, a + n);
		good = 0;
		for(int i = 0; i < n; i++)
			if (a[i].first == 0)
				good += a[i].second;
		cout << "Case #" << test << ": ";
		if (a[0].first > 0 || a[n - 1].first < 0)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << fixed << setprecision(10) << check() << endl;
			
		if (a[0].first <0 && a[n - 1].first > 0 && check() > 1e10)
			cerr << "PANIC!!!" << endl;
	}
	
	
	return 0; 
} 
