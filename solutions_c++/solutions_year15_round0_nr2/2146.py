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


#define LL long long

const long long  mod =1000000009;  //这个必须是质数
int q[2222];
int main()
{
    int T;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&T);
    int t=T;
    while (T--){
        int n;
        scanf("%d",&n);
        for (int j=0;j<n;j++)scanf("%d",&q[j]);
        sort(q,q+n,greater<int>());
        int ans=2100000000;
        for (int j=1;j<=1000;j++){
            int ha=0;
            int last=0;
            for (int k=0;k<n;k++){
                int now=q[k];
                int g=(now+j-1)/j-1;
                ha+=g;
                if (g>0) last=j;
                else last=max(last,now);
            }
            ans=min(ans,ha+last);
        }
        printf("Case #%d: %d\n",t-T,ans);
    }
    return 0;
}

