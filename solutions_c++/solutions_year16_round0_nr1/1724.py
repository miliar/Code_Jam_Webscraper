#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int main()
{
	freopen("Ain.txt","r",stdin);
	freopen("Aout.txt","w",stdout);
	int T;
	cin>>T;
	long long n,val,tmp;
	for(int t=1;t<=T;t++)
	{
		cin>>n;
		if(n==0)
		{
			printf("Case #%d: INSOMNIA\n",t);
			continue;
		}
		bool d[10]={false};
		int cnt=0,dig;
		for(val=n;;val+=n)
		{
			tmp=val;
			while(tmp)
			{
				dig=tmp%10;
				if(!d[dig])
				{
					cnt++;
					d[dig]=true;
				}
				tmp/=10;
			}
			if(cnt==10)
			{
				break;
			}
		}
		cout<<"Case #"<<t<<": "<<val<<endl;
	}
	return 0;
}