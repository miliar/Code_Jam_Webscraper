#include <stdio.h>
#include <string.h>
#include <string>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
typedef long long ll;
const int maxn = 2005;
char str[maxn];
int ans[300];
int ap[300];

int main() {
#ifdef LOCAL
    freopen("/Users/yew1eb/ClionProjects/CppGo/in.txt", "r", stdin);
    freopen("/Users/yew1eb/ClionProjects/CppGo/out.txt", "w", stdout);
#endif
    int T;
    scanf("%d", &T);
    for(int cas=1; cas<=T; ++cas) {
        scanf("%s", str);
        int len = strlen(str);
        memset(ap, 0, sizeof ap );
        for(int i=0; i<len; ++i) {
            ap[ str[i] ]++;
        }
        memset(ans, 0, sizeof ans );
        //0
        int val = ap['Z'];
        if(val > 0) {
            ans[0] += val;ap['Z'] -= val;ap['E'] -= val;ap['R'] -= val;ap['O'] -= val;
        }
        //2
        val = ap['W'];
        if(val > 0) {
            ans[2] += val;ap['T'] -= val;ap['W'] -= val;ap['O'] -= val;
        }
        //4
        val = ap['U'];
        if(val > 0) {
            ans[4] += val; ap['F'] -= val; ap['O'] -= val; ap['U'] -= val; ap['R'] -= val;
        }
        //5
        val = ap['F'];
        if(val > 0) {
            ans[5] += val; ap['F'] -= val; ap['I'] -= val; ap['V'] -= val; ap['E'] -= val;
        }
        //7
        val = ap['V'];
        if(val > 0) {
            ans[7] += val; ap['S'] -= val; ap['E'] -= val; ap['V'] -= val; ap['E'] -= val;
            ap['N'] -= val;
        }
        //8
        val = ap['G'];
        if(val > 0) {
            ans[8] += val; ap['E'] -= val; ap['I'] -= val; ap['G'] -= val; ap['H'] -= val;
            ap['T'] -= val;
        }
        //1
        val = ap['O'];
        if(val > 0) {
            ans[1] += val; ap['O'] -= val; ap['N'] -= val; ap['E'] -= val;
        }
        //3
        val = ap['T'];
        if(val > 0) {
            ans[3] += val; ap['T'] -= val; ap['H'] -= val; ap['R'] -= val; ap['E'] -= val;
            ap['E'] -= val;
        }
        //6
        val = ap['S'];
        if(val > 0) {
            ans[6] += val; ap['S'] -= val; ap['I'] -= val; ap['X'] -= val;
        }
        //9
        val = ap['I'];
        if(val > 0) {
            ans[9] += val;
        }
        printf("Case #%d: ", cas);
        for(int i=0; i< 10; ++i) {
            while(ans[i]>0) {
                printf("%d", i);
                ans[i]--;
            }
        }
        printf("\n");
    }
    return 0;
}
//"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"



















