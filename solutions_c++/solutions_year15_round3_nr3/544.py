// K1
// :)

#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <queue>
#include <bitset>
#include <string>
#include <cmath>
#include <iomanip>
#include <set>
#include <map>

#define EPS 1e-8
#define PI 3.141592653589793
#define X first
#define Y second
#define FX(x) fixed << setprecision((x))

using namespace std;

typedef pair<int, int> point;
typedef set<int>::iterator ITR;
const int MAXN = 2e3 + 123;

int main()
{
	int t;
	cin >> t;
	for (int test = 0; test < t; ++test)
	{

		vector <int> vec;
		std::vector<int> buff;
		
		int c, d, v;
		cin >> c >> d >> v;
		for (int i = 0; i < d; ++i){
			int inp;
			buff.clear();
			cin >> inp;
			buff.push_back(inp);
			for (int j = 0; j < vec.size(); ++j){
				buff.push_back(vec[j] + inp);
				//buff.push_back(vec[j] - inp);
			}
			sort(buff.begin(), buff.end());
			unique(buff.begin(), buff.end());
			for (int j = 0; j < buff.size(); ++j)
				vec.push_back(buff[j]);
			sort(vec.begin(), vec.end());
			unique(vec.begin(), vec.end());
		}
		int result = 0;
		for (int i = 1; i <= v; ++i)
		{
			if(binary_search(vec.begin(), vec.end(), i) == false)
			{
				result ++;
				buff.clear();
				buff.push_back(i);
				for (int j = 0; j < vec.size(); ++j){
					buff.push_back(vec[j] + i);
					//buff.push_back(vec[j] - i);
				}
				sort(buff.begin(), buff.end());
				unique(buff.begin(), buff.end());
				for (int j = 0; j < buff.size(); ++j)
					vec.push_back(buff[j]);
				sort(vec.begin(), vec.end());
				unique(vec.begin(), vec.end());
			}
		}
		cout << "Case #" << test+1 << ": " << result << endl;

	}

	return 0;
}