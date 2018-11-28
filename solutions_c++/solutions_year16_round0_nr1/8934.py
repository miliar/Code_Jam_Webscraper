#include <iostream>
#include <math.h>
using namespace std;

int main() {
	int T;
	cin>>T;
	for(int i=0;i<T;i++)
	{
		int N,n,num[10];
		for(int j=0;j<10;j++)
			num[j]=0;
		cin>>N;
		if(N==0)
			cout<<"Case #"<<i+1<<": INSOMNIA\n";
		else
		{
			for(int j=1;;j++)
			{
				n=N*j;
				int q=n,r,k=1,x=0;
				while(q)
				{
					r=q%(int)pow(10,k);
					num[r]++;
					q=q/(int)pow(10,k);
				}
				while(x<10 && num[x]){x++;}
				if(x==10)
				{
					cout<<"Case #"<<i+1<<": "<<n<<"\n";
					break;
				}
			}
		}
	}
	return 0;
}