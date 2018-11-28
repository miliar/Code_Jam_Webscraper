#include <stdio.h>
#include <algorithm>
#include <string.h>
#include <queue>
#include <math.h>
#include <stdlib.h>
#include <vector>
using namespace std;
#define maxn 1000005
int x[maxn];
int main(){
   
    FILE *in=fopen("/Users/ZZ/Desktop/in.txt","r");
    FILE *out=fopen("/Users/ZZ/Desktop/out.txt","w");
    int T;
    int cas=1;
    fscanf(in,"%d",&T);
    while(T--){
        int n;
        fscanf(in,"%d",&n);
        for(int i=0;i<n;i++) fscanf(in,"%d",&x[i]);
        int ans1=0,ans2=0;
        for(int i=1;i<n;i++)
            if(x[i]<x[i-1]) ans1+=x[i-1]-x[i];
        int v=0;
        for(int i=1;i<n;i++)
        {
            if(x[i]<x[i-1])
            {
                
                v=max(v,(x[i-1]-x[i]));
            }
        }
        
        for(int i=0;i<n-1;i++){
            if(v>x[i]) ans2+=x[i];
            else ans2+=v;
        }
        
        fprintf(out,"Case #%d: %d %d\n",cas++,ans1,ans2);
        
    }
    fclose(in);
    fclose(out);
}