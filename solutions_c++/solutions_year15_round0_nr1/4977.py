#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <string.h>
#include <math.h>

using namespace std;

#define MOD 1000000007
#define rec(i, n) for(int i = 0; i < n; i++)
#define max(a,b) ((a)>(b))?(a):(b)
#define u unsigned

int T;
int Smax;
string S;

int p, ans, l, i, j = 1;
int main() {
	scanf("%d", &T);
	while(T--) {
		scanf("%d", &Smax);
        cin>>S;
        l = S.length();

        p = 0;
        ans = 0;

        p += S[0] - '0';
        for (i = 1; i < l; i++) {
            if (p < i && S[i] != '0') {
                ans += (i - p);
                p = i;
            }
            p += S[i] - '0';
        }

        printf("Case #%d: %d\n", j++, ans);
	}
}