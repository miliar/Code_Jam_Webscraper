#pragma comment(linker, "/STACK:16777216")
#include<stdio.h>
#include<algorithm>
#include<string>
#include<vector>
#include<string.h>
using namespace std;
#define maxn 1005
int n;
int x[maxn];
bool f(int z){
    for(int i=1;i<=z;i++)
    {
        int ans=i;
        for(int j=0;j<n;j++){
            int u=x[j]/i; if(x[j]%i==0&&x[j]!=0) u--;
            ans+=u;
        }
        if(ans<=z) return 1;
    }
    return 0;
}

int main(){
    int T;
    int cas=1;
    FILE *in = fopen("/Users/ZZ/Downloads/B-large.in", "r");
    FILE *out = fopen("/Users/ZZ/Desktop/out.txt", "w");
    fscanf(in,"%d",&T);
    while(T--){
        fscanf(in,"%d",&n);
        for(int i=0;i<n;i++) fscanf(in,"%d",&x[i]);
        int st=0;
        int nd=1002;
        while(st<=nd){
            int mid=(st+nd)/2;
            if(f(mid)) nd=mid-1;
            else st=mid+1;
        }
        
        fprintf(out,"Case #%d: %d\n",cas++,nd+1);
        
    }
}