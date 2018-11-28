#include<iostream>
#include<string>
#include<algorithm>
#include<cmath>
#include<math.h>
using namespace std;int check(long long int ans){
	for(long long int i=2;i<=sqrt(ans);i++){
		if(ans%i==0){
			return 1;
		}
	}
	return 0;
}
int func(string str,long long int x){
	if(x==11){
		return 1;
	}
long long	int ans =0;
	for(long long int i=0;i<str.size();i++){
		if(str[str.size()-1-i]=='1'){
			ans+=pow(x,i);
		}
	}
	if(check(ans)==1&&func(str,x+1)==1){
		return 1;
	}
	else{
		return 0;
	}
}
int output(string str,long long int x){
long long	int ans=0;
	for(long long int i=0;i<str.size();i++){
		if(str[str.size()-1-i]=='1'){
			ans+=pow(x,i);
		}
	}
	for(long long int i=2;i<ans;i++){
		if(ans%i==0){
			return i;
		}
	}
}

int main (){
long long 	int k;
	cin>>k;
long long	int length ,x;
	cin>>length>>x;
	cout<<"Case #1:"<<endl;
	string str="";
	for(long long int i=0;i<length;i++){
		if(i==0||i==length-1){
			str=str+"1";
		}else{
			str=str+"0";
		}
	}
long long	int count=0;
	while(count<x){
		
		
		if(func(str,2)==1){
		count++;
		cout<<str<<" ";
			for(long long int i=2;i<=10;i++){
				cout<<output(str,i);
				if(i==10){
					cout<<endl;
				}else{
					cout<<" ";
				}
			}
		}
		
	
		
		//change string
		for( long long int i=length-2;i>0;i--){
			if(i==length-2){
				str[i]+=1;
			}
			if(str[i]=='2'){
				str[i-1]+=1;
				str[i]='0';
			}
		}
	}
}
