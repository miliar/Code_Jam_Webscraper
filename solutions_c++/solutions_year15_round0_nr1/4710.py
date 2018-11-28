#include <cstdio>
#include <cstring>
#include <stack>
#include <queue>
#include <vector>
#include <map>
#include <utility>
#include <string>
#include <algorithm>
#include <cmath>
#include <iostream>
#include <fstream>
#include <sstream>
#include <set>
using namespace std;
// template

// abbreviations
#define vi vector <int>
#define ii pair <int, int>
#define a first
#define b second
#define vii vector <ii>
#define mii map <int, int>
#define que queue
#define pque priority_queue
#define stk stack
#define lsone(value) (value)&(-value)

typedef unsigned long long ull;
typedef long long ll;

class Fenwick {
private:
	vector<int> arr;
	const int size;
public:
	Fenwick(int n) : arr(n+1), size(n) {
		for (int it = 0; it < arr.size(); ++it)
			arr[it] = 0;
	}
	void add(int v, int k) {
		for (;k <= size; k += lsone(k)) {
			arr[k] += v;
		}
	}
	int get(int k) {
		int total = 0;
		for (;k > 0; k -= lsone(k))  {
			total += arr[k];
		}
		return total;
	}
};

template <typename U> class Comparator {
public:
    bool operator() (const U lhs, const U rhs) {
        // implement
        return true;
    }
};
// end of template

int main() {
    // freopen("A-large.in", "r", stdin);
    // freopen("A-large.out", "w", stdout);
    int nt;
    scanf("%d", &nt);
    
    char s[1005];
    for (int t = 1; t <= nt; ++t) {
    	int smax;
    	scanf("%d %s", &smax, s);
    	int ans = 0;
    	int nPeople = 0;
    	for (int it = 0; it <= smax; ++it) {
    		if (it > nPeople) {
    			ans += it-nPeople;
    			nPeople = it;
    		}
    		nPeople += (s[it]-'0');
    	}
    	printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}