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

const int N = (int)(1e5 + 20);
const lli M = 4294967297ll;

int g[300][300];

int main()
{
ios_base::sync_with_stdio(0);
#ifdef FILE_IO
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif    
	int T;
	cin >> T;
	for(int qq = 0; qq < T; ++qq) {
		cout << "Case #" << qq+1 << ": ";
		
		int n;
		cin >> n;
		vector<string> v(n);
		for(int i = 0; i < n; ++i) cin >> v[i];

		vector<char> letter;
		vector<int> minL, maxL;
		for(int i = 0; i < v[0].length(); ) {
			int j = i + 1;
			while(j < v[0].length() && v[0][i] == v[0][j]) ++j;
			letter.push_back(v[0][i]);
			minL.push_back(j-i); maxL.push_back(j-i);

			g[0][letter.size() - 1] = j-i;

			i = j;
		}
	
		bool f = true;
		for(int k = 1; k < n && f; ++k) {
			int pos = 0;
			for(int i = 0; i < v[k].length(); ) {
				int j = i + 1;
				while(j < v[k].length() && v[k][i] == v[k][j]) ++j;
				if (pos >= letter.size() || letter[pos] != v[k][i]) {
					f = false;
					break;
				}
				minL[pos] = min(minL[pos], j-i);
				maxL[pos] = max(maxL[pos], j-i);

				g[k][pos] = j-i;
				
				++pos;
				i = j;
			}
			if (pos != letter.size()) f = false;
		}

		if (f == false) {
			cout << "Fegla Won";
		} else {
			lli ans = 0;
			for(int i = 0; i < letter.size(); ++i) {
				lli lans = 10202020;
				for(int p = minL[i]; p <= maxL[i]; ++p) {
					lli counter = 0;
					for(int k = 0; k < n; ++k) {
						counter += abs(p-g[k][i]);
					}
					lans = min(lans, counter);
				}
				ans += lans;
			}
			cout << ans;
		}

		
		
		cout << endl;
	}
    return 0;
}