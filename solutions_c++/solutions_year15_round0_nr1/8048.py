#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream A;
	A.open("A-large.in");
	ofstream B;
	B.open("A-large.doc");
	int t;
	A>>t;
	for(int i=1; i<=t; i++)
	{
		int smax;
		A>>smax;
		string S;
		A>>S;
		int n=0, cnt=0;
		for(int j=0; j<=smax; j++)
		{
			if(n<j)
			{
				cnt=cnt+j-n;
				n=j;
			}
			n=n+S[j]-'0';
		}
		B<<"Case #"<<i<<": "<<cnt<<endl;
	}
	return 0;
}
