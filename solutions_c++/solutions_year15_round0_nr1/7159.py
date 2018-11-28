#include<iostream> 
#include<vector>
#include<stdio.h> 
#include<numeric>
#include<string>
using namespace std; 
int main() 
{ 
	freopen ("A-large.in","r",stdin);
	freopen ("output.txt","w",stdout);
	
	int x,n;
	string s;
	cin>>n;
	for(int j=0;j<n;j++)
	{
	cin>>x>>s;
	int count=0,result=0;
	for(int i=0;i<=x;i++)
	{
		if(count >= i  )
		{
			count+= s[i]-'0';
			
		}
		else if(s[i]-'0' > 0 )
		{
			//count+= s[i]-'0';
			result+=i-count;
		   count+= i- count;
		   count+= s[i]-'0';
		}
	}
	
	cout<<"Case #"<<j+1<<":"<<" "<<result<<endl;
	}
} 