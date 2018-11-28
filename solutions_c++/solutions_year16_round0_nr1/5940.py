#include <iostream>
#include <algorithm>
#include <cstdio>
#include <string>
#include <cstdlib>
#include <vector>
#include <utility>
#include <tuple>


using namespace std;

#define var long long

void test()
{
	var N,P,ans;
	cin>>N;

	if(!N)
	{
		cout<<"INSOMNIA";
		return;
	}

	int fl[10]= {0};

	int i,c=10;
	for(i=1; i<1000; i++ )
	{
		for(ans=P=i*N; P; P/=10)
		{//	clog<<"trying ... "<<P<<"\n";
			if(!fl[P%10])
				c-=fl[P%10]=1;
			if(!c)
			{
				cout<<ans;
				return;
			}
		}
	}

}

/*
5
0
1
2
11
1692

1
1692

*/


int main()
{
	long long T,i;
	cin>>T;
	for(i=1; i<=T; i++)
	{
		cout<<"Case #"<<i<<": ";
		test();
		cout<<"\n";
	}
	return 0;
}
