#include <iostream>
#include <cmath>
using namespace std;

bool SqrtHasRemainer(int X, int sqrtX)
{
	return (X > (sqrtX*sqrtX));
}

int main()
{
	// 1 - sqrt(1000), i.e., 1 - 31
	const int P_MAX = 5;
	int palindomes[P_MAX] = { 1, 2, 3, 11, 22 };
	//
	int A, B, T;
	cin >> T;
	for(int t = 1; t <= T; t++)
	{
		cin >> A >> B;
		// looking for "squarable" palindomes on square-rooted boundaries
		int sqrtA = (int)sqrt((float)A);
		if(SqrtHasRemainer(A, sqrtA)) sqrtA += 1;	// integer round-off has to be resolved!
		A = sqrtA;
		B = (int)sqrt((float)B);	// integer round-off does not bother me here, on the countrary - it is good :)
		//
		int P = 0;
		for(int i = 0; i < P_MAX; i++)
			if((palindomes[i] >= A) && (palindomes[i] <= B))
				P += 1;
		//
		cout << "Case #" << t << ": " << P << "\n";
	}
	cout << flush;
	return 0;
}