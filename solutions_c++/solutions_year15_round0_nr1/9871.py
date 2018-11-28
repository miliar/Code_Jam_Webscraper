/*
 * p1.cpp
 *
 *  Created on: Apr 11, 2015
 *      Author: rss
 */
#include <iostream>
#include <string>
using namespace std;
int T, S, s[1001], sum, k;
string str;
int main() {
	cin>>T;
	for (int t=1; t<=T; t++) {
		cin>>S;
		cin>>str;
		sum=k=0;
		sum=str[0]-'0';
		for (int i=1; i<=S; i++) {
			s[i]=str[i]-'0';
			if (sum>=i)
				sum+=s[i];
			else {
				k+=i-sum;
				sum=i+s[i];
			}
		}
		cout<<"Case #"<<t<<": "<<k<<endl;
	}
	return 0;
}
