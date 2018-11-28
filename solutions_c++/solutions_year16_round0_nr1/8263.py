#include <iostream>
using namespace std;

int main() {
	
	long int T,N;
	cin>>T;
	for(int k=0;k<T;k++)
	{
		cin>>N;
		int c=0,a[10]={0,0,0,0,0,0,0,0,0,0};
		if(N!=0)
		{
			for(int i=1;i<=100;i++)
			{
				long int t=N*i;
				long int p=t;
				while(t!=0)
				{
					int d=t%10;
					//cout<<d<<" ";
					t=t/10;
					if(!a[d])
					{
						//cout<<d<<" ";
						a[d]=1;
					
						c++;
					}
				}
				if(c==10)
				{
					cout<<"Case #"<<k+1<<": "<<p<<"\n";
					break;
				}
			}
		}
		else
			cout<<"Case #"<<k+1<<": INSOMNIA\n";
	}
	
	return 0;
}