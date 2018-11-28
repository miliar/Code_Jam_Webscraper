#include<stdio.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>

#include<iostream>
#include<vector>
#include<map>
#include<string>
#include<set>
#include<queue>
#include<stack>
#include<algorithm>
using namespace std;

#define fori(a,b) for(i = a; i <= b; i++)
#define forj(a,b) for(j = a; j <= b; j++)
#define fork(a,b) for(k = a; k <= b; k++)
#define scani(a) scanf("%d",&a);
#define scanlli(a) scanf("%lld", &a);
#define scanc(c) scanf("%c",&c);
#define scans(s) scanf("%s", s);
#define mp(a,b) make_pair(a, b)
#define ll(a) (long long int)(a)
#define vi vector<int>
#define vc vector<char>
#define vs vector<string>
#define println printf("\n");
#define sz(v) v.size()
#define len(s) s.length()
#define max(a,b) ((a > b) ? a : b)
#define min(a,b) ((a < b) ? a : b)

int main() {
    int i, n, t;
    scani(t)
    fori(1, t) {
        scani(n)
        int mp[10] = {0}, count = 0, multiplier = 1, temp;
        if (n == 0) {
            printf("Case #%d: INSOMNIA\n", i);
            continue;
        }
        while (count < 10) {
            temp = multiplier * n;
            while (temp > 0) {
                int last = temp % 10;
                temp = temp / 10;
                if (mp[last] == 0) {
                    mp[last] = 1;
                    count++;
                }
            }
            if (count == 10) {
                printf("Case #%d: %d\n", i, multiplier * n);
                break;
            }
            multiplier = multiplier + 1;
        }
    }
    return 0;
}