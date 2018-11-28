// INCLUDE LIST
#include <cstdio>
#include <bitset>
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
#define CASE_LEFT(_A)   fprintf(stderr, "Cases left: %d\n", R);
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

bool valid(bool arr[]) {
	for(int i = 0; i < 10; i++) {
		if (!arr[i])
			return false;
	}
	
	return true;
}

// MAIN CODE
int main () {
	input("A-large.in");
	output("out.txt");
	
	LL t, n, kasus = 0ll;
	cin >> t;
	while (t--) {
		cin >> n;
		
		if (n == 0ll) {
			cout << "Case #" << ++kasus << ": INSOMNIA" << endl;
			continue;
		}
		
		bool arr[10];
		reset(arr, false);
		LL indx = 1ll;
		
		while(!valid(arr)) {
			int temp = n * indx++;
			while(temp > 0ll) {
				arr[temp % 10ll] = true;
				temp /= 10ll;
			}
		}
		
		cout << "Case #" << ++kasus << ": " << n * (indx - 1ll) << endl;
	}
    return 0;
}

