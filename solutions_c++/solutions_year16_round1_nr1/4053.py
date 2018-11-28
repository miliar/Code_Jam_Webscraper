#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
 
#include <algorithm>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <deque>
 
#define FOR(i, s, e) for(int i=s; i<e; i++)
#define loop(i, n) for(int i=0; i<n; i++)
#define getint(n) scanf("%d", &n)
#define pb(a) push_back(a)
#define ll long long
#define SZ size()
#define read(filename) freopen(filename, "r", stdin)
#define write(filename) freopen(filename, "w", stdout)
#define mem(a, v) memset(a, v, sizeof(a))
#define all(v) v.begin(), v.end()
#define pi acos(-1.0)
#define INF 1<<29
#define mod(a) (a>0?a:-a)
#define pf printf
 
using namespace std;
 
int main()
{
    int T;
    getint(T);
    char s[10000];
    loop(i, T) {
    	scanf("%s", s);
    	deque<char> r;
    	int l = strlen(s);
    	char max = 'A';
    	loop(j, l) {
    		char b = s[j];
    		if (b - max >= 0) {
    			r.push_front(b);
    			max = b;
    		}
    		else {
    			r.push_back(b);
    		}
    	}

    	printf("Case #%d: ", i+1);
    	for(int j = 0; j < r.size(); j++) {
    		printf("%c", (char)r[j]);
    	}
    	printf("%c\n", '\0');
    }
    return 0;
}