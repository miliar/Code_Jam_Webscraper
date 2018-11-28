#include <stdio.h>
#include <algorithm>
#include <string.h>
#include <queue>
#include <math.h>
#include <stdlib.h>
#include <vector>
using namespace std;
#define maxn 6005
#define pi acos(-1.0)
int x[maxn],y[maxn];
int n;
double z[maxn];
int main(){
    FILE *in=fopen("/Users/ZZ/Desktop/in.txt","r");
    FILE *out=fopen("/Users/ZZ/Desktop/out.txt","w");
    int T;
    int cas=1;
    fscanf(in,"%d",&T);
    while(T--){
        fscanf(in,"%d",&n);
        
        for(int i=0;i<n;i++) fscanf(in,"%d%d",&x[i],&y[i]);
        fprintf(out,"Case #%d:\n",cas++);
        if(n==1)
        {
            fprintf(out,"%d\n",0);
            continue;
        }
        for(int i=0;i<n;i++){
            for(int j=1;j<n;j++){
                z[j-1]=atan2((y[i]-y[(j+i)%n]+0.0),(x[i]-x[(j+i)%n]+0.0));
            }
            sort(z,z+n-1);
            for(int i=0;i<n-1;i++){
                z[n-1+i]=z[i]+2*pi;
            }
            int p=0,q=0;
            int ans=n;
            for(p=0;p<n-1;p++){
                while(q<2*(n-1)&&z[q]<=z[p]+1e-8+pi) q++;
                ans=min(ans,q-p);
                ans=min(ans,n-1-(q-p));
                if(ans<0) ans=0;
            }
            fprintf(out,"%d\n",ans);
        }
    }
    fclose(in);
    fclose(out);
}