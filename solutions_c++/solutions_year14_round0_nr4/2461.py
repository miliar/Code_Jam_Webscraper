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
	input("D-large.in");
	output("D.txt");
	int t, n, kasus = 0;
	double a[10000], b[10000];
	bool sudah[10000];
	cin >> t;
	while (t--) {
		cin >> n;
		REP(i, 0, n) cin >> a[i];
		REP(i, 0, n) cin >> b[i];
		sort(a, a+n);
		sort(b, b+n);
		int second = 0;
		reset(sudah, false);
		REP(i, 0, n) {
			bool ketemu = false;
			REP(j, 0, n) {
				if (b[j] > a[i] && sudah[j] == false) {
					ketemu = true;
					sudah[j] = true;
					break;
				}
			}
			
			if (!ketemu) {
				second++;
				REP(j, 0, n) {
					if (sudah[j] == false) {
						sudah[j] = true;
						break;
					}
				}
			}
		}
		
		int first = 0;
		double minim = 1000000000;
		//REP(i, 0, n) cout << a[i] << " "; cout << endl;
		//REP(i, 0, n) cout << b[i] << " "; cout << endl;
		int A = 0, B = 0, batas = n-1;
		while (1) {
			if (a[A] < b[B]) {
				batas--;
				A++;
			} else {
				first++;
				A++;
				B++;
			}
			if (B > batas) break;
		}
		//REP(i, 0, n) minim = min(b[i], minim);
		//REP(i, 0, n) if (a[i] < minim) first--;
		cout << "Case #" << ++kasus << ": " << first << " " << second << endl;
	}
    return 0;
}

/*
    DON'T HACK MY CODE :)
*/