#include <iostream>
using namespace std;

int a[10];

int checkDone()
{
	for(int i=0;i<10;i++)
		if(a[i]==0)
			return 0;
	return 1;
}

int main()
{
	int T,b;
	long int N,N1,N2;
	cin>>T;
	int i;
	for(i=0;i<10;i++)
		a[i]=0;
	for(i=0;i<T;i++)
	{
		cin>>N;
		//N1=N;
		if(N==0)
		{
			cout<<"Case #"<<i+1<<": "<<"INSOMNIA"<<endl;
			continue;
		}
		
		int j=1;
		while(!checkDone())
		{
			N2=j*N;
			N1=N2;
			
			while(N1>0)
			{
				b=(N1)%10;
				a[b]=1;
				N1=N1/10;
			}
			j++;

		}
		cout<<"Case #"<<i+1<<": "<<N2<<endl;
		for(j=0;j<10;j++)
			a[j]=0;

	}
	return 0;
}