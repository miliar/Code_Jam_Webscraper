#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<stdlib.h>
#include<time.h>
#define N 4
using namespace std;
int t,dap,t_cnt;
FILE *in,*out;
void input();
void solve(int s,int e);
int f(int x);
void output();

int main(){
    in=fopen("input.txt","r");
    out=fopen("output.txt","w");
    input();
}
void input(){
    int i,j;
    int s,e;
    fscanf(in,"%d",&t);
    for(t_cnt=1;t_cnt<=t;t_cnt++){
        dap=0;
        fscanf(in,"%d %d",&s,&e);
        solve(s,e);
        output();
    }
}
void solve(int s,int e){
    int i;
    int x;

    for(i=1;i*i<=e;i++){
        x=i*i;
        if(x<s) continue;

        if(f(i)==1 && f(x)==1) dap++;
    }

}
int f(int x){
    int i,j,a[20]={0,};
    int n=0;

    if(x%10==0) return 0;

    while(x){
        a[n++]=x%10;
        x/=10;
    }

    for(i=0,j=n-1;i<j;i++,j--){
        if(a[i]!=a[j]) return 0;
    }


    return 1;
}
void output(){
    fprintf(out,"Case #%d: %d\n",t_cnt,dap);
}
