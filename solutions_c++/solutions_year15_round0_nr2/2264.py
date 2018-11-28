/*************************************************************************
    > File Name: gcja.cpp
    > Author: Lawrence_
    > Mail: 402374437@qq.com
    > Created Time: 2015/4/11 21:29:59
 ************************************************************************/
#include <cstdio>
#include <iostream>
#include <stack>
#include <queue>
#include <algorithm>
#include <cstring>
#include <string>
#include <cmath>
#include <deque>
#include <list>
#include <map>
#include <vector>
#include <cstdlib>
#include <set>
#include <cctype>
#define ll long long
#define lson l,m,rt << 1
#define rson m+1,r,rt << 1 | 1
#define pi acos(-1)
#define INF 0x7f7f7f7f
#define Clear(name,init) memset(name,init,sizeof(name))
#define eps 1e-8
using namespace std;
int p[1005];
int main(){
    freopen("C:\\Users\\joho\\Desktop\\B-large.in","r+",stdin);
    freopen("C:\\Users\\joho\\Desktop\\A-small-attempt1.out","w+",stdout);
    int t;
    while(~scanf("%d",&t)){
        for(int cas = 1;cas <= t; cas++){
            int n,sum = 0;
            scanf("%d",&n);
            int maxx = -1;
            for(int i = 0;i < n; i++){
                scanf("%d",&p[i]);
                sum += p[i];
                if(p[i] > maxx)
                    maxx = p[i];
            }
            int ans = maxx;
            int temp,tp;
            for(int i = 1;i <= maxx; i++){
                for(int j = 1;j <= i; j++){
                    tp = 0;
                    for(int k = 0;k < n; k++){
                        if(p[k] <= j)
                            continue;
                        if(p[k] % j == 0)
                            temp = p[k] / j - 1;
                        else
                            temp = p[k] / j;
                        tp += temp;
                    }
                    if(tp + j < ans)
                        ans = tp + j;
                }
            }
            printf("Case #%d: %d\n", cas, ans);
        }
    }
    return 0;
}
