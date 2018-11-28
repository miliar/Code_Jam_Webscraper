#include <iostream>
#include <cstdio>
#include <fstream>
#include <cstring>
using namespace std;
int main()
{
	ifstream input;
	input.open("B-large.in", ios::in);
	ofstream output;
	output.open("Answer-B-large.txt", ios::out);
	int T, X;
	input>>T;
	X=T;
	while(X--)
	{
		char s[100];
		input>>s;
		int i, j, l=strlen(s), x[100], count=0;
		for(i=0;i<l;i++)
		{
			x[i]=0;
			if(s[i]=='+')
				x[i]=1;
		}
		for(i=l-1;i>=0;i--)
			if(!x[i])
			{
				for(j=i;j>=0;j--)
					x[j]=1-x[j];
				count++;
			}
		output<<"Case #"<<T-X<<": "<<count<<"\n";
	}
	input.close();
	output.close();
	return 0;
}
