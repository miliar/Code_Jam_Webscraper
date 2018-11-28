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
typedef pair<int, int> pii;
#define SZ(x) (int)(x.size())
#define F0(i,n) for(int i=0;i<n;i++)
#define F1(i,n) for(int i=1;i<=n;i++)
const int INF = 987654321;
ll gcd(ll x, ll y) { return y ? gcd(y, x%y) : x; }
int bc(int n) { return n ? bc((n - 1)&n) + 1 : 0; }
#define PI 3.141592
int n;

char buffer[1001];

int main() {
	string infile = "A-large.in";
	string outfile = "out.txt";
	
	freopen(infile.c_str(), "r", stdin);
	freopen(outfile.c_str(), "w", stdout);
	int tt;
	
	scanf("%d", &tt);
	for(int tc = 1; tc<= tt; tc++) {
		int S,K;
		int res = 0;
		scanf("%s %d", buffer, &K);
		S = strlen(buffer);
		for (int i = 0; i <= S - K; i++) {
			if (buffer[i] == '-') {
				res++;
				for (int j = 0; j < K; j++) {
					if (buffer[i + j] == '+')
						buffer[i + j] = '-';
					else
						buffer[i + j] = '+';
				}
			}
		}
		bool impossible = false;
		for (int i = S - K + 1; i < S; i++)
			if (buffer[i] == '-') {
				impossible = true;
				break;
			}
		if (impossible) {
			printf("Case #%d: IMPOSSIBLE\n", tc);
			continue;
		}
		printf("Case #%d: %d\n", tc,res );
	}
}