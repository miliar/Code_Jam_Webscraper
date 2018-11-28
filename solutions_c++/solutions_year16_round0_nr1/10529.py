#include<bits/stdc++.h>

using namespace std;
long long int a,i,n,f,m,cnt,rem,num,n2,t=1;
int main()
{
	cin>>n;
	while(n--)
	{
		cin>>a;
		
		cnt=0;
		long long int f=1,hp[12]={0};
		if(a==0)
		{
			cout<<"Case #"<<t<<": INSOMNIA\n";
			t++;
			continue;
		}
		while(f)
		{
			for(i=1;cnt<10;i++)
			{
				
				num=i*a;
				n2=num;
				while(num>0)
				{
					rem=num%10;
					if(hp[rem]!=1)
					{
						hp[rem]=1;
						cnt++;
					}
					num/=10;
				}
				if(cnt==10)
				{
					cout<<"Case #"<<t<<": "<<n2<<endl;
					f=0;
					t++;
					break;
				}
			}
		}
	}
	return 0;
}
