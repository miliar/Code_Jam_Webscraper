#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <complex>
#include <cstdio>
#include <vector>
#include <cctype>
#include <string>
#include <ctime>
#include <cmath>
#include <set>
#include <map>

typedef long double LD;
typedef long long LL;

using namespace std;

#define sz(A) (int)(A).size()
#define mp make_pair
#define pb push_back

const int N = int(1e6);

map<string, vector<int> > words;
char line[N], word[N];

bool getLang(int mask, int num) {
	if (num == 0) return false;
	if (num == 1) return true;
	return (mask & (1 << (num - 2)));
}

int main() {
	int t;
	cin >> t;
	for (int test = 0; test < t; test++) {
		cerr << test << endl;
		words.clear();
		int n;
		scanf("%d\n", &n);
		for (int i = 0; i < n; i++) {			
			gets(line);
			int pos = 0;
			while (sscanf(line + pos, "%s", word) != -1) {
				pos += strlen(word) + 1;
				string x = word;
				if (!words.count(x)) { 
					vector<int> v;
					words[x] = v;
				//	cerr << x << endl;
				}
				words[x].pb(i);
			}
			for (int j = 0; j <= pos; j++)
				line[j] = 0;
		}

		int res = int(1e9);

		for (int i = 0; i < (1 << (n - 2)); i++) {
			int cnt = 0;
			for (auto word = words.begin(); word != words.end(); word++) {
				/*if (!i) {
					cerr << (*word).first << " "; 
					for (int q = 0; q < (*word).second.size(); q++)
						cerr << (*word).second[q] << " ";
					cerr << endl;
				}*/

				bool eng = false, fr = false;
				for (int j = 0; j < (*word).second.size(); j++) {
					int lang = getLang(i, (*word).second[j]);
					//cerr << lang << " " << (*word).second[j] << " " << (*word).first << endl;
					if (lang) 
						fr = true;
					else
						eng = true;
				}
				if (fr && eng) {
					//cerr << "? " << (*word).first << endl;
					cnt++;
				}				
			}
			//cerr << i << " - " << cnt << endl;
			res = min(res, cnt);
		}

		printf("Case #%d: %d\n", test + 1, res);	
		//cerr << endl;
	}
	return 0;
}
