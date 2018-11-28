#include <fstream>
#include <algorithm>
using namespace std;

const int MAXN = 1005;
int N;
double A[MAXN], B[MAXN];

int opt1()
{
	int idx = 0, cnt = 0;
	for (int i = 0; i < N; i++)
	{
		if (A[i] > B[idx])
		{
			idx++;
			cnt++;
		}
	}

	return cnt;
}

int opt2()
{
	int idx = -1;
	for (int i = 0; i < N; i++)
	{
		idx++;
		while (idx < N && B[idx] < A[i])
			idx++;

		if (idx == N)
			return N - i;
	}

	return 0;
}

int main()
{
	ifstream in ("2014qualsD.in");
	ofstream out ("2014qualsD.out");

	int T;
	in >> T;

	for (int t = 1; t <= T; t++)
	{
		in >> N;
		for (int i = 0; i < N; i++)
			in >> A[i];
		for (int i = 0; i < N; i++)
			in >> B[i];

		sort(A, A + N);
		sort(B, B + N);

		out << "Case #" << t << ": " << opt1() << " " << opt2() << "\n";
	}

	in.close();
	out.close();
	return 0;
}