#include<stdio.h>
#include<stdlib.h>
#include<vector>
#include<set>
#include<algorithm>
#include<string>
#include<iostream>
using namespace std;
double mark[1<<20];
double ctr[1<<20];
int n;
void solve(){
    string s;
    cin >> s;
    n=s.size();
    int mx=0;
    for(int i=s.size()-1;i>=0;i--){
        mx=mx<<1;
        if(s[i]=='X')mx++;
    }
    for(int i=0;i<(1<<20);i++){mark[i]=-1;ctr[i]=0;}
    mark[mx]=0;
    ctr[mx]=1;
    for(int i=0;i<(1<<n)-1;i++){

        if(mark[i]>-0.5){
            //printf("%d %lf %d\n",i,mark[i],ctr[i]);
            mark[i]/=ctr[i];
            for(int j=0;j<n;j++){
                int k=j;
                double get=n;
                while(i&(1<<k)){
                    k++;
                    k%=n;
                    get--;
                }
                if(mark[i|(1<<k)]<-0.5)mark[i|(1<<k)]=0;
                mark[i|(1<<k)]+= 1.0*ctr[i]*(mark[i]+get);
                ctr[i|(1<<k)]+=ctr[i];
            }
        }
    }
    //printf("%.10lf %d\n",mark[(1<<n)-1],ctr[(1<<n)-1]);
    printf("%.10lf\n",mark[(1<<n)-1]/ctr[(1<<n)-1]);
}
int main(){
    freopen("D-small-attempt1.in","r",stdin);
    freopen("D-small.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        printf("Case #%d: ",i);
        solve();
    }
}
