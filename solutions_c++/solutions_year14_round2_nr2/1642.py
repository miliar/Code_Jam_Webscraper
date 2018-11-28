// Codejam2014_1A.cpp : Defines the entry point for the console application.
//



#include "vector"
#include "string"
#include "set"
#include "map"
#include "sstream"
#include "algorithm"
#include "cmath"
#include "cassert"
#include "iostream"
#include "numeric"
#include "fstream"
#ifdef __GNUC__
#include  <tr1/unordered_map>
#define unordered_map tr1::unordered_map
#else
#include <unordered_map>
#endif

using namespace std;

#define int64 long long
#define F(vec, index) for (int index = 0; index  < vec.size(); ++index)
#define F_S(vec, index, start) for (int index = start; index  < vec.size(); ++index)






int main(int argc, char* argv[])
{
	ifstream cin("in.txt");
	ofstream cout("out.txt");

	int T;
	cin >> T;
	for (int t = 0; t < T; ++t)
	{
		int A, B, K;
		cin >>  A >> B >> K;
		std::cout << t <<endl;
		int res = 0;
		for (int i = 0; i < A; ++i)
		{
			for (int j = 0; j < B; ++j)
			{
				if ((i & j) < K)
				{
					res++;
				}
			}
		}
		
		cout << "Case #" << t + 1 << ": "  << res << endl;
		
		
	}

	return 0;
}
