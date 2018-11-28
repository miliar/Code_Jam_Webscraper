#include<iostream>
using namespace std;

int main()
{
	int t;
	cin>>t;
	int count=0;
	long int R[t];
	while(count<t)
	{
		long int n;
		cin>>n;
		if(n==0)
		{
			R[count++]=-1;
			continue;
		}
		int j=1;
		bool t[10];
		for(int i=0;i<10;i++)
		t[i]=false;
		while(j)
		{
			bool flag = true;
			long int c = j*n;
			while(c)
			{
				t[c%10]=true;
				c=c/10;
			}
			for(int i=0;i<10;i++)
			{
				if(!t[i])
				flag=false;
			}
			if(flag)
			{
				R[count++] = j*n;
				break;
			}
			else
			++j;
		}
			
	}
	for(int i=0;i<t;++i)
	{
		if(R[i]==-1)
		cout<<"Case #"<<i+1<<": "<<"INSOMNIA"<<endl;
		else
		cout<<"Case #"<<i+1<<": "<<R[i]<<endl;
	}	
}
