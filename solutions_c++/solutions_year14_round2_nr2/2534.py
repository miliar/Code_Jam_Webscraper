#include <vector>
#include <queue>
#include <iostream>

using namespace std;
int case_number;

#define REP( i, N) for( int i = 0; (i < N); i ++ )

void main2()
{
	int A, B , K;
	scanf_s("%d %d %d", &A, &B, &K);

	int count = 0;
	REP(i, A)
		REP(j, B)
	{
			if ( (i & j) < K)
				count++;
	}
	cout << "Case #" << ++case_number << ": " << count << endl;
}

int main()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; i++)
		main2();
	cin >> T;
}