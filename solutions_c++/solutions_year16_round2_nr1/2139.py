//	Problem A

const bool debug=true;

#include <iostream>
#include <cstdio>
#include <iomanip>
#include <sstream>
#include <cmath>
#include <numeric>
#include <algorithm>
#include <functional>
#include <cstring>
#include <cstdlib>
#include <cstdarg>
#include <utility>
#include <cassert>
#include <ctime>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <bitset>
#include <deque>
#include <queue>
#include <stack>

#define TIMES(n) for (int i=0; i<(n); ++i)
#define FOR(i,s,t) for (int (i)=(s); (i)<=(t); ++(i))
#define RESET(a) memset((a), 0, sizeof((a)))
#define P(x, ...) printf((x), ##__VA_ARGS__)
#define D(x, ...) if (debug) printf((x), ##__VA_ARGS__)
#define MP(x, y) make_pair((x), (y))

const int INF = 0x7F7F7F7F; // or (unsigned)(-1)>>1
int caseI = 0, caseD = -1;

using namespace std;

//void P(char *f, ...) {va_list v; va_start(v, f); vprintf(f, v); va_end(v);}
//void D(char *f, ...) {if (!debug) return; va_list v; va_start(v, f); vprintf(f, v); va_end(v);}


/*

Sample Input:



Sample Output:


*/

const int maxN = 2005, maxM = 1005;

typedef pair<int, int> ii;
typedef vector<vector<ii> > graph;

string eng_numbers[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
vector<vector<pair<char, int> > > process_order;

class Qs {
	int n, m, k;
	//int e[maxN][maxN];
	char s[maxN];
	int num[10];
	int char_count[250];

public:
	Qs() {
		RESET(num);
		RESET(char_count);
	}

	bool input() {

		if (scanf("%s", s) != 1)
			return false;
		
		n = strlen(s);



		return true;
	}

	void solve() {
		TIMES(n) {
			++char_count[s[i]];
		}

		for (std::vector<vector<pair<char, int> > >::iterator po_it = process_order.begin(); po_it != process_order.end(); ++po_it)
		{
			for (std::vector<pair<char, int> >::iterator po_r_it = po_it->begin(); po_r_it != po_it->end(); ++po_r_it)
			{
				int times = char_count[po_r_it->first];
				if (times > 0) {
					num[po_r_it->second] += times;
					TIMES(eng_numbers[po_r_it->second].length()) {
						char_count[eng_numbers[po_r_it->second][i]] -= times;
					}
				}
			}
			// D(">> %s %d %d %d %d %d %d %d %d %d %d\n", s, num[0], num[1], num[2], num[3], num[4], num[5], num[6], num[7], num[8], num[9]);
		}

		printf("Case #%d: ", caseI);

		FOR(j, 0, 9) {
			TIMES(num[j]) printf("%d", j);
		}

		printf("\n");


	}
};

void pre_process() {
	//freopen("A.in", "r", stdin);
	//freopen("A.out", "w", stdout);
	scanf("%d%*c", &caseD);
	
	{
		vector<pair<char, int> > v;
		v.push_back(MP('Z', 0));
		v.push_back(MP('W', 2));
		v.push_back(MP('U', 4));
		v.push_back(MP('X', 6));
		v.push_back(MP('G', 8));
		process_order.push_back(v);
	}
	{
		vector<pair<char, int> > v;
		v.push_back(MP('H', 3));
		v.push_back(MP('F', 5));
		process_order.push_back(v);
	}
	{
		vector<pair<char, int> > v;
		v.push_back(MP('V', 7));
		v.push_back(MP('I', 9));
		process_order.push_back(v);
	}
	{
		vector<pair<char, int> > v;
		v.push_back(MP('N', 1));
		process_order.push_back(v);
	}
}

int main() {
	Qs *p = new Qs;
	pre_process();
	while ((++caseI|1) && caseD-- && p->input()) {
		p->solve();
		delete p;
		p = new Qs;
	}
	delete p;
	return 0;
}
