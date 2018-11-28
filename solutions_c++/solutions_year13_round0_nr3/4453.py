#include <iostream>
#include <stdio.h>
#include <cstring>
#include <map>
#include <stdlib.h>
#include <string.h>

char s[15];
using namespace std;
map<long long,int> mp;
long long num[10000],hui[10000];
bool Hui(long long t){
    itoa(t,s,10);
    int len=strlen(s);
    for(int i=0;i<=((len-1)>>1);i++)
        if(s[i]!=s[len-i-1])return 0;
    return 1;
}
int main()
{

    //freopen("C-small-attempt0.in","r",stdin);
    //freopen("a.txt","r",stdin);
   //freopen("b.txt","w",stdout);
   hui[0]=1;
   num[0]=1;
   long long en=1,h=1;
   bool flg;
   for(long long i=2;i<=10000000;++i){
        flg=0;
        for(int j=0;j<h&&hui[j]*hui[j]<=i;++j)
        if(hui[j]*hui[j]==i){
            flg=1;
            break;
        }
        if(Hui(i)){
            hui[h++]=i;
            if(flg)num[en++]=i;
        }
   }
    int T,cc=1;
     long long n,m,cnt;
    scanf("%d",&T);
    while(T--){
       scanf("%I64d%I64d",&n,&m);
       printf("Case #%d: ",cc++);
       cnt=0;
    for(long long i=0;i<en;++i){
        if(num[i]>=n&&num[i]<=m)cnt++;
    }
    printf("%I64d\n",cnt);

    }
   return 0;
}
