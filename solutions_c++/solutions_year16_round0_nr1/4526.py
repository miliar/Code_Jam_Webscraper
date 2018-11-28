#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;
int dig[10];
int dCount;
void breakAndMark(long long n)
{
	int d=1;
	while(n)
	{
		if(!dig[n%10])
		{
			dig[n%10]=1;
			dCount++;
		}
		n/=10;
	}
}
int main(int argc, char const *argv[])
{
	/* code */
	int T;
	cin>>T;
	int mx=0;
	for(int t=1;t<=T;++t)
	{
		memset(dig,0,sizeof dig);
		dCount=0;
		long long N;
		cin>>N;
		bool flag=0;
		if(N)
		for (int i = 1; i < 100; ++i)
		{
			/* code */
			//cout<<i*N<<endl;
			breakAndMark(i*N);
			if(dCount==10)
			{
				flag=1;
				mx=max(mx,i);
				cout<<"Case #"<<t<<": "<<i*N<<endl;
				break;
			}
				
		}
		if(!flag)
			cout<<"Case #"<<t<<": INSOMNIA"<<endl;
	
	}
	//cout<<mx<<endl;
	return 0;
}