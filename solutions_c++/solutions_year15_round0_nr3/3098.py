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

char mult[4][4] = {{'h', 'i', 'j', 'k'}, 
					{'i', 'h', 'k', 'j'}, 
					{'j', 'k', 'h', 'i'}, 
					{'k', 'j', 'i', 'h'}};

char boolMult[4][4] = {{1, 1, 1, 1}, 
						{1, 0, 1, 0}, 
						{1, 0, 0, 1}, 
						{1, 1, 0, 0}};
int main() {
    // freopen("C.in", "r", stdin);
    // freopen("C-small-attempt0.in", "r", stdin);
    // freopen("C-small-attempt0.out", "w", stdout);

    int nt;
    scanf("%d", &nt);
    for (int t = 1; t <= nt; ++t) {
    	int l, x;
    	scanf("%d %d", &l, &x);
    	string str;
    	cin >> str;

    	string res = "";
    	while (x--)
    		res += str;
    	vector<bool> i(res.length(), false);

    	printf("Case #%d: ", t);
    	char val = 'h'; char boolVal = 1;
    	for (int it = 0; it < res.length(); ++it) {
    		val = mult[val-'h'][res[it]-'h'];
    		boolVal = boolVal^boolMult[val-'h'][res[it]-'h'];
    		i[it] = (val == 'i');
    		
    		if (it)
    			i[it] = i[it] or i[it-1];
    	}
    	if (not ((val == 'h') and (boolVal == 0))) {
    		puts("NO");
    		continue;
    	}

    	val = 'h'; boolVal = 1;
    	bool ans = false;
    	for (int it = res.length()-1; it >= 1; --it) {
    		val = mult[res[it]-'h'][val-'h'];
    		boolVal = boolVal^boolMult[res[it]-'h'][val-'h'];
    		if (val == 'k') {
    			if (i[it-1]) {
    				ans = true;
    				break;
    			}
    		}
    	}
    	if (ans)
    		puts("YES");
    	else
    		puts("NO");
    }
    return 0;
}