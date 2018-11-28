#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int N;
string S;

int main()
{
	ifstream OpenFile("A-large2.txt");
	ofstream SaveFile("output3.txt");

	int T;
	OpenFile>>T;
	for (int t = 0; t < T; t++)
	{
		OpenFile>>N;
		OpenFile>>S;
		int res=0;
		int sum=0;
		for (int i = 0; i < N; i++)
		{
			if(S[i]!='0')
				sum=sum+(S[i]-48);
			else
			{
				if(i<sum)
					continue;
				else
				{
					res++;
					sum++;
				}
			}
		}
		if(N>sum)
			res+=(N-sum);
		SaveFile<<"Case #"<<t + 1<<": "<<res<<endl;
	}
	return 0;
}
