#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <iomanip>
#include <iostream>
#include <istream>
#include <map>
#include <numeric>
#include <ostream>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <vector>


using namespace std;


// Powered by caide (code generator, tester, and library code inliner)

// variable definition here
int n, p[128];
char ch[128];
int m;
char cool[8][32];
int len[8];

int pp[8][128];

void initialize(std::istream &in) {
	// initialize variables here
	in >> n;
	for (int i = 0; i < n; i++) {
		in >> p[i];
		if (p[i] == 0)
			p[i] = i;
		else
			p[i]--;
	}
	in >> ch;
	in >> m;
	for (int i = 0; i < m; i++) {
		in >> cool[i];
		len[i] = strlen(cool[i]);
	}

	for (int i = 0; i < n; i++)
		pp[0][i] = p[i];
	for (int i = 1; i < 8; i++)
		for (int j = 0; j < n; j++)
			pp[i][j] = pp[i - 1][pp[i - 1][j]];

	// debug_arr(pp, 8, n);
}

int pi[8][32];
void build_kmp() {
	for (int i = 0; i < m; i++) {
		pi[i][0] = 1;
		for (int j = 1; j <= len[i]; j++) {
			for (int k = 1; k <= j; k++) {
				bool ok = true;
				for (int ii = k; ii < j; ii++)
					if (cool[i][ii] != cool[i][ii - k])
						ok = false;
				if (ok) {
					pi[i][j] = k;
					break;
				}
			}
			assert(pi[i][j] != 0);
		}
		/*
		for (int j = 0; j <= len[i]; j++)
			cerr << pi[i][j] << " ";
		cerr << endl;
		*/
	}
}

char str[128];
bool is_done[128];
int undone[128];
int position[128];

void gen() {
	for (int i = 0; i < n; i++) {
		is_done[i] = false;
		undone[i] = i;
		position[i] = i;
	}
	// optimizable - later!
	for (int i = 0; i < n; i++) {
		// bias here
		int pos = rand() % (n - i);
		int v = undone[pos];
		for (int j = 7; j >= 0; j--)
			if (!is_done[pp[j][v]])
				v = pp[j][v];

		// MISTAKE: different order
		assert(!is_done[v]);
		is_done[v] = true;
		// debug(v);
		if (i < n - 1) {
			int nv = undone[n - 1 - i];
			int v_pos = position[v];
			undone[v_pos] = nv;
			position[nv] = v_pos;
		}

		str[i] = ch[v];
	}
	str[n] = '\0';
}

int accum[8];
void solve_case(std::ostream &out) {
	build_kmp();

	// solve the case here
	for (int i = 0; i < m; i++)
		accum[i] = false;
	const int loop_cnt = 50000;
	for (int loop = 0; loop < loop_cnt; loop++) {
		gen();
		// debug(str);
		for (int i = 0; i < m; i++) {
			// debug(cool[i]);
			// run KMP
			int match = 0;
			bool found = false;
			for (int j = 0; j < n; j++) {
				while (match >= 0 && str[j] != cool[i][match])
					match -= pi[i][match];
				match++;
				// debug(match)
				if (match == len[i]) {
					found = true;
					break;
				}
			}
			if (found)
				accum[i]++;
		}
	}
	// debug_arr(accum, m)
	for (int i = 0; i < m; i++)
		out << (double)accum[i] / loop_cnt << " ";
	out << endl;
}

void solve(std::istream& in, std::ostream& out) {
    out << std::setprecision(12);

	int T;
	in >> T;
	for (int t = 1; t <= T; t++) {
		cerr << "Case #" << t << " running" << endl;

		initialize(in);
		out << "Case #" << t << ": ";
		solve_case(out);

		cerr << "Case #" << t << " done" << endl;
	}
}


#include <fstream>


int main() {
    
    ios_base::sync_with_stdio(0);
    cin.tie(0);


    istream& in = cin;


    ostream& out = cout;

    solve(in, out);
    return 0;
}


