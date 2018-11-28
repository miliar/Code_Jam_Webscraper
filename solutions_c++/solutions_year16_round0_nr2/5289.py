#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <string>
#include <cstring>
#include <iomanip>
#include <set>
#include <map>
#include <queue>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair <int, int> pii;
#define x first
#define y second
#define mp make_pair
#define pb push_back
const int N = (int)1e5 + 5, INF = (int)1e9;
const ld EPS = 1e-9;
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("a.txt", "w", stdout);
	int t;
	string s;
	cin >> t;
	for(int z = 1; z <= t; z++){
		cout << "Case #" << z << ": ";
		cin >> s;
		int n = (int)s.size();
		while(n > 0 && s[n - 1] == '+'){
			s.erase(n - 1, 1);
			n--;
		}
		if(n == 0){
			cout << "0\n";
			continue;
		}
		int ans = 0, k;
		while(1){
			for(k = 0; k < n && s[k] == '-'; k++)
				s[k] = '+';
			if(k)
				ans++;
			if(k == n)
				break;
			for(k = 0; k < n && s[k] == '+'; k++)
				s[k] = '-';
			if(k)
				ans++;
		}
		cout << ans << "\n";
	}
	return 0;
}