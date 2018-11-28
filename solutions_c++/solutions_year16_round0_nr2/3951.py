#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <string>
#include <cstdlib>
#include <queue>
#include <stack>
#include <cmath>
#include <vector>
#include <map>

#define ll long long
#define ull unsigned long long
#define lson l, m, rt<<1
#define rson m+1, r, rt<<1|1

using namespace std;

const int inf = 0x3f3f3f3f;
const int M = 102;

char a[M], ch[M];


int main(){

   // freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for(int cas = 1; cas <= t; cas++){
        scanf("%s", a);
        int cnt = 0, len = strlen(a);
        ch[cnt++] = a[0];
        for(int j = 1; j < len; j++){
            if(a[j] != a[j-1]){
                ch[cnt++] = a[j];
            }
        }
        int ans;
        if(ch[0] == '+')
            ans = 0;
        else
            ans = 1;
        for(int i = 1; i < cnt; i++){
            if(ch[i] == '-')
                ans += 2;
        }
        printf("Case #%d: %d\n", cas, ans);
    }


    return 0;
}









