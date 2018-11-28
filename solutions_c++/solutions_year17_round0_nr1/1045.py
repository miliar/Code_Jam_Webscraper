#include <iostream>
#include <iomanip>
#include <fstream>
#include <stdlib.h>
#include <time.h>
#include<cstring>
#include<cstdio>
#include<vector>
#include<string>
#include<algorithm>
#include <limits.h>
#include<cmath>
#include<map>
#include<queue>
#include<set>
using namespace std;

#define N 100005
#define M 100005
#define LL long long

//为自己加油O(∩_∩)O~

const long long  mod =1000000007;
char z[N];
char f(char x)
{
    return x=='-'?'+':'-';
}
void gao(int len,int ans)
{
    for (int j=0;j<len;j++) if (z[j]=='-') {
        printf("IMPOSSIBLE\n");
        return ;
    }
    printf("%d\n",ans);
}
int main()
{
    freopen("1.in","r",stdin);
    freopen("1.txt","w",stdout);
    int T;
    scanf("%d",&T);
    int t=T;
    while (T--){

        int K;
        scanf("%s %d",z,&K);
        printf("Case #%d: ",t-T);
        int len=strlen(z);
        int ans=0;
        for (int j=0;j+K-1<len;j++){
            if (z[j]=='-') {
                for (int k=j;k-j<K;k++) z[k]=f(z[k]);
                ans++;
            }
        }
        gao(len,ans);
    }
    return 0;
}








