#include <iostream>
using namespace std;
int main()
{
	int test,t=0;
	cin>>test;
	int dec[10]={0};
	while(t++<test)
	{
		long long int N,Num,n;
		int win=11,ind=0,insom=0;
		for(int i=0;i<10;i++)dec[i]=0;

		cin>>Num;
		if(Num==0)
			{cout<<"Case #"<<t<<": INSOMNIA\n";continue;}

		N=Num;
		n=N;
		int flag=0,iter=1;
		while(flag==0)
		{
			ind++;
			n=N;
			while(n>0)
			{
				dec[n%10]=1;
				n/=10;
			}

			for(int i=0;i<10;i++)
			{
				if(dec[i]==0)
					{flag=1;break;}
			}
			if(flag==0)
				{cout<<"Case #"<<t<<": "<<N<<endl;break;}
			N=(++iter)*Num;
			//if(ind>win && flag==1)
				//{ind=0;insom=1;break;}
			flag=0;
		}
		if(insom)
			{cout<<"Case #"<<t<<": INSOMNIA\n";continue;}

	}
	return 0;
}