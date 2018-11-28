#include <iostream>
#include<string>
#include<stack>
using namespace std;
int main()
{
int T,k;
cin>>T;
for(k=0;k<T;k++)
{
string str;
stack<char> bucket;
cin>>str;
int j;
while ( ! bucket.empty() )	{   bucket.pop();}
int count=0;
for(int i=str.size()-1;i>=0;i--)
{
//cout<<i;
	if(str[i]=='+') continue;
	else
	{
		if(str[0]=='+'){count++;int t=0;while(str[t]=='+')str[t++]='-';}
		j=i;
		count++;
		while(j >= 0) 
		{
		if(str[j]=='-')	bucket.push('+');
		else 		bucket.push('-');
		j--;
		}
		
		j=i;	
		while(j >= 0) 
		{
		str[j]=bucket.top();bucket.pop();
		//str.insert(j,1,bucket.top());bucket.pop();
		j--;
		}	
		
	}
	//cout<<str<<endl;
}
cout<<"Case #"<<k+1<<": "<<count<<endl;
}
return 0;
}


