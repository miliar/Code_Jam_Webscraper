#include <iostream>
#include <math.h>
#include <string.h>
#include <string>
#include <cmath>
#include <stdio.h>
#include <vector>
#include <map>
#include <list>
#include <queue> 
#include <algorithm>
#include <bitset>
#include <set>

using namespace std;

#define REP(i,n) for(long long int i = 0; i < int(n); ++i)
#define REPV(i, n) for (long long int i = (n) - 1; (int)i >= 0; --i)
#define FOR(i, a, b) for(long long int i = (int)(a); i < (int)(b); ++i)

#define ALL(v) (v).begin(), (v).end()
#define PF push_front
#define PB push_back
#define MP make_pair
#define F first
#define S second

#define lli long long int

string v = "aeiuo";

int main()
{
#ifdef FILE_IO
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif	
	int T;
	cin >> T;
	REP(q, T) {
		cout << "Case #" << (q + 1) << ": ";
		lli n;
		string s;
		cin >> s >> n;
		
		int cc = 0;
		int *a = new int[s.length()];
		for(int i = 0; i < s.length(); ++i) {
			if (s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u' ) {
				a[i] = cc = 0;
			} else {
				a[i] = ++cc;
			}
		}
		lli count = 0; 
		lli last = 0;
		lli len = s.length();
		for (lli i = s.length() - 1; i >= n - 1; --i) {
			if (a[i] >= n) {
				count += (i - n + 1 + 1) * (len - i - last);
				last += len - last - i;
			}
		}
		cout << count << endl;
	}
    return 0;
}