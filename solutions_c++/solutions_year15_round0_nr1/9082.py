#include <iostream>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <string.h>
#include <map>
#include <fstream>
#include <functional>
#include <bitset>
#include <stack>
#include <set>
#include <climits>
#define MAX_N 200010
#define LOG 21
#define PI 3.141592653589
#define EPS 1e-6
#define MOD 1000000007
#define YJSNPI 810
#define INF (1 << 30)
#define ADD(a, b) a = (a + (ll)b) % MOD
#define MUL(a, b) a = (a * (ll)b) % MOD
#define MAX(a, b) a = max(a, b)
#define MIN(a, b) a = min(a, b)
#define x first
#define y second
#define REP(i, a, b) for(int i = a; i < b; i++)
#define RER(i, a, b) for(int i = a - 1; i >= b; i--)

using namespace std;

typedef long long ll;
typedef pair<int, int> pi;
typedef pair<int, pi> ppi;

void debug() {cout << endl; }

template<class FIRST, class... REST>
void debug(FIRST arg, REST... rest) { cout << arg << " "; debug(rest...); }

template<class T>
void showary(T begin, T end) { 
	while(begin != end) { cout << *begin << " "; begin++; } cout << endl; }

int T, N;
string str;

int main() {
	cin >> T;
	REP(t, 0, T) {
		cin >> N >> str;
		int cnt = 0, standing = 0;
		REP(i, 0, N + 1) {
			if(standing >= i) standing += str[i] - '0';
			else {
				cnt += i - standing;
				standing = i;
				standing += str[i] - '0';
			}
		}
		cout << "Case #" << t + 1 << ": " << cnt << endl;
	}
}
