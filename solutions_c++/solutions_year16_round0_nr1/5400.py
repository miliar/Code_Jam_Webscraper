#include <bits/stdc++.h>
using namespace std;
int flag[10];

int main()
{
	int T;
	int N;
	cin>>T;
	int c=0;
	int super;
	while(T--)
	{
		cin>>N;
//		super=0;
		memset(flag, 0, sizeof(flag));
		int i=1;
		int prod2;
		while(true)
		{
			int prod=i*N;
			prod2=i*N;
			super=0;
			while(prod!=0)
			{
				flag[prod%10]=1;
				prod=prod/10;
			}
			if(i==1000)
			{
				prod2=-1;
				break;
			}
			for(int j=0;j<10;j++)
				if(flag[j]==0)
					super=1;
			if(super==0)
				break;
			i++;
		}
		if(prod2!=-1)
		cout<<"Case #"<<++c<<": "<<prod2<<endl;
		else
		cout<<"Case #"<<++c<<": INSOMNIA\n";
	}
}
		
