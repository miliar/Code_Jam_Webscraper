#include<iostream>
#include<stdio.h>

using namespace std;

int f(){
	int max;
	cin>>max;
	char ch;
	string temp;
	cin>>temp;
	int cur;
	int sum=0;
	int needed=0;
	for(int i=0;i<=max;i++){
		ch=temp[i];
		if(sum<i){
			needed+=i-sum;
			sum+=i-sum;
		}
		cur=ch-'0';
		sum+=cur;


	}
	return needed;



}

int main(){
	long long t;
	scanf("%d",&t);
	long long d=0;

	
	while(t>0){
		t--;
		d++;
		
		cout<<"Case #"<<d<<": "<<f()<<endl;
	
	}
	
	return 0;
}
