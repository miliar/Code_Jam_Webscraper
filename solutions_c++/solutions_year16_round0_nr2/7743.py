#include<iostream>
#include<cstdio>
#include<vector>
using namespace std;

int main()
{

	
	int n;
	cin>>n;
	for(int i=1;i<=n;i++)
	{
		
		string s;
		cin>>s;
		int steps=0;
		while(true)
		{
	
			
			if(count(s.begin(),s.end(),'-')==0)
				break;
			int j;		
			if(s[0]=='+')
			{
				for(j=0;j<s.size() && s[j]=='+';j++);
				reverse(s.begin(),s.begin()+j);
			for(int k=0;k<j;k++)
			{
				s[k]=(s[k]=='-'?'+':'-');
			}
				steps++;	
			}
			else
			{
				for(j=0;j<s.size() && s[j]=='-';j++);
				reverse(s.begin(),s.begin()+j);
				for(int k=0;k<j;k++)
			{
				s[k]=(s[k]=='-'?'+':'-');
			}
			steps++;
			}
				
		}
			
		cout<<"Case #"<<i<<": "<<steps<<endl;
	}


}

