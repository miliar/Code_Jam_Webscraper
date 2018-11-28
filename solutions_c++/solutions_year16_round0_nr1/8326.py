#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	ifstream fin;
	ofstream fout;
	fin.open("A-large.in");
	fout.open("jam1lf.txt");
	int t,r,i;
	int num[20];
	long int n,c,j,k;
	long long int updatedn,s;
	fin>>t;
	i=1;
	while(t--)
	{ for(j=0;j<=9;j++) num[j]=0;
	fin>>n;
	if(n==0)
	{fout<<"Case #"<<i<<": INSOMNIA"<<endl;}
	else{
	c=0;
	for(k=1;;k++)
	{
		updatedn=k*n;
		s=updatedn;
		while(s!=0)
		{
			r=s%10;
			if(num[r]==0)
			{
				num[r]++;
				c++;
			}
			s=s/10;
		}
		if(c==10) break;
	}
	fout<<"Case #"<<i<<": "<<updatedn<<endl;

	}
	i++;
	}
	return 0;
}
