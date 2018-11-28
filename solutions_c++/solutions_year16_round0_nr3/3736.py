#include <iostream>
#include <cmath>
#include <cstdio>
#include <fstream>
#include <vector>
using namespace std;
int main()
{
	ifstream input;
	input.open("C-small-attempt1.in", ios::in);
	ofstream output;
	output.open("Answer-C-small.txt", ios::out);
	int T;
	input>>T;
	int N, J, coin[32], i;
	input>>N>>J;
	input.close();
	long long int j, k, count=0;
	vector<long long int> prime;
	for(j=3;j<(2<<14);j=j+2)
	{
		i=1;
		for(k=3;k<(j/3) && i;k=k+2)
			if(j%k==0)
				i=0;
		if(i)
		{
			prime.push_back(j);
			count++;
		}
	}
	for(i=1;i<N-1;i++)
		coin[i]=0;
	coin[0]=1;
	coin[N-1]=1;
	output<<"Case #"<<T<<":\n";
	while(J)
	{
		int base;
		unsigned long long int result, x, div[9];
		for(i=0;i<9;i++)
			div[i]=0;
		int flag2=1;
		for(base=2; base<=10 && flag2; base++)
		{
			result=0;
			for(i=0;i<N;i++)
				result=result+(coin[i]*pow(base,N-1-i));
			if(result%2==0)		
				div[base-2]=2;
			else
			{			
				for(j=0;j<count && !div[base-2];j++)
					if(result%prime[j]==0)
						div[base-2]=prime[j];
			}
			if(!div[base-2])
				flag2=0;
		}
		if(flag2)
		{
			J--;
			for(i=0;i<N;i++)
				output<<coin[i];
			for(i=0;i<9;i++)
				output<<" "<<div[i];
			output<<"\n";
		}
		for(i=N-2, x=0; i>0 && !x ;i--)
			if(coin[i]==0)
				x=i;
		coin[x]=1;
		for(i=x+1;i<N-1;i++)
			if(coin[i]==1)
				coin[i]=0;
	}
	output.close();
	return 0;
}
