#include<iostream>

using namespace std;

main() {
long long int n,a[100],t,b,i,dgt,cn[10],k,c;
cin>>t;
for(i=0;i<t;i++) {
cin>>a[i];
}
for(i=0;i<t;i++) {
c=10;k=1;
if(a[i]==0) cout<<"Case #"<<i+1<<": INSOMNIA\n";
else {
while(c!=0) {
b=k*a[i];
do {
dgt=b%10;
if(cn[dgt]!=i+1) {
c--;
cn[dgt]=i+1;
}
if(c==0) break;
b=b/10;
}while(b!=0);
k++;
}
if(c==0) cout<<"Case #"<<i+1<<": "<<(k-1)*a[i]<<"\n";
}
}
}
