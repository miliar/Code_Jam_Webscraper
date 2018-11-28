#include<bits/stdc++.h>
using namespace std;
int  main()
{
	ifstream file1;
		file1.open("A-large (1).in");
		if(file1.fail())
		{
			cerr<<"Error opening File\n";
			exit(1);
		}
		ofstream file2;
		file2.open("outputLn.txt");
	int T,k=1;;
	file1>>T;
	while(T--)
	{
		int smax,sum=0,tot=0;
		file1>>smax;
		char str[smax+1];
		file1>>str;
		int a[smax+1];
		for(int i=0;i<smax+1;i++)
		a[i]=(int)str[i]-48;
		int min=a[0];
		for(int i=1;i<smax+1;i++)
		{
			if(a[i]<min)
			min=a[i];
		}
		for(int i=smax;i>=1;i--)
		{
			tot=0;
			for(int j=i-1;j>=0;j--)
			tot+=a[j];
			if(tot<i)
			{
				sum+=(i-tot);
				for(int l=0;l<i;l++)
				{
					if(a[l]==min)
					{
						a[l]=(i-tot);
						break;
					}
				}
			}
		}
		file2<<"Case #"<<k<<": "<<sum<<"\n";
		
		k++;
	}
	return 0;
}
