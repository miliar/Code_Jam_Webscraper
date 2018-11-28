#include <iostream>
#include <string>
#include <stdio.h>

using namespace std;

int main(){
	int t; 
	cin>>t;
	for(int j=1; j<=t; j++){
		int s,sol=0,sum=0;
		string a;
		cin>>s;
		cin>>a;
		for(int i=0; i<=s; i++){
			if(sum<i){
				sol = sol + (i - sum);
				sum = i ;
			}
			sum = sum + a[i] - 48;
		}
		printf("case #%d: %d\n",j,sol);
	}
}
