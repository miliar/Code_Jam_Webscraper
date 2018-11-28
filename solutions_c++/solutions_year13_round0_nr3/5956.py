#include <iostream>
#include <cmath>
#include <stdio.h>

using namespace std;

int ispalindrom (int a)
{
	int b=a;
	string s="",z="";

	for (;b>0;b/=10)
	{
		s+=(char)('0'+(b%10));
	}

//	cout<<"dddddddddd      "<<s<<'\n';

	for (int j=0;j<s.length();j++)
		z+=s[s.length()-1-j];

//	cout<<"dddddddddd      "<<s<<'\n';

	if (z==s)
		return 1;
	else
		return 0;
}


int main ()
{
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	

	int T,A,B;
	cin >> T;

	for (int i=0;i<T;i++)
	{
		int answer=0;
		cin >> A >> B;

		for (int h=A;h<=B;h++)
		{
			if ( ((int) sqrt(h) ) * ((int) sqrt(h) ) == h )
			{
				if (ispalindrom(h)&& ispalindrom( (int) sqrt(h) ) )
					answer++;					
			}
		}

		cout<<"Case #"<<i+1<<": "<<answer<<'\n';

	}


	return 0;
}
