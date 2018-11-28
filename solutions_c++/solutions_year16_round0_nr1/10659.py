/*
ID: txy
PROG: holstein
LANG: C++
*/
#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<cstring>
using namespace std;

int digit[11];
int get(long long i){
    while(i){
        digit[i%10]=1;
        i/=10;
    }
}
bool check(){
    for(int i=0;i<=9;i++)
        if(digit[i]==0)
            return false;
    return true;
}
int main(){
    FILE* fin=fopen("A-large.in","r");
    FILE *fout = fopen ("A-large.out", "w");
    int cas=1;
    int T;
    long long N;
    //scanf("%d",&N);
    fscanf(fin,"%d",&T);
    while(T--){
        memset(digit,0,sizeof(digit));
        fscanf(fin,"%lld",&N);
        //scanf("%lld",&N);
        long long temp=N;
        int total=0;
        while(total<10000000){
            get(N);
            if(check()){
                fprintf(fout,"Case #%d: %lld\n",cas++,N);
                //printf("%lld\n",N);
                N=-1;
                break;
            }
            N+=temp;
            total++;
        }
        if(N!=-1)
            fprintf(fout,"Case #%d: INSOMNIA\n",cas++);
        //fprintf(fout,"%d/%d\n",);
    }
    return 0;
}
