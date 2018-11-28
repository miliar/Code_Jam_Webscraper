/*
 * Author:  xtestw
 * Created Time:  2015/4/11 20:54:10
 * File Name: B.cpp
 */
#include <iostream>
#include <cstdio>
#include <queue>
using namespace std;
const int maxint = -1u>>1;
int a[1010];
int main() {
   freopen("B-large.in","r",stdin);
  freopen("B-large.out","w",stdout);
   int tt;
   cin>>tt;
   for(int ca=1;ca<=tt;ca++){
        int n;
        scanf("%d",&n);
        int ma=0;
        for(int i=0;i<n;i++)
        {
            scanf("%d",&a[i]);
            if(ma<a[i]) ma=a[i];
        }
        int ans=0x3f3f3f3f;
        for(int i=1;i<=ma;i++)
        {
            int tmp=0;
            for(int j=0;j<n;j++)
            {
                if(a[j]==0 && i==1 ) continue;
                tmp=tmp+(a[j]-1)/i ;
            }
            if (ans>tmp+i) ans=tmp+i;
        }
        printf("Case #%d: %d\n",ca,ans);
   }
   return 0;
}

