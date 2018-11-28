// INCLUDE LIST
#include <cstdio>
#include <iostream>
#include <queue>
#include <stack>
#include <string>
#include <cstring>
#include <algorithm>
#include <map>
#include <set>
#include <list>
#include <vector>
#include <cstdlib>
#include <cctype>
#include <cmath>
using namespace std;

// DEFINE LIST
#define REP(_I, _J, _K) for(_I = (_J) ; _I < (_K) ; _I++)
#define input(_A)       freopen(_A, "r", stdin);
#define output(_A)      freopen(_A, "w", stdout);
#define INPUT           input("in.txt");
#define OUTPUT          output("out.txt");
#define CASE_LEFT(_A)   fprintf(stderr, "Cases left: %d\n", _A);
#define hold            {fflush(stdin); getchar();}
#define reset(_A, _B)   memset((_A), (_B), sizeof (_A));
#define debug           printf("<<TEST>>\n");
#define eps             1e-11
#define f_cmp(_A, _B)   (fabs((_A) - (_B)) < eps)
#define phi             acos(-1)
#define pb              push_back
#define value(_A)       cout << "Variabel -> " << #_A << " -> " << _A << endl;
#define st              first
#define nd              second

// TYPEDEF LIST
typedef pair<int, int>  ii;
typedef vector<int>     vi;
typedef vector<ii>      vii;
typedef long long       LL;

// VAR LIST
int MAX =               1000000;
int MIN =               -1000000;
int INF =               1000000000;
int x4[4] =             {0, 1, 0, -1};
int y4[4] =             {1, 0, -1, 0};
int x8[8] =             {0, 1, 1,  1,  0, -1, -1, -1};
int y8[8] =             {1, 1, 0, -1, -1, -1,  0,  1};
int i, j, k;

// MAIN CODE
int main () {
	input("B-large.in");
	OUTPUT;
	int t, kasus = 0;
	double c, f, x;
	cin >> t;
	while (t--) {
		cin >> c >> f >> x;
		double minimal = 1000000000;
		for(int beli = 0;beli <= 1000000;beli++) {
			double kue_regen = ((double)beli * f) + 2.0;
			double waktu_ke_beli = 0.0;
			double kue_temp = 2.0;
			for(int farm = 1;farm <= beli;farm++) {
				waktu_ke_beli += c / kue_temp;
				kue_temp += f;
			}
			double total_time = waktu_ke_beli + (x / kue_regen);
			if (minimal > total_time)
		 		 minimal = total_time;
			else break;
		}
		printf("Case #%d: %.7lf\n", ++kasus, minimal);
	}
  return 0;
}

/*
    DON'T HACK MY CODE :)
*/
