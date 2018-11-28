#include <iostream>
using namespace std;

int ans;

void rev(string &s,int b, int e)
{
	if(b < e)
	{	
		ans ++;
	}
	e--;
	while(b < e)
	{
		char t = s[b];
		s[b] = s[e];
		s[e] = t;
		b++; e--;
	}
}

void minimum(string &s, int length)
{
	if(length == 1)
	{
		if (s[0] == '-')
		{
			s[0]  = '+';
			ans ++;
		}
	}
	else if(s[length - 1] == '+')
	{
		minimum(s,length -1);
	}
	else
	{
		int i = 0;
		while(s[i] == '+')
		{
			s[i] = '-';
			i++;
		}
		rev(s,0,i);
		rev(s,0,length);
		for(int i = 0 ; i < length; i++)
		{
			if(s[i] == '+')
				s[i] = '-';
			else
				s[i] = '+';
		}
		minimum(s,length -1);
	}
}

int main() {
	int t;
	string s;
	cin>>t;
	for(int i = 1; i <= t; i++)
	{
		cin>>s;
		ans = 0;
		minimum(s,s.length());
		cout<<"Case #"<<i<<": "<<ans<<endl;
		//cout<<s<<endl;
	}
	return 0;
}