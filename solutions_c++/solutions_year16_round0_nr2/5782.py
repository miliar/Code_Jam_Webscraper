#include<iostream>
using namespace std;
void flip(string &s,int i)
{
	if(s[0]=='-') 
		for(int j=0;j<=i;j++)
			s[j]='+';
	else
		for(int j=0;j<=i;j++)
			s[j]='-';
}
int main()
{
	int t;
	cin >> t;
	for(int ii=1;ii<=t;ii++)
	{
		string s; 
		cin >> s;
		int i,flag=0;
			for(i=0;i<s.size();i++)
			{
				if(s[i]=='+' && s[0]=='-')
				{
					flip(s,i-1);
					flag++;
				}
				if(s[i]=='-' && s[0]=='+')
				{
					flip(s,i-1);
					flag++;
				}
			}
			if(s[0]=='-')
			{
				flip(s,i-1);
				flag++;	
			}
		cout << "Case #" << ii << ": " << flag << endl;  
	}
}
