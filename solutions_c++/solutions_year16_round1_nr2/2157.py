#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>
#include <functional>
#include <vector>
using namespace std;

int main()
{
	ifstream in("in.in");
	ofstream write;
	vector <int> vec;
	write.open("out.expect");
	int T, N,a,max;

		in >> T;
		for (int i = 0; i < T; i++)
		{
			in >> N;
			vec.clear();
			max = 0;
			int arr[25000] = { 0 };
			for (int j = 0; j < N*N*2-N; j++)
			{
				
					in >> a;
					if (max <= a)
					{
						max = a;
					}
					arr[a]++;
				
			}
			for (int j = 1; j <= max; j++)
			{
				if (arr[j] % 2 == 1)
				{
					vec.push_back(j);
				}
			}
			sort(vec.begin(), vec.end());
			cout << "Case #" << i + 1 << ": ";
			write << "Case #" << i + 1 << ": ";
			for (int j = 0; j < vec.size(); j++)
			{
				cout << vec[j] << " ";
				write << vec[j] << " ";
			}
			cout << endl;
			write << endl;

		}

	return 0;
}