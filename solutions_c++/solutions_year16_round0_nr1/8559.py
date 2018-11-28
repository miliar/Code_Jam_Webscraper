#include<iostream>
using namespace std;
int main(){
int test,kk=1;
cin>>test;
while(test--){
long long int n;
int i;
cin>>n;
char numbers[10],convert[100];
for(i=0;i<10;i++){
numbers[i]=i+48;
}
int flag=0;
int p,k;
for(i=1;i<1000000;i++){
p=i*n;
while(p!=0){
k=p%10;
p=p/10;
k=k+48;
for(int j=0;j<10;j++){
if(k==numbers[j]){
numbers[j]='#';
break;
}
}
}
flag=0;
for(int j=0;j<10;j++){
if(numbers[j]!='#'){
flag=1;
break;
}
}
if(flag==0) break;
}
if(flag==0) cout<<"Case #"<<kk<<": "<<i*n<<'\n';
if(flag==1) cout<<"Case #"<<kk<<": "<<"INSOMNIA\n";
kk++;
}
return 0;
}


