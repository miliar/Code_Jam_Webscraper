#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <string>
using namespace std;
int main()
{
	int T,A,B,K;
	cin >> T;
	for(int t=1;t<=T;t++)
	{
		int result=0;
		cin >> A >> B >> K ;
		for(int i=0;i<A;i++)
		{
			for(int j=0;j<B;j++)
			{
				if( (i&j) < K )
					result ++;
			}
		}
		cout << "Case #" << t << ": "<<result << endl;
	}
	return 0;
}