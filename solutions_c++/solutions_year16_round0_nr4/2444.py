#include <vector>
#include <iostream>
#include <gmp.h>
#include <gmpxx.h>

using namespace std;

typedef mpz_class LL;




int main()
{	
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++)
	{
		cout << "Case #" << t << ":";
		
		int K,C,S;
		cin >> K >> C >> S;

		vector<LL> pos;
		for(int i = 0; i < K; i++)
		{
			LL z = 0;
			z += i;
			pos.push_back(z);
		}

		for(int i = 0; i < C - 1; i++)
		{

			vector<LL> npos(K);
			for(int j = 0; j < K; j++)
				npos[j] = pos[j]*K + j;
		
			pos = npos;
		}
		
		for(int i = 0; i < K; i++)
			cout << " " << pos[i] + 1;
		cout << endl;
	}
}
