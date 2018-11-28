#include<stdio.h>
#include<math.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<set>
#include<iostream>
#include<map>
#include<queue>
#include<bitset>
#include<string>
#include<stdlib.h>
#include<sstream>
#define pb push_back
using namespace std;
int cs;
long long win(long long P,int N){
    long long now=0;
    int i;
    for(i=0;i<N;i++){
        if((P>>(N-i-1))&1){
            return now*2;
        }
        else{
            now=now*2+1;
        }
    }
    return (1ll<<N)-1;
}
long long win2(long long P,int N){
    long long now=0,res=(1<<N);
    int i;
    for(i=0;i<N;i++){
        if((P>>(N-i-1))&1){
            now=2*now+1;
        }
        else{
            res=min(res,2*now+1);
        }
    }
    return (1ll<<N)-min(now,res)-1;
}
int main(){
    int T,i,j,k,N;
    long long P,an1,an2=0;
    scanf("%d",&T);
    while(T--){
        cin>>N>>P;
        P=(1<<N)-P;
        an1=win(P,N);
        an2=win2(P,N);
        printf("Case #%d: %lld %lld\n",++cs,an1,an2);
    }
    return 0;
}

