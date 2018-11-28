#include<iostream>
#include<cstring>
#include<fstream>
using namespace std;
char L[10000001];
int main()
{
	int t,i;
	ifstream fin("C:/a.txt");
	ofstream fout("C:/o.txt");
	long long n,slength,cs,j,k,temp,sval,snum;
	char ch;
	fin>>t;
	for(i=0;i<t;i++)
	{
		fin>>L>>n;
		
		snum=0;
		slength=strlen(L);
		temp=slength;
		cs=slength-n+1;
		for(k=0;k<cs;k++)
		{
			temp=slength;
			
		while(1)
		{
			sval=0;
			for(j=k;j<temp;j++)
			{
			ch=L[j];
				
				if(ch!='a' && ch!='e' && ch!='i' && ch!='o' && ch!='u')
				{
					sval++;
					if(sval==n)
					{
						snum++;
						break;
					}
				}
				else
			    	sval=0;

			}
			temp--;
			
			if((temp-k)<n)
				break;
		}
	}
		fout<<"Case #"<<(i+1)<<": "<<snum<<endl;
	}
	return 0;
}