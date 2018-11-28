// main.cpp

#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <functional>
#include <bitset>
#include <deque>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <vector>
#include <numeric>
#include <complex>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <utility>

#define i64 long long
#define ui64 unsigned long long

using namespace std;

#define READ_IN_FILE 1

#ifdef ONLINE_JUDGE
#define READ_IN_FILE 0
#endif

vector<int> vi;
vector<char> vc;
vector<string> vs;

char str[10000];

double solve()
{
	return 0;
}

void multi_d(char sa, char a, char sb, char b, char &so, char &o) {
	char s = sa * sb;
	
	if (a == '1') {
		switch (b) {
			case '1':
				o = '1'; so = s *  1; break;
			case 'i':
				o = 'i'; so = s *  1; break;
			case 'j':
				o = 'j'; so = s *  1; break;
			case 'k':
				o = 'k'; so = s *  1; break;
		}
	} else if (a == 'i') {
		switch (b) {
			case '1':
				o = 'i'; so = s *  1; break;
			case 'i':
				o = '1'; so = s * -1; break;
			case 'j':
				o = 'k'; so = s *  1; break;
			case 'k':
				o = 'j'; so = s * -1; break;
		}
	} else if (a == 'j') {
		switch (b) {
			case '1':
				o = 'j'; so = s *  1; break;
			case 'i':
				o = 'k'; so = s * -1; break;
			case 'j':
				o = '1'; so = s * -1; break;
			case 'k':
				o = 'i'; so = s *  1; break;
		}
	} else if (a == 'k') {
		switch (b) {
			case '1':
				o = 'k'; so = s *  1; break;
			case 'i':
				o = 'j'; so = s *  1; break;
			case 'j':
				o = 'i'; so = s * -1; break;
			case 'k':
				o = '1'; so = s * -1; break;
		}
	}
}

int main()
{
	if (READ_IN_FILE) freopen("in.in", "r", stdin);
	
	int T;
	scanf("%d\n", &T);
	if (!T) {
		cerr << "Check input!" << endl;
		exit(0);
	}
	
	for (int t = 1; t <= T; t++) {
		vi.clear();
		int L = 0, X = 0;
		scanf("%d %d\n", &L, &X);
		if (L == 0 || X == 0) break;
		
		for (int l = 0; l < L; l++) {
			scanf("%c", &str[l]);
		}
		
		for (int x = 1; x < X; x++) {
			for (int l = 0; l < L; l++) {
				str[L * x + l] = str[l];
			}
		}
		
		int cur_pos = 0;
		int i_pos = -1, j_pos = -1, k_pos = -1;
		char cur_sym = 1; char cur_n = '1';
		int len = L * X;
		char re_j = 0;
		char possible = 0;
		
		while (1) {
			if (i_pos == -1 && cur_pos >= len) break;
			
			while (1) {
				if (re_j) { re_j = 0; break; }
				if (cur_pos >= len) {
					i_pos = -1;
					break;
				}
				multi_d(cur_sym, cur_n, 1, str[cur_pos], cur_sym, cur_n);
				if (cur_sym == 1 && cur_n == 'i') {
					i_pos = cur_pos;
					cur_sym = 1; cur_n = '1';
					cur_pos++;
					break;
				}
				cur_pos++;
			}
			
			// j
			while (1) {
				if (i_pos == -1) break;
				if (cur_pos >= len) {
					j_pos = -1;
					// Find new i
					cur_pos = i_pos + 1;
					cur_sym = 1; cur_n = 'i';
					break;
				}
				
				multi_d(cur_sym, cur_n, 1, str[cur_pos], cur_sym, cur_n);
				if (cur_sym == 1 && cur_n == 'j') {
					j_pos = cur_pos;
					cur_sym = 1; cur_n = '1';
					cur_pos++;
					break;
				}
				cur_pos++;
			}
			
			while (1) {
				if (j_pos == -1) break;
				if (cur_pos >= len) {
					k_pos = -1;
					break;
				}
				multi_d(cur_sym, cur_n, 1, str[cur_pos], cur_sym, cur_n);
				cur_pos++;
			}
			
			if (i_pos != -1 && j_pos != -1 && cur_sym == 1 && cur_n == 'k') {
				possible = 1;
				break;
			}
			
			if (i_pos != -1 && j_pos != -1) {
				re_j = 1;
			}
		}
		
		if (possible) {
			printf("Case #%d: %s\n", t, "YES");
		} else {
			printf("Case #%d: %s\n", t, "NO");
		}
	}
	
	if (READ_IN_FILE) fclose(stdin);
	return 0;
}
