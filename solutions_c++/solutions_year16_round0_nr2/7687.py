#include <iostream>
using namespace std;
bool checkc(string s)
{
	for(int i=0;i<s.size();i++)
	{
		if(s[i]!='+')
			return false;
	}
	return true;
}
int main()
{
	int T;
	cin>>T;
	int ca;
	ca=0;
	int count = 0;
	int k;
	while(T>0)
	{
		ca++;
		string c;
		cin>>c;
		count = 0;
		while(!checkc(c))
		{	
			k=0;
			count++;
			for(int i=0;i<c.size();i++)
			{
				if(c[i+1]==c[i])
					k++;
				else break;
			}
			for(int i=0;i<=k;i++)
			{
				if(c[i]=='-')
					c[i]='+';
				else c[i] = '-';
			}
			
		}
		cout<<"Case #"<<ca<<": "<<count<<endl;
		T--;
	}
}