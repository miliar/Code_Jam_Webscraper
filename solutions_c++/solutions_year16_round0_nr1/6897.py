#include <iostream>
#include <cstdio>
using namespace std;
int main()
{
	int tz;
	cin>>tz;
	for (int ta=1;ta<=tz;ta++)
	{
		printf("Case #%d: ",ta);
		int n;
		cin>>n;
		if (n==0)
		{
			cout<<"INSOMNIA"<<endl;
			continue;
		}
		int count=0;
		bool flag[10]={0};
		int now=0;
		while (1)
		{
			count++;
			now+=n;
			if (count>100000)
			{
				cout<<"INSOMNIA"<<endl;
				break;
			}
			int tnow=now;
			while (tnow>0)
			{
				flag[tnow%10]=1;
				tnow/=10;
			}
			bool done=true;
			for (int i=0;i<=9;i++)
				if (flag[i]==false)
					done=false;
			if (done)
			{
				cout<<count*n<<endl;
				break;
			}
		}
	}
}
