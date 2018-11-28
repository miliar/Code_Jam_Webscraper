#include <iostream>
#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <string.h>
#include <stdlib.h>
using namespace std;

int T,iCase;
long long n;
int ma[10];

int main()
{
    int i,j;
    //FILE *fp;
    //fp=fopen("H:\\out3.txt","w");
    //freopen("H:A-large.in","r",stdin);
     scanf("%d",&T);
    for(iCase=1;iCase<=T;iCase++){
        scanf("%lld",&n);
        if(n==0){
            printf("Case #%d: INSOMNIA\n",iCase);
            continue;
        }
        memset(ma,0,sizeof(ma));
        for(i=1;i<=0x3f3f3f3f;i++){
            long long tmp=n*i;
            while(tmp){
                int a=tmp%10;
                ma[a]=1;
                tmp/=10;
            }
            if(ma[0]==1&&ma[1]==1&&ma[2]==1&&ma[3]==1&&ma[4]==1&&ma[5]==1&&ma[6]==1&&ma[7]==1&&ma[8]==1&&ma[9]==1){
                printf("Case #%d: %lld\n",iCase,n*i);
                break;
            }
        }
    }
    return 0;
}




























