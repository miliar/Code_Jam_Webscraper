#include <fstream>

using namespace std;

int main()
{
	ifstream in ("A.in");
	ofstream out ("A.out");
	int T;
	in >> T;
	for (int t = 1; t <= T; t++)
	{
		int A, B, K;
		in >> A >> B >> K;
		long long int ans = 0;
		for (int i = 0; i < A; i++)
		{
			for (int j = 0; j < B; j++)
			{
				if (int(i & j) < K)
					ans++;
			}
		}
		out << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}
