// Wsl_F

#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <fstream>
#include <sstream>
#include <cmath>
#include <math.h>
#include <iomanip>
#include <algorithm>
#include <functional>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <string.h>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <bitset>
#include <numeric>
#include <cassert>
#include <time.h>
#include <ctime>
#include <memory.h>
#include <complex>
#include <utility>
#include <climits>
#include <cctype>


using namespace std;
#pragma comment(linker, "/STACK:1024000000,1024000000")


typedef long long LL;
typedef unsigned long long uLL;
typedef double dbl;
typedef vector<int> vi;
typedef vector<LL> vL;
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef pair<LL, LL> pLL;

#define mp(x,y)  make_pair((x),(y))
#define pb(x)  push_back(x)
#define sqr(x) ((x)*(x))


map<string, char> win;

bool check(string s) {
	while (s.length() > 1) {
		string s2;
		int l = s.length() / 2;
		for (int i = 0; i < l; i++) {
			char c= win[s.substr(2 * i, 2)];
			if (c == 'b') {
				return false;
			}
			s2 += c;
		}
		s = s2;
	}

	return true;
}

void solve()
{
	LL n, r, p, s;
	cin >> n >> r >> p >> s;

	string str = "";
	for (int i = 0; i < p; i++) {
		str += 'P';
	}

	for (int i = 0; i < r; i++) {
		str += 'R';
	}

	for (int i = 0; i < s; i++) {
		str += 'S';
	}

	//int l = str.length();
	do
	{
		if (check(str)) {
			cout << str << endl;
			return;
		}
	} while (next_permutation(str.begin(), str.end()));

	cout << "IMPOSSIBLE" << endl;
}

int main()
{
 ios_base::sync_with_stdio(0);
 cin.tie(0);
 srand(__rdtsc());

 freopen("A-small-attempt0.in","r",stdin);
 freopen("A-small-output.txt","w",stdout);
 //cout<<fixed;
 //cout<<setprecision(9);

 win["RS"] = 'R';
 win["SP"] = 'S';
 win["PR"] = 'P';
 win["SR"] = 'R';
 win["PS"] = 'S';
 win["RP"] = 'P';
 win["RR"] = 'b';
 win["SS"] = 'b';
 win["PP"] = 'b';



 int T;
 cin>>T;
 for (int testCase= 1; testCase <= T; testCase++)
 {
     cout<<"Case #"<<testCase<<": ";
     solve();
 }


 return 0;
}
