#include <iostream>
#include <string>
#include <stdio.h>

using namespace std;

int main(){
	int t,smax;
	string s;
	unsigned long long int sum,extra;
	cin>>t;
	for(int k=1 ; k<=t ; k++){
		sum=0;
		extra=0;
		scanf("%i",&smax);
		cin>>s;
		for(int i=0 ; i<s.size() ; i++){
			if(sum < i){
				extra+=i-sum;
				sum=i;
			}
			sum+=(int)s[i]-48;
		}
		printf("Case #%i: %lli\n",k,extra);
	}
}
