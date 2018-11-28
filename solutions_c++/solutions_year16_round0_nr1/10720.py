#include<bits/stdc++.h>
using namespace std;
int main()
{
	ios_base::sync_with_stdio(false);
	int T;
	int it;
	cin>>T;
	int a[10];
	int temp;
	for(int i=0;i<T;i++)
	{
		 for(int j=0;j<10;j++)
		 {
			 a[j]=0;
		 }
		 long long int n;
		 cin>>n;
		 if(n==0)
		 {
			 cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
		 }
		 else
		 {
			 int flag=0,b=1;
			 while(flag==0)
			{
				temp=n*b;
				while(temp!=0)
				{
					if(a[temp%10]==0)
					{
						a[temp%10]++;
					}
					temp=temp/10;
				}
				flag=1;
				for(int j=0;j<10;j++)
				{
					if(a[j]==0)
					{
						flag=0;
						break;
					}
				}
				b++;

			}
			 cout<<"Case #"<<i+1<<": "<<n*(b-1)<<endl;
		 }
	}

	return 0;
}
