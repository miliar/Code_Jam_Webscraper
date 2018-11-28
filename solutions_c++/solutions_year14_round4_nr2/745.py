// Codejam2014_1C.cpp : Defines the entry point for the console application.
//


#include "vector"
#include "string"
#include "set"
#include "map"
#include "sstream"
#include "algorithm"
#include "cmath"
#include "cassert"
#include "iostream"
#include "numeric"
#include "fstream"
#ifdef __GNUC__
#include  <tr1/unordered_map>
#define unordered_map tr1::unordered_map
#else
#include <unordered_map>
#endif

using namespace std;


#define F(vec, index) for (int index = 0; index  < vec.size(); ++index)
#define F_S(vec, index, start) for (int index = start; index  < vec.size(); ++index)


//void swapFromTo (vector<int>& copyData, int from, int to)
//{
//}

int main(int argc, char* argv[])
{
	#define int long long
	ifstream cin("in.txt");
	ofstream cout("out.txt");

	int T;
	cin >> T;
	for (int t = 0; t < T; ++t)
	{
		
		
		int N = 0;

		cin >> N;

		vector<int> data(N);

		F(data, i)
		{
			cin >> data[i];
		}

		vector<int> copyData;
		
		//int test = 1000000000;
		int res = 9999999999;
		//for (int i = 0; i < data.size(); ++i)
		{
			copyData = data;
			int currRes = 0;

			int pos = max_element(copyData.begin(), copyData.end()) - copyData.begin();

			/*if (pos > i)
			{
				for (int j = pos; j > i; --j)
				{
					swap(copyData[j], copyData[j - 1]);
					currRes++;
				}
			}
			else if (pos < i)
			{
				for (int j = pos; j < i; ++j)
				{	
					swap(copyData[j], copyData[j + 1]);
					currRes++;
				}
			}*/

			/*int fromArr = i + 1;
			while (fromArr < copyData.size())
			{
				int pos = max_element(copyData.begin() + fromArr, copyData.end()) - copyData.begin();

				for (int j = pos; j > fromArr; --j)
				{	
					swap(copyData[j], copyData[j - 1]);
					currRes++;
				}
				fromArr++;
			}

			fromArr = i - 1;
			while (fromArr >= 0)
			{
				int pos = max_element(copyData.begin(), copyData.begin() + (fromArr + 1)) - copyData.begin();

				for (int j = pos; j < fromArr; ++j)
				{	
					swap(copyData[j], copyData[j + 1]);
					currRes++;
				}
				fromArr--;
			}*/

			int from = 0;
			int to = copyData.size() - 1;
			while (to - from > 0)
			{
				int pos = min_element(copyData.begin() + from, copyData.begin() + (to + 1)) - copyData.begin();
				
				if (to - pos < pos - from)
				{
					for (int j = pos; j < to; ++j)
					{	
						swap(copyData[j], copyData[j + 1]);
						currRes++;
					}
					to--;
				}
				else
				{
					for (int j = pos; j > from; --j)
					{	
						swap(copyData[j], copyData[j - 1]);
						currRes++;
					}
					from++;
				}
				
				
			}


			//  check 

			/*for (int j = i; j < copyData.size() - 1;j++)
			{
				assert(copyData[j] > copyData[j + 1]);
			}
			for (int j = i; j > 0; --j)
			{
				assert(copyData[j] > copyData[j - 1]);
			}*/

			res = min(res, currRes);
		}
	

		
		cout << "Case #" << t + 1 << ": "  << res << endl;
		
		
	}

	return 0;
}
