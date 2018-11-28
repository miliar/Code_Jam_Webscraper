#include <bits/stdc++.h>
using namespace std;

int main() 
{
int t,k=1;
cin>> t;
while(t--)
{
int n; 
cin >> n;
string a;
cin >> a;
int s[n];
for(int i=0;i<a.length();i++) 
s[i]=a[i]-'0';
long long int sum=0,res=0;
n++;
for(int i=0;i<n;i++)
{
	if(s[i])
	{
	if(i-sum <= 0)
	{
		sum+=s[i];
	}
	else
	{
		res+=(i-sum);
		sum+=s[i]+res;
	}
	}
}
cout<<"Case #"<<k++<<": "<<res<<endl;
}
	return 0;
}