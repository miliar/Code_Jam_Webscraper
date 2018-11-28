#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char const *argv[])
{
	int T;

	cin >> T;

	vector<int> naomy;
	vector<int> ken;

	for (int k = 0; k < T; ++k)
	{
		int N;
		cin >> N;

		naomy.clear();
		ken.clear();

		naomy.resize(N);
		ken.resize(N);

		for (int i = 0; i < N; ++i)
		{
			double in;
			cin >> in;
			in *= 1000;

			naomy[i] = in;
		}

		for (int i = 0; i < N; ++i)
		{
			double in;
			cin >> in;
			in *= 1000;

			ken[i] = in;
		}

		sort(naomy.begin(), naomy.end());
		sort(ken.begin(), ken.end());

		int nw=0, dw=0;

		int sn=0,en=N-1, sk=0,ek=N-1;

		while ((!(sn > en)) && (!(sk > ek)))
		{
			if (naomy[en] > ken[ek])
			{
				en--;
				sk++;
				nw++;
			}
			else
			{
				ek--;
				en--;
			}
		}

		sn=0;
		en=N-1;
		sk=0;
		ek=N-1;

		while ((!(sn > en)) && (!(sk > ek)))
		{
			if (naomy[en] > ken[ek])
			{
				en--;
				ek--;
				dw++;
			}
			else
			{
				ek--;
				sn++;
			}
		}

		cout << "Case #" << k+1 << ": " << dw << " " << nw << '\n';
	}
	return 0;
}