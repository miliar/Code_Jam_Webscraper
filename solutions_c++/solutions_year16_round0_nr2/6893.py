#include<iostream>
#include<string>
#include<string.h>
using namespace std;
int main()
{
	char S[100000];
	int i,j,T,l,c,t=0;
	cin >> T;
	while(T--)
	{	
		cin >> S;
		c=0;
		t++;
		l=strlen(S);
		for(i=0;i<l-1;i++)
		{
			if(S[i]!=S[i+1])
				c=c+1;
		}
		if(S[l-1]=='-')
			c++;

		cout << "Case #" << t << ": " << c << endl;
		

	}
}
