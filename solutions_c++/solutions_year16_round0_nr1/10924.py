#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
#include <vector>

#define mp make_pair
#define pb push_back
#define xx first
#define yy second

using namespace std;

int a[1003];
int main(){
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T, cas = 0, s, i, x, n, ans;

    cin >> T;
    while (T--) {
	cin >> n;
	if (n == 0){
	    printf("Case #%d: INSOMNIA\n", ++cas);
	    continue;
	}
	s = 0;
	memset(a, 0, sizeof a);
	for (i = n; ; i += n) {
	    x = i;
	    while (x) {
		if (a[x % 10] == 0){
		    a[x % 10] = 1;
		    s++;
		}
		x /= 10;
	    }
	    if (s == 10) break;
	}
	
	printf("Case #%d: %d\n", ++cas, i);
    }
}

