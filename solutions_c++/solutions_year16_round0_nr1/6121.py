#include<iostream>

using namespace std;

int allone(int flag[10])
{
	for(int i=0;i<10;i++)
	{
		if(flag[i]==0)
			return 0;
	}
	return 1;
}

int main()
{
	int T,flag[10],temp;
	cin>>T;
	long long N,M,keep;
	
	

	for(int i=0;i<T;i++)
	{
		int f=0;
		for(int j=0;j<10;j++)
			flag[j]=0;

		cin>>N;
		keep=N;
		int k=2;
		while(k<500)
		{
			temp=N%10;
			flag[temp]=1;
			M=N/10;
			while(M!=0)
			{				
				temp=M%10;
				flag[temp]=1;
				M=M/10;
			}
			if(allone(flag))
			{
				f=1;
				break;
			}
			N=k*keep;
			k++;
		}
		if(f)
			cout<<"case #"<<(i+1)<<": "<<N<<endl;
		else
			cout<<"case #"<<(i+1)<<": INSOMNIA"<<endl;
			
	}
}
