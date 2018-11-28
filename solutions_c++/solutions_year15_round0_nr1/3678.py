#include<bits/stdc++.h>
using namespace std;

main()
{
	int T, smax, t=0;
	int sum=0, ctr=0;
	fstream fin("A2.in",ios::in);
	fstream fout("1b.txt",ios::out);
	fin>>T;
	while(t++<T)
	{
		fin>>smax;
		int s[smax+1]; char c;
		for(int i=0;i<=smax;i++)
		{
			fin>>c;
			s[i]=(c-'0');
		}
		sum=s[0]; ctr=0;
		for(int i=1;i<=smax;i++)
		{
			if(i>sum)
				while(i>sum)
				{
					ctr++;
					sum++;
				}
			sum+=s[i];
		}
		fout<<"Case #"<<t<<": "<<ctr<<endl;
	}
}
