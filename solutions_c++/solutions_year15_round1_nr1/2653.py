#include <iostream>

using namespace std;

int main()
{
	long T,N,m[10000];
	cin >> T;

	for (int j = 0; j < T; j++)
	{
		cin >> N;
		long e = -1;
		for (long i = 0; i < N; i++)
		{
			cin >> m[i];
			if (i > 0 && (m[i-1] - m[i]) > e)
				e = m[i-1] - m[i];
			//cout << m[i-1] << " " << m[i] << " " << e << endl;
		}

//		cout << e << endl;
		long eat = 0, eat2 = 0;
		for (long i = 0; i < N-1; i++)
		{
			if (m[i+1] < m[i])
				eat+= m[i] - m[i+1];
			eat2 += min(m[i],e);
		}

		cout << "Case #" << (j+1) << ": " << eat << " " << eat2 << endl;
	}

	return 0;
}
