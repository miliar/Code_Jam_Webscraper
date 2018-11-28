#include <iostream>
#include <cstdio>
#include <fstream>
#include <cstring>
using namespace std;
int main()
{
	ifstream input;
	input.open("A-large.in", ios::in);
	ofstream output;
	output.open("Answer-A-large.txt", ios::out);
	int T, Q;
	input>>T;
	Q=T;
	while(Q--)
	{
		char S[1000];
		input>>S;
		int l=strlen(S), i, j;
		char P[1000];
		P[0]=S[0];
		for(i=1;i<l;i++)
		{
			if(S[i]>=P[0])
			{
				for(j=i-1;j>=0;j--)
					P[j+1]=P[j];
				P[0]=S[i];
			}
			else
				P[i]=S[i];
		}
		output<<"Case #"<<T-Q<<": ";
		for(i=0;i<l;i++)
			output<<P[i];
		output<<"\n";
	}
	input.close();
	output.close();
	return 0;
}
