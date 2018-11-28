# include <iostream>
# include <cstdlib>
using namespace std;
int main()
{
	long long int T, N, n, k=1 ;
	cin>>T;
	int t=1;
	while(t<=T)
	{
		k=1;
		//cout<<"hi";
		cin>>N;
		if(!N) { cout<<"Case #"<<t<<": "<<"INSOMNIA\n"; t++; continue; }
		int a[10];
		bool done = false; 
		for (int i=0;i<10;i++)
			a[i]=0;
		while(!done)
		{
			n=N*k;
			done=true;

		//	cout<<k<<'\t'<<n<<"\n";
			for (int i=0;i<10;i++)
				if (a[i]==0) done = false;
			if (!done)
			{
				while(n)
				{
					a[n%10]++;
					n=n/10;
				}
			}
			k++;
			
		}
		cout<<"Case #"<<t<<": "<<N*(k-2)<<"\n";
		t++;
	}
	return 0;
}
