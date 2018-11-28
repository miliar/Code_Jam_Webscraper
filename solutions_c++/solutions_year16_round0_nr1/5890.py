#include <vector>
#include <fstream>
#include <string>

using namespace std;

bool count(int n, std::vector<int>& q)
{
	while (n > 0)
	{
		int k = n % 10;
		++q[k];
		n /= 10;
	}
	for (int i = 0; i < q.size(); ++i)
	{
		if (q[i] < 1)
			return false;
	}
	return true;
}

int main()
{
	ifstream in("A-large.in");
	ofstream out("OUT.out");
	int T;
	in >> T;
	int N;
	std::vector<int> q(10);
	for (int i = 0; i < T; ++i)
	{
		for (int k = 0; k < q.size(); ++k)
			q[k] = 0;
		in >> N;
		out << "Case #" << i + 1 << ": ";
		if (N == 0)
		{
			out << "INSOMNIA\n";
			continue;
		}
		for (int j = 1;; ++j)
		{
			if (count(j * N, q))
			{
				out << j * N << "\n";
				break;
			}
		}
	}
}