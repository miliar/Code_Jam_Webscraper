#include<iostream>
#include<cstdio>
#include<fstream>
using namespace std;
int main()
{
	ifstream fin("a.txt");
	ofstream fout("b.in");
	int t,N,ncount,kcount,i,j,K,counter;
	float n[1005],k[1005],temp;
	fin>>t;
	for(K=1;K<=t;K++)
	{
		fin>>N;
		for(i=1;i<=N;i++)
		{
			fin>>n[i];
			for(j=i;j>1;j--)
			{
				if(n[j]<n[j-1])
				{
					temp=n[j];
					n[j]=n[j-1];
					n[j-1]=temp;
				}
				else break;
			}
		}
		for(i=1;i<=N;i++)
		{
			fin>>k[i];
			for(j=i;j>1;j--)
			{
				if(k[j]<k[j-1])
				{
					temp=k[j];
					k[j]=k[j-1];
					k[j-1]=temp;
				}
				else break;
			}
		}
		//for(i=1;i<=N;i++) fout<<n[i]<<' ';fout<<endl;
		//for(i=1;i<=N;i++) fout<<k[i]<<' ';fout<<endl;
		kcount=0;
		ncount=0;
		counter=1;
		i=1;
		while(counter<=N)
		{
			if(n[i]<k[counter])
			{
				kcount++;
				counter++;
				i++;
			}
			else
			{
				counter++;
			}
		}
		counter=N;
		i=N;
		while(counter>=1)
		{
			if(n[i]>k[counter])
			{
				ncount++;
				counter--;
				i--;
			}
			else
			{
				counter--;
			}
		}
		fout<<"Case #"<<K<<": "<<ncount<<' '<<(N-kcount)<<endl;
	}
}
				
