#include <iostream>
#include <algorithm>
#include <vector>
#include <iomanip>
#include <string>
#include <cstdio>
using namespace std;



int main()
{
	
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	long long int A,B,K;
	cin>>T;
	for(int i=0; i<T; i++)
	{
		cin>>A>>B>>K;
		long long int count = 0;
		for(long long int i=0; i<A; i++)
			for(long long int j=0; j<B; j++)
			{
				//cout<<i<<" "<<j<<" "<<(i&j)<<endl;
				if((i&j) < K) {count++;}
		
			}
		cout<<"Case #"<<i+1<<": "<<count<<endl;
	}
	
	return 0;
}

