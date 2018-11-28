#include<iostream>
#include<stdio.h>
#include<string.h>
#include<fstream>
using namespace std;
#define cin fin
#define cout fout


int main()
{

	ifstream fin("input.in");
	ofstream fout("o.out");
	int T;
	int N;
	int A[10000];
	cin>>T;
	int S=0;
	//string s;
	int s=0;
	int max=0;
	int x=0;
	int sum=0,c=0,i=0,j=1;
	while(j!=T+1)
	{
	s=0;S=0;max=0;x=0;
	cin>>N;
	cin>>A[0];

		
	
	for(i=1;i<N;i++)
	{
		cin>>A[i];
		if(A[i]<A[i-1])
		{
			x=A[i-1]-A[i];
			s+=x;
			if((x)>max)
				max=x;
			
		}
		
	
	}
	for(i=0;i<N-1;i++)
	{
		if(max>A[i])
			S+=A[i];
		else 
		S+=max;
	}	 
	cout<<"Case #"<<j++<<": "<<s<<" "<<S<<endl;	   	   
	}
	return 0;
}

