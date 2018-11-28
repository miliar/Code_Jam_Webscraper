#include <bits/stdc++.h>
using namespace std;

ifstream fin("A-large.in");
ofstream fout("output.txt");

int total(int smax, string np)
{
	int tot = 0,l,p,s;
	l=smax+1;
	s=np[0]-'0';
	for(int i=1;i<l;i++)
	{
		if(s<=i)
		{
			p=i-s;
			tot=tot+p;
			s=s+p;
		}
 		s=s+np[i]-'0';
	}

	return tot;
}
 
int main()
{
	ios_base::sync_with_stdio(false);
	int t,smax;
	string np;
	fin>>t;
	int m=t;
	while(t--)
	{
		fin>>smax>>np;
		fout<<"Case #"<<m-t<<": "<<total(smax,np)<<endl;
	}
	return 0;
}