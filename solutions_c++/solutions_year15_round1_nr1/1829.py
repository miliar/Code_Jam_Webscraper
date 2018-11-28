#include<iostream>
#include<climits>
#include<fstream>
using namespace std;
int main()
{
		ofstream fout ("sub1.out");
    ifstream fin ("sub1.in");
		int tes;
		fin>>tes;
		for(int u=0;u<tes;u++)
		{
				fout<<"Case #"<<u+1<<": ";
				int n;
				fin>>n;
				long ar[n];
				unsigned long long ct1=0,ct2=0,max=0;
				for(int i=0;i<n;i++)
				{
						fin>>ar[i];
						if(i>0)
						{
								if(ar[i]<ar[i-1])
								{
										ct1+=ar[i-1]-ar[i];
										if(max<ar[i-1]-ar[i])
										{
												max=ar[i-1]-ar[i];
										}
								}
						}
				}
				for(int i=0;i<n-1;i++)
				{
						if(ar[i]<max)
						{
								ct2+=ar[i];
						}
						else
						{
								ct2+=max;
						}
				}
				//ct2-=ar[n-1];
				fout<<ct1<<' '<<ct2<<'\n';
				//ct2=n-1*max;
		}
		return 0;
}
								
								
						
						
				
