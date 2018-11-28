#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define SZ(x) (int)(x.size())
#define F0(i,n) for(int i=0;i<n;i++)
#define F1(i,n) for(int i=1;i<=n;i++)
const int MOD = 1000002013;
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;
ll gcd(ll x, ll y) { return y ? gcd(y, x%y) : x; }
int bc(int n) { return n ? bc((n-1)&n)+1 : 0; }

int i, j, k, m, n, l;
char S[2005];

int main() {
    //freopen("x.in", "r", stdin);

	//freopen("A-small-attempt1.in", "r", stdin);
	//freopen("A-small-attempt1.out", "w", stdout);

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	//freopen("C-small-practice.in", "r", stdin);
	//freopen("C-small-practice.out", "w", stdout);
	//freopen("C-large-practice.in", "r", stdin);
	//freopen("C-large-practice.out", "w", stdout);

	int tn; cin >> tn;

#define ALP(x)  alpha[x-'A']
	F1(tt,tn) {
		cerr << tt << endl;
		cin >> S;
		int ans = 0;
		int alpha[26];
		F0(i, 26) alpha[i] = 0;
		n = strlen(S);
		F0(i, n) alpha[S[i] - 'A']++;
		int telnum[10];
		F0(i, 10) telnum[i] = 0;
		telnum[8] = ALP('G');
		ALP('E') -= telnum[8];
		ALP('I') -= telnum[8];
		ALP('G') -= telnum[8];
		ALP('H') -= telnum[8];
		ALP('T') -= telnum[8];
		telnum[6] = ALP('X');
		ALP('S') -= telnum[6];
		ALP('I') -= telnum[6];
		ALP('X') -= telnum[6];
		telnum[7] = ALP('S');
		ALP('S') -= telnum[7];
		ALP('E') -= telnum[7];
		ALP('V') -= telnum[7];
		ALP('E') -= telnum[7];
		ALP('N') -= telnum[7];
		telnum[3] = ALP('H');
		ALP('T') -= telnum[3];
		ALP('H') -= telnum[3];
		ALP('R') -= telnum[3];
		ALP('E') -= telnum[3];
		ALP('E') -= telnum[3];
		telnum[2] = ALP('T');
		ALP('T') -= telnum[2];
		ALP('W') -= telnum[2];
		ALP('O') -= telnum[2];
		telnum[0] = ALP('Z');
		ALP('Z') -= telnum[0];
		ALP('E') -= telnum[0];
		ALP('R') -= telnum[0];
		ALP('O') -= telnum[0];
		telnum[4] = ALP('R');
		ALP('F') -= telnum[4];
		ALP('O') -= telnum[4];
		ALP('U') -= telnum[4];
		ALP('R') -= telnum[4];
		telnum[5] = ALP('F');
		ALP('F') -= telnum[5];
		ALP('I') -= telnum[5];
		ALP('V') -= telnum[5];
		ALP('E') -= telnum[5];
		telnum[1] = ALP('O');
		ALP('O') -= telnum[1];
		ALP('N') -= telnum[1];
		ALP('E') -= telnum[1];
		telnum[9] = ALP('N')/2;
		ALP('N') -= telnum[9];
		ALP('I') -= telnum[9];
		ALP('N') -= telnum[9];
		ALP('E') -= telnum[9];

		F0(i, 26) cerr << alpha[i];
		cerr << endl;

  		printf("Case #%d: ", tt);
		F0(i, 10) {
			F0(j, telnum[i]) cout << char(i + '0');
		}
		cout << endl;
	}
	return 0;
}
