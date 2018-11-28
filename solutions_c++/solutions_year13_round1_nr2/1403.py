#include <iostream>
using namespace std;

int main()
{
	long long t;
	cin>>t;
	for (long long i1 = 1; i1 <= t; ++i1)
	{
		long long E,R,N;
		cin>>E>>R>>N;
		long long* v=new long long[N];
		for (long long i = 0; i < N; ++i)
		  cin>>v[i];
		long long** optimal=new long long*[E+1];
		for (long long i = 0; i <= E; ++i)
			optimal[i]=new long long[N];
		for (long long i = 0; i <= E; ++i)
		{
			optimal[i][0]=i*v[0];
		}
		for (long long j = 1; j <N ; ++j)
		{
			for (long long i = 0; i <= E; ++i)
			{
				optimal[i][j]=-1;
				for (long long k = 0; k <= i; ++k)
				{
					long long newenergy;
					if(i-k+R<=E)
					 newenergy=i-k+R;
					else
						newenergy=E;
					if(optimal[i][j]<optimal[newenergy][j-1]+k*v[j])
						optimal[i][j]=optimal[newenergy][j-1]+k*v[j];
				}
			}
		}
		long long maximum=-1;
		for (long long i = 0; i <= E; ++i)
		{
			if(maximum<optimal[i][N-1])
				maximum=optimal[i][N-1];
		}
		cout<<"Case #"<<i1<<": "<<maximum<<endl;
	}
}
