#include <bits/stdc++.h>
#include<cstring>
#define ll long long
using namespace std;
int dp[1000003];
 

 string to_string1(int i)
 {
 	string temp="";
 	while(i>0)
 	{
 		temp+=((i%10)+48);
 		i=i/10;
	 }
	 	return temp;
 }
 
 int stoi1(string s)
 {
 	int i;
 	int sum=0;
 	for(int i=0;i<s.length();i++)
 	{
 		sum+=((s[i]-48)*(int)(pow(10,s.length()-i-1)));
	 }
	 return sum;
 }
int main() 
{
	int t;
	cin>>t;
	string s="2300";
	//cout<<to_string1(2300)<<" "<<stoi1(s)<<endl;
	memset(dp, 0x3f, sizeof dp);
	dp[1]=1;
	for(int i = 1; i < 1000000; ++i)
	{
		string tmp = to_string1(i);
	//	reverse(tmp.begin(), tmp.end());
		int reverse = stoi1(tmp);
		dp[i+1] = min(dp[i+1], dp[i] + 1);
		dp[reverse] =min(dp[reverse], dp[i] + 1);
	}
	for(int i=1;i<=t;i++)
	{
		int n;
		cin>>n;
		cout<<"Case #"<<i<<": "<<dp[n]<<"\n";
	}
	return 0;
}
