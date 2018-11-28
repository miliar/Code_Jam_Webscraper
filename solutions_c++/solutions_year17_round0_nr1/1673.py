#include <vector>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <list>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cassert>
#include <ctime>
#include <cctype>
#include <cstring>
#include <bitset>
#include <algorithm>
#include <iomanip>

#define ld long double
#define ll long long
#define ull unsigned long long
#define pb push_back
#define mp make_pair
#define fst first
#define snd second
#define y0 _y0
#define y1 _y1

using namespace std;

template < typename T > T abs(T x)
{
    return x > 0 ? x : -x;
}

template < typename T > T sqr(T x)
{
    return x * x;
}

int main()
{
	freopen("input1.txt", "r", stdin);
	freopen("output1.txt", "w", stdout);
	
	int t;
	
	cin >> t;
	
	int initt = t;
	
	while (t--) {
		int l;
		string s;
		
		cin >> s >> l;
		
		int n = s.size();
		vector <int> c(n + 5);
		
		int ans = 0;
		int cnt = 0;
		
		for (int i = 0; i < n - l + 1; i++) {
			cnt -= c[i];
			if (((cnt & 1) && s[i] == '-') || (!(cnt & 1) && s[i] == '+')) {
				continue;
			}
			else {
				cnt++;
				ans++;
				c[i + l] = 1;
			}
		}
		bool f = 1;
		for (int i = n - l + 1; i < n; i++) {
			cnt -= c[i];
			if (((cnt & 1) && s[i] == '-') || (!(cnt & 1) && s[i] == '+')) {
				continue;
			}
			else {
				f = 0;
				break;
			}
		}
		cout << "Case #" << initt - t << ": ";
		if (f)
			cout << ans;
		else
			cout << "IMPOSSIBLE";
		
		cout << "\n"; 
	}	
    return 0;   
}

