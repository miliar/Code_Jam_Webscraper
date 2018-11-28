#include<iostream>
#include<string.h>
#include <algorithm>
using namespace std;

int max(int P[],int,int);


int main()
{
	int T;
	cin>>T;
	for(int i=0;i<T;i++)
	{
		int N;
		cin>>N;
		
		int P[N];
		int senetor=0;
		for(int j=0;j<N;j++)
		{
			cin>>P[j];
			senetor=senetor+P[j];
		}
		char eva[senetor];
		memset(eva,'\0',senetor);
		int l=0;
		for(int j=0;j<senetor;j++)
		{
			l=max(P,N,l);
			P[l]--;
			eva[j]=(char)('A'+l);
		}		

		cout<<"Case #"<<i+1<<": ";

		if(senetor%2)
		{
			for(int j=0;j<senetor;j++)
			{
				cout<<eva[j];
				if((senetor-j)==3)
				{	
					cout<<" ";
				}
				else
				{
					j++;
					cout<<eva[j]<<" ";
				}		
			}
			cout<<"\0"<<endl;
		}
		else
		{
			for(int j=0;j<senetor;j++)
			{
				cout<<eva[j];
				j++;
				cout<<eva[j]<<" ";
			}		
			cout<<"\0"<<endl;
		}
	}
}

int max(int P[],int N,int l)
{
	int maximum = P[l];
 	int location=l;
  	for (int c = 0; c <N; c++)
  	{
    		if (P[c] > maximum)
    		{
       			maximum  = P[c];
       			location = c;
    		}
  	}
	return location;
}


