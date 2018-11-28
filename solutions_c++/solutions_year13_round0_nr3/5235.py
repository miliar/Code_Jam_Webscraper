#include<iostream>
#include<stdio.h>
#include<string>
#include<math.h>
using namespace std;
#define limit 4
int rev(int a){
	int res=0;
	while(a>0){
		res=res*10+(a%10);
		a/=10;
	}
	return res;
}
bool fair(int a){
	if(a==rev(a))return true;
	return false;
}
bool squar(int a){
	int k=sqrt(a);
	if(k*k==a)return true;
	return false;
}
int main(){
	int t,a,b,result,temp,ctr=0;
	cin>>t;
	while(ctr++<t){
		result=0;
		cin>>a>>b;
		for(int i=a;i<=b;i++){
			if(squar(i)&&fair(i)){
				temp=sqrt(i);
				if(fair(temp)){result++;}
			}
		}
		cout<<"Case #"<<ctr<<": "<<result<<endl;
	}
	return 0;
}
