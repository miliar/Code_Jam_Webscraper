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
#include <functional>
#include <algorithm>
#include <bitset>
#include <set>
#include <stack>
#include <limits>
#include <sstream>
#include <ctime>
#define endl '\n'

using namespace std;

#define lli long long int
#define MP make_pair

const int N = (int)(1e4 + 20);
const int L = 80;
const lli M = 1000000007;

string s[20];
int la[20], lb[20];
int b[20];

int t[27];

int main()
{
ios_base::sync_with_stdio(0);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

	int T;
	cin >> T;
	for(int qq = 0; qq < T; ++qq) {
        cout << "Case #" << qq + 1 << ": ";

		int n;
		cin >> n;
		for(int i = 0; i < n; ++i) {
			cin >> s[i];
			la[i] = s[i][0]; lb[i] = s[i][s[i].length() - 1];
			b[i] = 0;
			for(int j = 0; j < s[i].length(); ++j) b[i] |= 1 << (s[i][j] - 'a');
		}
		vector<int> v(n);
		for(int i = 0; i < n; ++i) v[i] = i;
		lli ans = 0;
		do{
			bool fl = true;
			int cur = 26;
            memset(t, 0, 27*sizeof(int));
			for(int i = 0; i < n && fl; ++i) {
                    int id = v[i];
				for(int j = 0; j < s[id].length(); ++j) {
                    if (s[id][j]-'a' != cur) {
                        cur = s[id][j]-'a';
                        if (t[cur]) {
                            fl = false;
                            break;
                        } else t[cur] = 1;
                    }
				}
			}
			if (fl) ++ans;
		} while(next_permutation(v.begin(), v.end()));

		cout << ans << endl;
	}
    return 0;
}
