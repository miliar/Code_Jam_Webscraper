#include <bits/stdc++.h>
#define llong long long

using namespace std;
int main()
{
	//ifstream cin("in.txt");
	//ofstream cout("out.txt");
	int T;
	cin>>T;
	for (int Q=1;Q<=T;Q++)
	{
		cout<<"Case #"<<Q<<": ";

		llong N;
		cin>>N;
		
		if (N==0)
		{
			cout<<"INSOMNIA"<<endl;
			continue;
		}
		
		bool f[12];
		memset(f,0,sizeof(f));

		int c=0;		
		llong i = N;
		while (c != 10 )
		{
			llong t=i;
			while (t)
			{
				f[t%10]=1;
				t/=10;
			}

			c = 0;
			for (int j=0;j<10;j++) if (f[j]) c++;
			i += N;
		}
		cout << i-N << endl;
	}

	return 0;
}
