#include<iostream>
#include<cstdio>
#include<cstdlib>

using namespace std;

int main()
{
	int T;
	scanf("%d ", &T);
	for(int t=1; t<=T; t++)
	{
		int N, R, P, S;
		scanf("%d %d %d %d", &N, &R, &P, &S);
		cout<<"Case #"<<t<<": ";
		if(R != S && R != P && P != S)
		{
			cout<<"IMPOSSIBLE"<<endl;
			continue;
		}
		if(abs(R-S) != 1 && abs(R-P) != 1 && abs(P-S) != 1)
		{
			cout<<"IMPOSSIBLE"<<endl;
			continue;
		}
		while(P>1 && R>1 && S>1)
		{
			cout<<"PRPSRS";
			P-=2;
			R-=2;
			S-=2;
		}
		if(P && R && P+R != S)
		{
			cout<<"PR";
			P--;
			R--;
		}
		if(P && S)
		{
			cout<<"PS";
			P--;
			S--;
		}
		if(R && S)
		{
			cout<<"RS";
			R--;
			S--;
		}
		cout<<endl;//manually modify output for edge cases
	}
	return 0;
}
