#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main()
{
	int tests;
	cin>>tests;
	int x=1;
	while(tests--){
		int max, sum=0, ct=0;
		string s;
		cin>>max;
		cin>>s;
		sum = (int)(s[0]-'0');
		for(int i=1;i<=max; i++){
			if(s[i] == '0')
				continue;
			if(sum<i){
				ct+=(i-sum);
				sum = i;
			}
			sum+=(int)(s[i]-'0');
		}
		cout << "case #" << x++ << ": "<<ct<<endl; 
	}
	return 0;
}
