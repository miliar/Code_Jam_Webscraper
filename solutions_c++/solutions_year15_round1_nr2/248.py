#include <stdio.h>
#include <algorithm>
#include <string.h>
#include <queue>
#include <math.h>
#include <stdlib.h>
#include <vector>
using namespace std;
#define maxn 10005
int m[maxn];
int b,n;
long long f(long long t){
    long long num=0;
    for(int i=0;i<b;i++){
        num+=(t/m[i]+1);
        if(num>n) return num;
    }
    return num;
}

int main(){
   
    FILE *in=fopen("/Users/ZZ/Desktop/in.txt","r");
    FILE *out=fopen("/Users/ZZ/Desktop/out.txt","w");
    int T;
    int cas=1;
    fscanf(in,"%d",&T);
    while(T--){
        fscanf(in,"%d%d",&b,&n);
        for(int i=0;i<b;i++) fscanf(in,"%d",&m[i]);
        long long st=0;
        long long nd=(long long)n*100000;
        while(st<=nd){
            long long mid=(st+nd)/2;
            long num=f(mid);
            if(num>=n) nd=mid-1;
            else st=mid+1;
        }
        int num=0;
        for(int i=0;i<b;i++){
            if(st%m[i]==0) num+=st/m[i];
            else num+=st/m[i]+1;
        }
        
        int ans=0;
        for(int i=0;i<b;i++){
            if(st%m[i]==0){
                num++;
                if(num==n){
                    ans=i+1;
                    break;
                }
            }
        }
        
        fprintf(out,"Case #%d: %d\n",cas++,ans);
    }
    fclose(in);
    fclose(out);
}