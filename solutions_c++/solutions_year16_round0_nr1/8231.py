#include<iostream>
#include<cstring>

using namespace std;
int main()
{
	int nt;
	cin>>nt;
	for(int t=1;t<=nt;t++)
	{
		long long int n;
		cin>>n;
		if(n==0)
		{
			cout<<"Case #"<<t<<": INSOMNIA"<<endl;
		}
		else{
 
			int i=1,flag=1;
			int ar[10];
			memset(ar,0,sizeof(ar));
			int arn = 0;
			while(flag)
			{
				long long int a = n*i;
				while(a&&flag)
				{
					int k = a%10;
					a=a/10;
					if(ar[k]==0)
					{
						arn++;
						if(arn==10)
						{
							flag=0;
						}
						ar[k]++;
					}
				}
				i++;
			}
			cout<<"Case #"<<t<<": "<<n*(i-1)<<endl;
	}
}
 	return 0;
}
 