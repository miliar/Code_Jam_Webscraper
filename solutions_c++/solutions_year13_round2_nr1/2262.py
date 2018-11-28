#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

struct Para
{
	int wartosc;
	int koszt;

	Para(int wartosc = 0, int koszt = 0) : wartosc(wartosc), koszt(koszt) {}

	bool operator<(const Para& p) const
	{
		return wartosc < p.wartosc;
	}
};

int main()
{
	int T,A,N,tmp;
	scanf("%d\n", &T);

	for(int ile = 1 ; ile <= T ; ++ile)
	{
		scanf("%d %d\n", &A, &N);
		vector<Para> vec;
		for(int j = 0 ; j < N ; ++j)
		{
			scanf("%d", &tmp);
			vec.push_back(Para(tmp));
		}

		sort(vec.begin(), vec.end());

		if(A == 1)
		{
			printf("Case #%d: %d\n", ile, N);
			continue;
		}

		for(int a = 0 ; a < N ; ++a)
		{
			while(A <= vec[a].wartosc)
			{
				A = 2*A - 1;
				++vec[a].koszt;
			}
			A += vec[a].wartosc;
		}

		int k = 0;
		int i = 0;
		for(; i < N ; ++i)
		{
			if(!(vec[i].koszt < N - i )) break;
			
				k += vec[i].koszt;
		}

		k += N - i;

		printf("Case #%d: %d\n", ile, k);
	}
	
	return 0;
}
