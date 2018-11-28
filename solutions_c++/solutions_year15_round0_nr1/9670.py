#include <iostream>
using namespace std;
int main() {
	int t,j;
cin>>t;
for(j=1;j<=t;j++){
int s,i,k,l,x,y;
char a[1010];
cin>>s;
long long sum=0,flag=0;
for(i=0;i<=s;i++){
cin>>a[i];
x=a[i]-48;
if(i>sum){
flag=flag+(i-sum);
sum=i;
}
sum=sum+x;
}
cout<<"Case #"<<j<<":"<<" "<<flag<<endl;
}
	return 0;
}