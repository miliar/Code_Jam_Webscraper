///////////////////////IN THE NAME OF GOD
#include <iostream>
#include <vector>
#include <stack>
#include <string>
#include <algorithm>
#include <cmath>
#include <set>
#include <queue>
#include <map>
#include <fstream>
#include <utility>
#include <sstream>
#include <list>
#include <iomanip>
#include <functional>
#include <deque>
#include <ctime>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <complex>
#include <climits>
#include <cctype>
#include <cassert>
#include <bitset>
#include <limits>
#include <numeric>

using namespace std;

#define     For(i,a,b)      for (int i=a; i<(int)b; i++)
#define     Rep(i,a)        for (int i=0; i<(int)a; i++)
#define     ALL(v)          (v).begin(),(v).end()
#define     Set(a,x)        memset((a),(x),sizeof(a))
#define     EXIST(a,b)      find(ALL(a),(b))!=(a).end()
#define     Sort(x)         sort(ALL(x))
#define     UNIQUE(v)       Sort(v); (v).resize(unique(ALL(v)) - (v).begin())
#define     SF              scanf
#define     PF              printf
#define     timestamp(x)    printf("Time : %.3lf s.\n", clock()*1.0/CLOCKS_PER_SEC)
#define     INF             1e9
#define     pii             pair < int , int >
#define     MP              make_pair
#define     MOD             1000000007
#define     EPS             1e-9
#define     ll              long long
#define     MAXN            100000+10
#define     Dbug            cout<<""
#define     PI                3.1415926535897932384626433
//int month[]={0,31,29,31,30,31,30,31,31,30,31,30,31};

int main(int argc, char *argv[]) {
	ios::sync_with_stdio(false);
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int t , tc = 1 ;
	cin >> t;
	while (t--) {
		cout << "Case #" << tc++ << ": ";

		string sen , tmp ;
		int res = 0;
		cin >> sen;
		while (sen.find('-') != -1 && sen.size() ) {
			while (sen[sen.size() - 1] == '+') sen.erase(sen.begin() + sen.size() - 1);
			int p = 0;
			while (p < sen.size() && sen[p] == '+') p++;
			Rep(i, p ) {
				if (sen[i] == '+') sen[i] = '-';
			}
			if (p) res++;
			p = 0;
			while (p < sen.size() && sen[p] == '-') p++;
			if (p) res++;
			for (int i = sen.size()-1; i >= p; i--) {
				tmp.push_back(sen[i] == '+' ? '-' : '+');
			}
			sen = tmp;
			tmp.clear();
		}
		cout << res << endl;
	}
	return 0;
}