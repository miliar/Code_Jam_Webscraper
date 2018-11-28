#include<iostream>
using namespace std;
#define ull unsigned long long
int main()
{
	int test;
	//test=1000000;
	cin>>test;
	for(int tt=1;tt<=test;tt++)
	{
		ull n;
		//n=tt;
		cin>>n;
		int arr[10]={0};
		int rem=10;
		if(n==0)
		{
			cout<<"Case #"<<tt<<": INSOMNIA\n";
		}
		else
		{
			ull tot=n;
			while(1)
			{
				if(rem==0)
					break;
				ull temp=tot;
				while(temp>0)
				{
					if(arr[temp%10]==0)
					{
						arr[temp%10]=1;
						rem--;
					}
					temp/=10;
				}
				if(rem==0)
				break;
				tot+=n;
			}
			cout<<"Case #"<<tt<<": "<<tot<<endl;
		}
	}
	return 0;
}
