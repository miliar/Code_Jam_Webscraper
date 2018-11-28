#include<iostream>
using namespace std;

long long cc[10];
void ccc(long long n){
while(n>0){
cc[n%10]=1;
n=n/10;
}
}
int main(){
	long long n;
	cin>>n;
for(long long i=1;i<=n;i++){
long long t;
cin>>t;
if(t==0){
cout<<"Case #"<<i<<": INSOMNIA"<<endl;
continue;
}
for(long long i=0;i<=9;i++)cc[i]=0;
long long c=t;
while(1)
{
ccc(c);
bool f=true;
for(long long i=0;i<=9;i++){if(cc[i]==0)f=false;}
if(f)break;
c=c+t;
}
cout<<"Case #"<<i<<": ";
cout<<c<<endl;
}
return 0;
}

