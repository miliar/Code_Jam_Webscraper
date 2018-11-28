#include<iostream>
#include<algorithm>
#include<string>
#include<stack>
#include<fstream>
using namespace std;

int main()
{
long long int i,j,k,t,flag,c;

string s;

ofstream outfile;
outfile.open("E:\\codejam\\ggcodeout.txt");

char ch;

cin>>t;

k=1;

while(t--)
{
	
	c=0;
	flag=0;
	
	cin>>s;
	
	while(flag!=1)
	{	
		
		for(i=0;i<s.length();i++)
		{
			if(s[i]=='+')
			flag=1;
			else
			{
				flag=0;
				break;
				
			}
		}
		
		if(flag==0)
		{
			ch=s[0];
			i=0;
			
			if(ch=='+')
			{
				s[i]='-';
				i++;
				while(s[i]=='+')
				{
					s[i]='-';
					i++;
				}
				c++;
			}
			else if(ch=='-')
			{
				s[i]='+';
				i++;
				while(s[i]=='-')
				{
					s[i]='+';
					i++;
				}
				c++;
			}
		}
		else
		break;
				
	}
		
	outfile<<"Case #"<<k++<<":  "<<c<<endl;			
}

}
