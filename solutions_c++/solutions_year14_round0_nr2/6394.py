#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <queue>

using namespace std;

int main()
{
	int T;
	cin>>T;
	for(int N=0; N<T; N++)
	{
		double C, F, X;
		cin>>C>>F>>X;
		double best_time=X/2;
		double rate=2.0, t=0.0;
		while(t<best_time)
		{
			best_time=min(best_time, (t+X/rate));
			t+=C/rate;
			rate+=F;
		}
		//cout<<"Case #"<<N+1<<": "<<best_time<<endl;
		printf("Case #%d: %.7lf\n", N+1, best_time);
	}
	return 0;
}