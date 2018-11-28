#include <bits/stdc++.h>

using namespace std;

int f(string x)
{
	if(x.length()==0)
		return 0;
	string y="",z;
	int i=x.length()-1;
	while(x[i]=='+')
	{
		i--;
		if(i<0)
			break;
	}
	for(int j=0;j<=i;j++)
		y+=x[j];
	if(y.length()==0)
		return 0;
	else if(y[0]=='+')
	{
		z=y;
		reverse(z.begin(),z.end());
		return 1+f(z);
	}
	else
	{
		for(int i=0;(i<y.length())?(y[i]=='-'):0;i++)
			y[i]='+';
		z=y;
		return 1+f(z);
	}
}

int main()
{
	int i=1;
	string s;
	cin>>s;
	while(cin>>s)
		cout<<"Case #"<<i++<<": "<<f(s)<<endl;
	return 0;
}