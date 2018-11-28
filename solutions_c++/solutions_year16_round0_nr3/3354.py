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

LL isPrime(LL number) {
	for (LL i = 2ll; i * i <= number; i++) {
		if (number % i == 0ll)
			return i;
	}
	
	return -1ll;
}

LL pangkat(LL A, LL B) {
	LL res = 1ll;
	for (LL i = 0ll; i < B; i++) {
		res *= A;
	}
	
	return res;
}

LL inBase(LL number, LL base) {
	LL res = 0ll;
	for(LL i = 0ll; i < 16ll; i++) {
		res += ((number & (1ll << i)) > 0ll) * pangkat(base, i);
	}
	
	return res;
}

void printAll(int num, vector<LL> divider) {
	for(int i = 15; i >= 0; i--)
		cout << (((num & (1ll << i)) > 0ll) ? "1" : "0");
	
	for(int i = 0; i < divider.size(); i++) 
		cout << " " << divider[i];
		
	cout << endl;
}

// MAIN CODE
int main () {
	output("out.txt");
	
	int t;
	int n, m;
	cin >> t;
	cin >> n >> m;
	cout << "Case #1:" << endl;
	
	LL allNumber = 0ll;
	
	for (LL i = 1ll; i < 65536ll; i++) {
		if ((i & (1ll << 0ll)) > 0ll && (i & (1ll << 15ll)) > 0ll) {
			vector<LL> divider;
			bool allPrime = true;
			for (int j = 2ll; j <= 10ll; j++) {
				LL num = inBase(i, j);
				LL dividerNum = isPrime(num);
				if (dividerNum == -1ll)
					allPrime = false;
				else divider.push_back(dividerNum);
			}
			
			if (allPrime) {
				printAll(i, divider);
				allNumber++;
				
				if (allNumber >= 50ll)
					return 0;
			}
			
			divider.clear();
		}
	}
    return 0;
}

