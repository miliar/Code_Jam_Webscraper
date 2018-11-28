#include<stdio.h>
#include<iostream>
#include <algorithm>
using namespace std;

int main(){

	//freopen("B.in","r",stdin);
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);

    int T,D,P[1001],ans=0,Z;

    scanf("%d",&T);
    for(int i=1; i<=T; i++)
    {
        scanf("%d",&D);
        for(int j=0; j<D; j++){
            scanf("%d",&P[j]);
        }
        ans = 0;
        for(int j=0;j<D;j++)
        {
            if(P[j]>ans)
                ans=P[j];
        }
        //printf("for %d max is %d\n",i,ans);

        Z = 2;

        while(Z<ans){
            int sum = 0, value = 0;
            for(int j=0; j<D; j++){
                sum += (P[j]-1)/Z;
             //   printf("%d\n",sum);
            }
            value = sum + Z;
            ans = min(ans, value);
            Z++;
        }
        printf("Case #%d: %d\n",i,ans);
    }
    return 0;
}
