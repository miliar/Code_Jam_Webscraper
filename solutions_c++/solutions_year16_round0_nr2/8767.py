#include<iostream>
#include<string>
using namespace std;
string replacen(string str1,int n)
{
	for(int i=0;i<n;i++)
	{
		if(str1[i]=='+')
		{
			str1[i] = '-';
		}
		else
		{
			str1[i] = '+';
		}
	}
	return str1;
}

int main()
{
	int t;
	cin>>t;
	for(int k=0;k<t;k++)
	{
		string str1,str2;
		int count = 0;
		cin>>str1;
		int a = str1.length();
		for(int i=0;i<a;i++)
		{
			str2 = str2 + '+';
		}
		while(str1!=str2)
		{
			int i=0;
			while(str1[i]!='-')
			{
				i++;
			}
			if(i!=0)
			{
				str1 = replacen(str1,i);
				count++;
			}	
			int j=0;
			while(str1[j]!='+' && j!=a)
			{
				j++;
			}
			if(j!=0)
			{
				str1 = replacen(str1,j);
				count++;	
			}
		}
		cout<<"Case"<<" "<<"#"<<k+1<<":"<<" "<<count<<"\n";	
	}
	
}
