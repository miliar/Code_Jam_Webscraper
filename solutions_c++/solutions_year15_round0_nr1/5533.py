#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

int main()
{
	int T,Smax,casenumber=0;
	string num;
	scanf("%d",&T);
	while(T--){
		casenumber++;
		cin>>Smax>>num;
		int sum=0,required=0;
		for(int i=0;i<num.length();i++){
			if(sum<i){
				required = required+(i-sum);
				sum = sum+(i-sum);
			}
			sum=sum+(num[i]-'0');
		}
		cout<<"Case #"<<casenumber<<": "<<required<<endl;
	}
	return 0;
}