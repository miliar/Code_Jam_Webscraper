#include<iostream>
using namespace std;

bool isnotfull(int *d){
    int k=1;
    for(int j=0; j<10; j++){
        if(d[j]==0){
            k=0;
            goto cont;
        }
    }
cont:
    if(k==0) return true; 
    else return false;
}
void split(int n, int* d){
    do{
        d[n%10]=1;
        n=n/10;
    }while(n!=0);
}


int main(){
int t;
cin>>t;
for(int loop=1; loop<=t; loop++){
//Solution here:
int n,s,k=0,ans=0;
cin>>n;
s=n;
int i,d[10]={0,0,0,0,0,0,0,0,0,0};
for(i=1; (isnotfull(d))&&(i<1000000); i++){
k=n*i;
split(k,d);
ans++;
}
if(s==0) cout<<"Case #"<<loop<<": INSOMNIA"<<endl;
else if(i>=1000000) cout<<"Case #"<<loop<<": INSOMNIA"<<endl;
else cout<<"Case #"<<loop<<": "<<k<<endl;
}
return 0;
}
