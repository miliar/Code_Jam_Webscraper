#include <iostream>
#include<stdio.h>
#define loop(i,n) for(int i=0;i<n;i++)
using namespace std;
inline int get(int a[],int n,int q){
    int x=n*q,temp=0;
    while(x>0){
        if(a[x%10]==0)
        a[x%10]=1;
        x=x/10;
    }
    loop(i,10)if(a[i]==0)temp=1;
    if(temp==0) return n*q;
    else get(a,n,q+1);
}
int main(){
int t,i=1;
cin>>t;
while(t--){
int n;
scanf("%d",&n);
int a[10]={0};
if(n==0)printf("Case #%d: INSOMNIA\n",i);
else printf("Case #%d: %d\n",i,get(a,n,1));
i++;
}
return 0;
}
