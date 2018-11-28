#include<iostream>
#include<cstring>
#include<stdio.h>
using namespace std;

int main() {
	long int t,s,count,res;
	char str[1001];


	cin>>t;

	for(int j=1;j<=t;j++){

	count = 0;
	res=0;
	cin>>s;
	cin>>str;
	

	for(int i =0; i<s+1 ;i++){
		if(res<i && str[i] !='0'){
			count += i-res;
			res=i;
		}
		res = res+ (str[i]-'0'); //6 0100001
	}
	printf("Case #%d: %ld",j,count);
	cout<<endl;
	}

	return 0;
}

	
