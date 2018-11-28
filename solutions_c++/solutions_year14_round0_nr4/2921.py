#include<iostream>
#include<cstdlib>
using namespace std;
int cmpup(const void *a,const void *b)
{
	double n=*(const double *)a;
	double m=*(const double *)b;
	return n<m;
}
int cmpdown(const void *a,const void *b)
{
	double n=*(const double *)a;
	double m=*(const double *)b;
	return n<m;
}
int main()
{
	int T;
	cin>>T;
	for(int t=0;t<T;t++)
	{
		int N;
		cin>>N;
		double  arr1[N];
		double arr2[N];
		double namo[N],ken[N];
		for(int i=0;i<N;i++)
			cin>>arr1[i];
		for(int i=0;i<N;i++)
			cin>>arr2[i];
		int dwin=0,win=0;
		qsort(arr1,N,sizeof(double),cmpdown);
		qsort(arr2,N,sizeof(double),cmpdown);
		for(int i=0;i<N;i++)
			namo[i]=arr1[i];
		for(int i=0;i<N;i++)
			ken[i]=arr2[i];
	/*	for(int i=0;i<N;i++)
			cout<<namo[i]<<" ";
		cout<<endl;
		for(int i=0;i<N;i++)
			cout<<ken[i]<<" ";
		cout<<endl;*/
		for(int i=0;i<N;i++)
		{	if(namo[i]>ken[i])
			{
				win++;
			
				
				for(int j=N-1;j>i;j--)
					ken[j]=ken[j-1];
				
			}	
		}		
		
		for(int i=0;i<N;i++)
			namo[i]=arr1[i];
		for(int i=0;i<N;i++)
			ken[i]=arr2[i];
		if(N==1)
			dwin=win;
		else
		{	
		for(int i=0;i<N;i++)
		{	if(namo[i]>ken[i])
				dwin++;
			else
			{
				
				for(int j=N-1;j>i;j--)
					namo[j]=namo[j-1];
			}
		}		
		}
					
		cout<<"Case #"<<(t+1)<<": "<<dwin<<" "<<win<<endl;	
	}	
	return 0;
}