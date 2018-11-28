#include <iostream>
#include <algorithm>
using namespace std;
#include<stdio.h>

int main(){
    int t,n,p[10],i,j,count,lar,answer,tc;
    scanf("%d",&t);
    tc=1;
    while(t--){
        scanf("%d",&n);
        lar=0;
        for(i=0;i<n;i++){
            cin>>p[i];
            lar=max(lar,p[i]);
        }
        answer=100;
        for(i=1;i<=lar;i++){
            count=0;
            for(j=0;j<=n-1;j++){
                if(p[j]%i==0) count+=(p[j]/i)-1;
                else{count+=p[j]/i;}
            }
            answer=min(answer,count+i);
        }
       cout<<"Case #"<<tc<<": "<<answer<<endl;
       tc++;
    }
}