# include <iostream>
# include <stdio.h>
using namespace std;
long long int a[10];
int main()
{
	ios_base::sync_with_stdio(false);
	long long int t;
	cin>>t;
	long long int i,j,k,l;
	for(i=0;i<t;i++)
	{
		for(j=0;j<10;j++)
			a[j]=0;
		long long int n;
		cin>>n;
		if(n==0)
			cout<<"Case #"<<(i+1)<<": INSOMNIA\n";
		else
		{
		long long int count=0;
		long long int temp;
		long long int lk=1;
		while(count!=10)
		{
	//		cout<<"a\n";
			temp=(lk)*n;
			long long int te=temp;
			while(te>0)
			{
				if(a[te%10]==0)
				{
					++count;
					++a[te%10];
				}
				te=te/10;
			}
			++lk;
		}
		cout<<"Case #"<<(i+1)<<": "<<temp<<endl;
		}
		}

	return 0;
}
