#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
using namespace std;


#define REP(i,n) for(int i=0; i<n; i++)
#define REPs(i,x,n) for(int i=x; i<n; i++)
#define SZ(x) x.size()
#define VVII vector< vector< pair<int, int> > > 
#define mem(f, a) memset(f, a, sizeof(f))
#define all(c) (c).begin(), (c).end()
#define PB push_back
#define MP make_pair
#define epsil 1e-9
#define infinit  1e8
#define ll long long
#define PI pair<int, int>
#define X first
#define Y second

//bool A[1000];

int main()
{
	ifstream cin("A-small-attempt0.in");
	ofstream cout("out.txt");
	int t; cin >> t;
	//TODO special case when impossible!
	REP(i, t){
		cout << "Case #" << i + 1 << ": ";
		int minans = infinit;
		int n;
		cin >> n;
		vector<string> strs(n), oristrs;
		bool good = 1;
		REP(j, n){
			string str;
			cin >> str;
			oristrs.push_back(str);
			for (int k = SZ(str) - 2; k >= 0; k--)if (str[k] == str[k + 1]) str.erase(str.begin() + k+1);
			strs[j]=str;
			if (j > 0) if (str != strs[j - 1]){
				good = 0;  break;
			}
		}
		if (!good) {
			cout << "Fegla Won" << endl;
			continue;
		}
		int strleng = strs[0].length();
		int ans = 0;
		vector<int> buf; REP(j, n) buf.push_back(0);
		REP(j, strleng){
			vector<int> counts(n, 0);
			char curch = strs[0][j];
			REP(k, n){
				while (oristrs[k][buf[k]] == curch){
					counts[k]++;
					buf[k]++;
				}
			}
			int share = accumulate(counts.begin(), counts.begin() + n, 0) / n;
			REP(k, n) ans += abs(counts[k] - share);
		}
		cout <<ans<< endl;
	}
	return 0;
}