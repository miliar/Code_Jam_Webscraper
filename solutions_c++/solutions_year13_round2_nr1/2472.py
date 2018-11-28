#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

typedef long long ll;

ll A, N;
ll motes[101];

// Calculate the cost from the current point
ll cost(int start, ll A)
{
	if (start == N) return 0;
	
	int res=0;
	for (int i=start; i<N; i++)
	{
		if (A <= motes[i])
		{
			// check delete cost
			ll delCost = cost(i+1, A);
			
			// Now add the numbers and see if we can improve this way 
			if ( A != 1)
			{
				ll AA = A;
				int delta = 0;

				while (AA <= motes[i])
				{
					AA += (AA - 1); 
					delta++;
				}

				ll addCost = cost(i+1, AA+motes[i]);

				if (delCost < (addCost+delta))
					res++;
				else
				{
					A = AA;
					A += motes[i]; 
					res+=delta;
				}
			}
			else 
				res++;
		}
		else
			A += motes[i];
	}

	return res;
}

void main() {
	FILE *in = freopen( "Debug\\input.txt", "r", stdin );
	FILE *out = freopen( "Debug\\output.txt", "w", stdout );

	int C;
	scanf("%d",&C);

	for (int test=1;test<=C;test++) {

		cin >> A >> N;

		for (int i=0; i<N; i++)
			cin >> motes[i];

		std::sort(motes, motes+N);

		cout << "Case #" << test << ": " << cost(0, A) << endl;
	}
}
