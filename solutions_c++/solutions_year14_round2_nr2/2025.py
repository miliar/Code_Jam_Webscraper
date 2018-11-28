#include <iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<string>
#include<fstream>
#define LL long long
using namespace std;
int  main()
{
    LL cnt,ics=0,i,j,t,A,B,K;
   //freopen("B-small-attempt1.in","r",stdin);
   // freopen("B-small-attempt1.out","w",stdout);
    scanf("%I64d",&t);
    while(t--){
        scanf("%I64d%I64d%I64d",&A,&B,&K);
        printf("Case #%I64d: ",++ics);
        cnt=0;
        for(i=0;i<A;i++){
            for(j=0;j<B;j++){
                if((i&j)<K)
                cnt++;
            }
        }
        printf("%I64d\n",cnt);
    }
    return 0;
}
