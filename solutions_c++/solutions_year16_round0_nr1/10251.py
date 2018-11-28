#include<iostream>
using namespace std;
int main()
{
	int T,k,i,A[10]={0},c=0;
	cin>>T;
	long long S,N,flag[100]={0};
	for(int t=0;t<T;t++)
	{
		cin>>N;
		if(N==0)
		flag[t]=0;
		else
		{
			for(int o=0;o<10;o++)
			A[o]=0;
			//c=1;
			//cout<<"yiuy"<<7<<A[7]<<"\n";
			i=1;
			while(flag[t]==0)
			{
				S=i*N;
				while(S!=0)
				{
					k=S%10;
					A[k]=1;
					S/=10;
				}
			i++;
			c=1;
			for(int y=0;y<10;y++)
			if(A[y]!=1)
			{
				c=0;
				break;
			}
			if(c==1)
			flag[t]=(i-1)*N;
			}
		}
	}
	for(int u=0;u<T;u++)
	if(flag[u]==0)
	cout<<"Case #"<<u+1<<": INSOMNIA\n";
	else
	cout<<"Case #"<<u+1<<": "<<flag[u]<<"\n";
	return 0;
}

