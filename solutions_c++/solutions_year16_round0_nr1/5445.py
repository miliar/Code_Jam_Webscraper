#include<bits/stdc++.h>

using namespace std;
int main()
{
    ios_base::sync_with_stdio(0);
	int test;
		ifstream cin ("in.txt");
	ofstream cout("out.txt");
	cin >> test;
	int h[10]={0};

	for(int t=1;t<=test;t++)
	{
		long long n;
		cin>>n;
		if(!n)
		{
			cout<<"Case #"<<t<<": INSOMNIA"<<'\n';
		}
		else{

			int i=1,flag=1;


			memset(h,0, sizeof(h));
			int hash = 0;
			while(flag)
			{
				long long  prod = i *n;
				while( flag && prod)
				{
					long long k = prod%10;
					prod/=10;
					if(h[k]==0)
					{
						hash++;
						if(hash ==10)
						{
							flag =0;
						}
						h[k]++;
					}
				}
				i++;
			}
			cout<<"Case #"<<t<<": "<<n*(i-1)<<'\n';
	}
}
 	return 0;
}
