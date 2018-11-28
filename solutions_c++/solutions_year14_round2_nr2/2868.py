#include<algorithm>
#include<map>
#include<iomanip>
#include<queue>
#include<set>
#include<string>
#include<vector>
#include<iostream>
#include<cstring>
#include <fstream>
#include <stack>

using namespace std;

#define FORA(a, b) for(int i =(a); i <=(b); ++i)
#define FORD(i, a, b) for(int i = (a); i >= (b); --i)
#define For(b) for(int i=0; i<(b); i++)
#define PB push_back
#define SQR(a) ((a)*(a))
#define ulld unsigned long long int
#define lld unsigned long long int

int main()
{
	ifstream fin("B-small-attempt1.in");

	ofstream fout("p1.out");
	
	int T;
	fin>>T;

	for(int i=0; i<T; i++)
	{
		int A,B,K;
		fin>>A;
		fin>>B;
		fin>>K;
		if( A<1 || A>1000 || B<1||B>1000||K<1||K>1000)
			return 1;

		int total;
		if(K>B || K>A)
		{
			total = A*B;
		}
		else
		{
			total = B*K+(K*(A-K));

			for(int i=K; i<A; i++)
				for(int j=K; j<B; j++)
				{
					int a=i&j;
					if(a < K)
						total++;
				}
		}
		fout<<"Case #"<<i+1<<": "<<total<<endl;
	}
	
	return 0;
}