#include<bits/stdc++.h>
using namespace std;
char x[111],y[111];
int main(){
    int T,n;
    FILE *in = fopen("input.txt","r");
    FILE *out = fopen("output.txt","w");
    fscanf(in,"%d",&T);
    for(int t=1;t<=T;t++){
        fscanf(in,"%s",x);
        int k = strlen(x);
        int ans=0;
        for(int now=k-1;now>=0;now--){
            if(x[now]=='+') continue;
            else{
                if(x[0]=='-'){
                    ans++;
                    for(int i=0;i<=now;i++) y[i]=x[now-i]=='+'?'-':'+';
                    for(int i=0;i<=now;i++) x[i]=y[i];
                }
                else{
                    int c=0;
                    while(x[c]=='+') c++;
                    for(int i=0;i<c;i++) y[now+i+1-c] = x[i];
                    for(int i=0;i<=now-c;i++) y[i]=x[now-i]=='+'?'-':'+';
                    ans+=2;
                    for(int i=0;i<=now;i++) x[i]=y[i];
                }
            }
        }
        fprintf(out,"Case #%d: %d\n",t,ans);
    }
}
