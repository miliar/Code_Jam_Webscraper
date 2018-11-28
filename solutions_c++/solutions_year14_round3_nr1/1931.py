#include <vector>
#include <queue>
#include <iostream>

using namespace std;

typedef vector<int> vi;
typedef vi::iterator vit;

using namespace std;
int case_number;

#define REP( i, N) for( int i = 0; (i < N); i ++ )

void main2()
{
	int P, Q;
	scanf_s("%d/%d", &P, &Q );

	double fraction = (double)P / (double)Q;

	long double sum_of_P = fraction * 2;
	int level = 1;
	
	while ((level < 41) && (sum_of_P < 1.0 ))
	{
		sum_of_P *= 2;
		level++;
	}
	int ans = level;
	if (level < 41)
	{
		while (level < 40 )
		{
			sum_of_P *= 2;
			level++;
		}

		long double fract = (sum_of_P - (long long)sum_of_P);

		if ( (fract == 0) && sum_of_P <= 1099511627775 )
			cout << "Case #" << ++case_number << ": " << ans << endl;
		else
			cout << "Case #" << ++case_number << ": " << "impossible" << endl;
	}
	
	else
		cout << "Case #" << ++case_number << ": " << "impossible" << endl;
}

int main()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; i++)
		main2();
	cin >> T;
}