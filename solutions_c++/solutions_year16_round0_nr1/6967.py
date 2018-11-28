#include <iostream>
#include <chrono>
#include <map>
#include <vector>
#include <array>
#include <list>
#include <set>
#include <queue>
#include <stack>
#include <deque>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <cmath>
#include <string>
#include <cstring>

#define forn_i(N) for(int i = 0; i < N; ++i)
#define forn_j(N) for(int j = 0; j < N; ++j)

#define DEBUG

int gcd (int a, int b ) {
	if (a == 0) return b;
	return gcd (b % a, a);
}

using namespace std;

int solution (int n)
{
	long long temp = n;
	set <int> se;
	
	if (n == 0) return -1;
	
	for (int it = 0; it < 1000000; ++it, temp += n) {
		long long bl = temp;
		while (bl) {
			se.insert(bl%10);
			bl /= 10;
		}
		if (se.size() == 10) return temp;
	}
	
	return -1;
}

void solve()
{
	int t, n;
	cin >> t;
	
	for (int it = 1; it <= t; ++it) {
		cin >> n;
		
		cout << "Case #" << it << ": ";
		
		if ((n = solution(n)) == -1) cout << "INSOMNIA";
		else cout << n;
		
		cout << endl;
	}
}

int main()
{
	
#ifdef DEBUG
	freopen("out.txt", "w", stdout);
	freopen("in.txt", "r", stdin);
	auto start = chrono::system_clock::now();
#endif
	
	solve();
	
#ifdef DEBUG
	auto elapsed_seconds = chrono::system_clock::now() - start;
	printf("\n\nTime: %fs\n", elapsed_seconds.count());
#endif
	
	return 0;
}
