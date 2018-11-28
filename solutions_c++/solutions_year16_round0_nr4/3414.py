/*
coded by @just_code21
© to Prakhar Srivastava
*/
#include<bits/stdc++.h>
#define ll long long int
#define M 1000000007
using namespace std;

int main()
{
	ifstream fcin("D-small-attempt0.in");
	ofstream fcout("output.txt");
	int t;
	fcin>>t;
	for(int i=1;i<=t;i++)
	{
		int k,c,s;
		fcin>>k>>c>>s;
		fcout<<"Case #"<<i<<": ";
		for(int j=1;j<=k;j++)
			fcout<<j<<" ";
		fcout<<"\n";
	}
	return 0;
}
/*

*/


