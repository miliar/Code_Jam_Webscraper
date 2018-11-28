#include <iostream>
using namespace std;
bool check(string s,int n)
{
	int counter=0;
	for(int i=0;i<s.length();i++)
	{
		if((s[i]!='a')&&(s[i]!='e')&&(s[i]!='i')&&(s[i]!='o')&&(s[i]!='u'))
		{counter++;
		
		if (counter==n)
			return true;
		
		}
		else
		counter=0;
	}
	return false;
}
int main()
{       
		int no;
		cin>>no;
		int n[no];
		int nval[no];
		string names[no];
 	for(int i=0;i<no;i++)
	{	cin>>names[i];
		cin>>n[i];
		nval[i]=0;
	}
	for(int i=0;i<no;i++)
	{ 
	for(int j=1;j<=names[i].length();j++)
		for(int k=0;k<=(names[i].length()-j);k++)
		{  if(check(names[i].substr(k,j),n[i]))
			nval[i]++;
		}
	}
	for(int i=0;i<no;i++)
	{
	cout<<"Case #"<<i+1<<": ";
	cout<<(nval[i])<<endl;
	}
	
}