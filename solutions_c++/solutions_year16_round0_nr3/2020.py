#include <iostream>
#include <fstream>

using namespace std;

int T, N, J;

int main()
{
	ifstream in ("C-large.in");
	ofstream out ("C-large.out");

	int sz, i, j, l, k;
	bool A[33];
	int64_t num[10];

	in >> T;

	i = 1;
	while (i <= T)
	{
		out << "Case #" << i << ": " << endl;

		in >> N >> J;

		sz = N / 2;

		A[sz - 1] = 1;
		A[sz - 2] = 1;
	
		j = 0;
		while (j < sz - 2)
		{
			A[j] = 0;
			j++;
		} 

		while (J--)
		{
			l = 0;
			while (l <= 8)
			{
				num[l] = 0;
				l++;
			}

			i = 0;
			k = 0;
			while (i < sz)
			{
				if (A[i])
					break;
				else
					k++;
	
				i++;
			}

			while (i < sz)
			{
				out << A[i];

				l = 0;
				while (l <= 8)
				{
					num[l] *= (l + 2);
					num[l] += A[i];

					l++;
				}

				i++;
			}

			while (k--)
				out << 0;

			i = 0;
			while (i < sz)
			{
				out << A[i];
				i++;
			}

			out << " ";

			l = 0;
			while (l <= 8)
			{
				out << num[l] << " ";
				l++;
			}

			out << endl;

			j = sz - 2;
			while (j >= 0)
			{
				if (A[j])
				{
					A[j] = 0;
					j--;
				}
				else
				{
					A[j] = 1;
					break;
				}
			}

			if (j == -1)
				break; 
		}

		i++;
	}

	in.close();
	out.close();

	return 0;
}