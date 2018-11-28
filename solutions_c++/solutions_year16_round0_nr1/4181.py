#include <iostream>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <fstream>

using namespace std;
int main()
{
	ios_base::sync_with_stdio(0);
	long long t,test,key,a[10],rem,sum,tsum;
	int n,i,j;
	ifstream fin;
	ofstream fout;
	fin.open("A-large.in",ios::in);
	fout.open("output.txt",ios::out);
	fin>>t;
	test=t;
	while(t--)
	{
		key=-1;
		i=1;
		sum=0;
		fin>>n;
		if(n==0)
			{
			fout<<"Case #"<<test-t<<": INSOMNIA\n";
			}
			else
			{
			for(j=0;j<10;j++)
			{
				a[j]=0;
			}
		while(key==-1)
		{
			key=1;
			sum=i*n;
			tsum=sum;
			while(sum>0)
			{
				rem=sum%10;
				sum/=10;
				a[rem]++;
			}
			for(j=0;j<10;j++)
			{
				if(a[j]==0)
				{
				key=-1;
				break;
				}
			}
			i++;
		}
		fout<<"Case #"<<test-t<<": "<<tsum<<"\n";
		}
	}
	fin.close();
	fout.close();
	return 0;
}
