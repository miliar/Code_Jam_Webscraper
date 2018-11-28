
#include <iostream>
#include <string.h>
#include <math.h>
#include <queue>
#include <algorithm>
#include <stdlib.h>
#include <map>
#include <set>
#include <stdio.h>
#include <string>
#include <time.h>
#include <vector>
using namespace std;
#define LL long long
#define pi acos(-1.0)
#pragma comment(linker, "/STACK:1024000000")
const int mod=1e9+7;
const int INF=0x3f3f3f3f;
const double eqs=1e-9;
const int MAXN=200000+10;
char s[2000];
int main()
{
    int t, len, k, i, j, icase=0;
    freopen("A.in", "r", stdin);
    freopen("A.out","w",stdout);
    scanf("%d",&t);
    while(t--){
        scanf("%s %d",s, &k);
        len=strlen(s);
        int cnt = 0;
        for(i=0;i<len-k+1;i++){
            if (s[i] == '+'){
                continue ;
            }
            for(j=0;j<k;j++){
                int tmp=i+j;
                s[tmp] = s[tmp]=='+'?'-':'+';
            }
            cnt++;
        }
        int flag=0;
        for(i=len-k+1;i<len;i++){
            if(s[i]=='-')
                flag=1;
        }
        printf("Case #%d: ",++icase);
        if(flag){
            puts("IMPOSSIBLE");
        }
        else{
            printf("%d\n",cnt);
        }
    }
    return 0;
}
