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

//为自己加油O(∩_∩)O~

const long long  mod =1000000009;  //这个必须是质数
int q[2000];
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    int t=T;
    while (T--){
        int n;
        scanf("%d",&n);
        for (int j=0;j<n;j++){
            scanf("%d",&q[j]);
        }
        int ans1=0;
        for (int j=0;j<n-1;j++){
            if (q[j+1]<q[j]) ans1+=-q[j+1]+q[j];
        }
        int ans2=0;
        int r=0;
        for (int j=0;j<n-1;j++){
            if (-q[j+1]+q[j]>r) r=-q[j+1]+q[j];
        }
        int now=0;
        for (int j=0;j<n-1;j++){
            if (now==0) now+=q[j];else now=q[j];
            if (now<r) {
                ans2+=now;
                now=0;
            }else {
                ans2+=r;
                now-=r;
            }
        }
        printf("Case #%d: %d %d\n",t-T,ans1,ans2);
    }
    return 0;
}
