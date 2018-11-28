#include <bits/stdc++.h>
using namespace std;

int up(char s[], int n)
{
	if(n==0)
		return 0;
	if(s[n-1]=='-')
	{
		for(int i=0;i<n;i++)
		{
			if(s[i]=='+')
			{
				s[i]='-';
			}
			else
			{
				s[i]='+';
			}
		}
		return (1 + up(s,n-1));
	}
	else
		return up(s,n-1);
}
int main()
{
	int t,n,c,l;
	ifstream file;
	file.open("B-large.in");
	ofstream gadhu;
	gadhu.open("pancakesout.txt");
	char s[100];
	file>>t;
	for(int i=1; file>>s; i++)
	{
		
		l= strlen(s);
		c= up(s, l);
		gadhu<<"Case #"<<i<<": "<<c<<endl;
	}
	file.close();
	gadhu.close();
	return 0;
}