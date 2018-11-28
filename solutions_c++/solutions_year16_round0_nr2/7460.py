#include<iostream>
#include<conio.h>
#include<algorithm>
#include<fstream>
#include<cstring>
#include<string>
using namespace std;

int t,n;
int dp[105][2];
string s;

int main(void) {

	ifstream cin("input.in");
	ofstream cout("output.out");
	
	cin>>t;
	getline(cin,s);
	
	int c=0;
	
	for (; t; --t) {

		getline(cin,s);
		
		if (s[0]=='-'){
			 dp[0][0]=0;
			 dp[0][1]=1;
		}
		else {
			 dp[0][0]=1;
			 dp[0][1]=0;
		}
		
		for (int i=1; i<s.length(); ++i)
		 if (s[i]=='-') {
		 	dp[i][0]=min(dp[i-1][0],dp[i-1][1]+2);
		 	dp[i][1]=min(dp[i-1][0]+1,dp[i-1][1]+2);
		 }
		 else {
		 	dp[i][0]=min(dp[i-1][0]+2,dp[i-1][1]+1);
		 	dp[i][1]=min(dp[i-1][0]+1,dp[i-1][1]);
		 }
		
		++c;
		cout<<"Case #"<<c<<": "<<dp[s.length()-1][1]<<"\n";
	
	}
	
	return 0;
}
