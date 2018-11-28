#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <assert.h>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int t = 0; t<T; t++) 
	{
		int A,B,K;
		cin >> A >> B >> K;

		/*
		if (A>B)
			swap(A,B);
		assert(A<B);
		*/

		long long result = 0;
		for(int b=0;b<B;b++) 
		for(int a=0;a<A;a++) 
		{
			if ((a&b) < K)
			{
				// cout << a << " " << b << " " << (a&b) << endl;
				result++;
			}

		}

		cout << "Case #" << (t+1) << ": ";

		cout << result << endl;
	}
	return 0;
}
