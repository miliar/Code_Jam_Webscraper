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

int arr[10];
void copy_to_temp(int temp[]) {
    int i;
    fori(0, 9) {
        temp[i] = arr[i];
    }
}
void copy_from_temp(int temp[]) {
    int i;
    fori(0, 9) {
        arr[i] = temp[i];
    }
}
int recurse(int sofar) {
    int m, mc, a, b, i;
    for (i = 9; i >= 1; i--) {
        if (arr[i] > 0) {
            m = i;
            mc = arr[i];
            break;
        }
    }
    a = sofar + m;
    if (m == 1) {
        return sofar + 1;
    }
    int temp[10];
    if (m == 9) {
        copy_to_temp(temp);
    }
    arr[m] = 0;
    arr[m/2] += mc;
    arr[(m+1)/2] += mc;
    b = recurse(sofar + mc);
    if (m == 9) {
        copy_from_temp(temp);
        arr[9] = 0;
        arr[3] += mc * 3;
        int c = recurse(sofar + mc * 2);
        b = min(b, c);
    }
    return min(a, b);
}
int main() {
    int t, te, i, d, num;
    scani(t)
    for (te = 1; te <= t; te++) {
        scani(d)
        fori(0, 9) {
            arr[i] = 0;
        }
        fori(0, d-1) {
            scani(num)
            arr[num]++;
        }
        printf("Case #%d: %d\n", te, recurse(0));
    }
    return 0;
}