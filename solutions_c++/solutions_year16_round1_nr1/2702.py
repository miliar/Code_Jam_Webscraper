#define DEBUG

#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <stack>
#include <queue>
#include <deque>
#include <vector>
#include <map>
#include <set>
#include <utility>
#include <algorithm>
#include <cmath>
#include <iostream>
#include <fstream>
#include <sstream>
#include <climits>
#include <ctime>
#include <cassert>
using namespace std;
// template

// abbreviations
#define vi vector <int>
#define vl vector <long long>
#define vb vector <bool>
#define vs vector <string>
#define ii pair <int, int>
#define a first
#define b second
#define vii vector <ii>
#define mii map <int, int>
#define que queue
#define pque priority_queue
#define stk stack
#define lsone(value) (value)&(-value)
#define pub push_back
#define pob pop_back
#define puf push_front
#define pof pop_front
#define pu push
#define po pop
#define mp make_pair
#define loop(i, n) for(int i = 0; i < n; ++i)
#define loop1(i, n) for(int i = 1; i <= n; ++i)
#define reverse_iterate(a, b) for(__typeof(b.rend()) a = b.rbegin(); a != b.rend(); ++a)
#define iterate(a, b) for(__typeof(b.begin()) a = b.begin(); a != b.end(); ++a)
#define all(i) i.begin(), i.end()

typedef unsigned long long ull;
typedef long long ll;

const double PI = acos(-1);

#ifdef DEBUG
	#define debug(...) printf(__VA_ARGS__)
	#define GetTime() fprintf(stderr,"Running time: %.3lf second\n",((double)clock())/CLOCKS_PER_SEC)
#else
	#define debug(...) 
	#define GetTime() 
#endif

// end of template

int main() {
    // freopen("A-large.in", "r", stdin);
    // freopen("A-large.out", "w", stdout);
    
    int nt;
    scanf("%d%*c", &nt);
    loop1(t, nt) {
    	string str;
    	getline(cin, str);
    	deque<char> ans;
    	iterate(c_p, str) {
    		char &c = *c_p;
    		if (ans.size() == 0) {
    			ans.pub(c);
    		} else {
    			if (ans.front() > c) 
    				ans.pub(c);
    			else
    				ans.puf(c);
    		}
    	}
    	printf("Case #%d: ", t);
    	while (ans.size()) {
    		printf("%c", ans.front());
    		ans.pof();
    	}
    	printf("\n");
    }

    return 0;
}