#include<iostream>
#include<cmath>
#include<vector>
#include<algorithm>
using namespace std;

int main()
{
	int T;
	cin>>T;
	for(int i=0;i<T;++i)
	{
		long long unsigned r,t;
		cin>>r>>t;
		long long unsigned tempr=2*r-1;
		long long unsigned temps=8*t/(long double)tempr;
		long long unsigned val=floor(((sqrt(tempr)*sqrt(tempr+temps))-tempr)/4);
		while(2*r*val+2*val*val-val > t )
			--val;
		while((2*r*(val+1)+2*(val+1)*(val+1)-(val+1))<= t)
			++val;
		cout<<"Case #"<<i+1<<": "<<val<<endl;
	}
	return 0;
}