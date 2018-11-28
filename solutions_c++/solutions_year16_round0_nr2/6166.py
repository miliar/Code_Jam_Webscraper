#include <iostream>
#include<string.h>
using namespace std;

int main() {
int t;
cin>>t;
int m=0;
while(t>0)
{
	t--;
	m++;
	char s[150];
	int dp[150];
	cin>>s;
	int p=strlen(s);
if(s[0]=='-')
dp[0]=1;
else
dp[0]=0;
for(int i=1;i<p;i++)
{
	if(s[i-1]=='+'&&s[i]=='-')
	dp[i]=dp[i-1]+2;
	else
	dp[i]=dp[i-1];
}
	
cout<<"Case #"<<m<<": "<<dp[p-1]<<endl;	
	
}

	return 0;
}