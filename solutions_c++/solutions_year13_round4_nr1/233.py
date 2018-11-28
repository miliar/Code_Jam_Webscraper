#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <string.h>
using namespace std;

int in[1010][3];
int pos[3000];
long long c[3000];
const long long INF=1000000000000000000LL;
const long long MOD=1000002013LL;
const long long M2=(1000002013+1)/2;
int main(){
    int tt,TT,n,m,i,j,k,r,x,y,z;
    long long sum1,sum,d;
    scanf("%d",&TT);
    for( tt=0; tt<TT; tt++ ){
        scanf("%d %d",&n,&m);
        r=0;
        sum1=0;
        for( i=0; i<m; i++ ){
            scanf("%d %d %d",&in[i][0],&in[i][1],&in[i][2]);
            pos[r++]=in[i][0];
            pos[r++]=in[i][1];
            d=in[i][1]-in[i][0];
            sum1=(sum1+((d*d)%MOD)*in[i][2])%MOD;
        }
        sort(pos,pos+r);
        r=unique(pos,pos+r)-pos;
        memset(c,0,sizeof(c));
        for( i=0; i<m; i++ ){
            x=lower_bound(pos,pos+r,in[i][0])-pos;
            y=lower_bound(pos,pos+r,in[i][1])-pos;
            for( j=x; j<y; j++ ){
                c[j]+=in[i][2];
            }
        }
        sum=0;
        while(1){
            long long md=INF;
            for( i=0; i<r; i++ ){
                if(c[i]>0 && c[i]<md){
                    md=c[i];
                }
            }
            if(md==INF) break;
            d=0;
            for( i=0; i<r; i++ ){
                if(c[i]){
                    d=(d+pos[i+1]-pos[i])%MOD;
                    c[i]-=md;
                }else{
                    if(d){
                        sum=(sum+((d*d)%MOD)*md)%MOD;
                        d=0;
                    }
                }
            }
        }
        printf("Case #%d: %I64d\n",tt+1,(((sum-sum1)%MOD+MOD)*M2)%MOD);
    }
    return 0;
}
