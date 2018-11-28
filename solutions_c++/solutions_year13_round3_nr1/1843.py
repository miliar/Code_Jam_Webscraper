#include<iostream>
#include<fstream>
#include<stdlib.h>
#include<cstring>
#include<math.h>
#include<inttypes.h>
using namespace std;

ofstream op;

int main()
{
	ifstream ip;
	ofstream op;
	unsigned long i,j,k,l,temp;
	unsigned long T,n;
	op.open("output.txt");	
	ip.open("A-small-attempt2.in");
	ip>>T;
	char *t=new char[1000000];
	long A,N,X,Y,w,sum;
	long count,val;
	long B;
	for(l=0;l<T;l++)
	{
		ip>>t;
		ip>>N;
		val=strlen(t);
		count=0;
		for(i=0;i<val;i++)
		{
			sum=0;
			for(j=i;j<val;j++)
			{
				
				if(t[j]!='a' && t[j]!='e' && t[j]!='i' && t[j]!='o' && t[j]!='u')
				{
					sum++;
					if(sum==N)
						break;

				}					
				else
					sum=0;
			}
			//cout<<l<<" "<<j<<"\n";
			if(j==val)
				continue;
			else
			{
				count+=val-j;
			}
		}
		op<<"Case #"<<l+1<<": "<<count<<"\n";
		
	}
	ip.close();
	op.close();
	return 0;
	
}
