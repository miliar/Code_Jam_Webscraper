#include <iostream>
#include <cstdio>
#include <fstream>
using namespace std;
int main()
{
	ifstream input;
	input.open("A-large.in", ios::in);
	ofstream output;
	output.open("Answer-A-large.txt", ios::out);
	int T, D[10], X;
	input>>T;
	X=T;
	while(X--)
	{
		long long int N, i, flag=0, x, j;
		for(i=0;i<10;i++)
			D[i]=0;
		input>>N;
		if(N!=0)
		{
			for(i=1; !flag; i++)
			{
				x=N*i;
				while(x)
				{
					D[x%10]=1;
					x=x/10;
				}
				flag=1;
				for(j=0;j<10 && flag;j++)
					if(D[j]==0)
						flag=0;
			}
		}
		if(!flag)
			output<<"Case #"<<T-X<<": INSOMNIA\n";
		else
			output<<"Case #"<<T-X<<": "<<(N*(i-1))<<"\n";
	}
	input.close();
	output.close();
	return 0;
}
