#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	int t;
	//freopen("A-large.in","rt+",stdin);
	//freopen("output.cpp","wt+",stdout);
    cin>>t;
    for(int c=1;c<=t;c++)
	{
		long long n;
		cin>>n;
		if(n==0){
            cout<<"Case #"<<c<<":"<< " INSOMNIA"<<endl;
            continue;
		}
		int a[10];
		int flag=0;
		for(int i=0;i<10;i++)
		{
			a[i]=0;
		}
		long long i=1,q=100;
		while(1)
		{
			long long z=n*i;
			while(z!=0)
			{
				long long x=z%10;
				a[x]++;
				z=z/10;
			}
			if(a[0]>=1&&a[1]>=1&&a[2]>=1&&a[3]>=1&&a[4]>=1&&a[5]>=1&&a[6]>=1&&a[7]>=1&&a[8]>=1&&a[9]>=1)
			{
				cout<<"Case #"<<c<<":"<<" "<<n*i<<endl;
				flag=1;
				break;
			}
			q--;
			i++;
		}
	}
}
