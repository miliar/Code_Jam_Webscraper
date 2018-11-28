#include <algorithm>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <memory>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define EPS 1e-10
#define INF 1000000
#define mp make_pair
#define pb push_back

typedef vector<int> vi;
typedef vector<vi> vii;
typedef pair<int,int> pii;
typedef long long ll;

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		string S;
		cin >> S;
		int g = 1;
		for (int i = 1; i < S.size(); i++) {
			if (S[i] != S[i-1]) {
				g++;
			}
		}
		if (S[S.size()-1] == '+') {
			g--;
		}
		cout << "Case #" << t << ": " << g << endl;
	}
}

