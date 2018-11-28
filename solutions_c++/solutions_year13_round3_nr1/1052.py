#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <bitset>
#include <deque>
#include <utility>
#include <sstream>

#define set(a, b, c, d) for(int i=b; i<c; i++) a[i]=d
#define INF 1000000000
#define FOR(i, a, b) for(int i=int(a); i<int(b); i++)
#define p2(b) (1 << (b))

using namespace std;

typedef unsigned long long ull;
typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

template <typename T> string toString(T n){ostringstream ss; ss << n; return ss.str();}
template <typename T> T toNum(const string &Text){istringstream ss(Text); T result; return ss >> result ? result : 0;}

string str;
long long n;

bool isCons(char c) {
	if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')
		return false;
	return true;
}

int main() {

	long long TC;
	cin >> TC;
	FOR(a, 1, TC+1) {

		cin >> str;
		cin >> n;

		long long len = str.length();

		long long count = 0;
		long long p1 = -1;
		long long p2 = -1;
		long long last = 0;
		FOR(i, 0, len) {
			if(isCons(str[i])) {
				if(p1 == -1) {
					p1 = i;
					p2 = i;
				}else
					p2++;
				if(p2 - p1 + 1 == n) {
					count += (len-p2)*(p1-last+1);
					last = p1 + 1;
					p1++;
				}
			}else {
				p1 = -1;
				p2 = -1;
			}
		}

		cout << "Case #" << a << ": " << count << endl;

	}

}