#include<fstream>
#include<iostream>
#include<sstream>
#include<iomanip>
#include<string>
#include<vector>
#include<list>
#include<set>
#include<map>
#include<queue>
#include<algorithm>
#include<functional>
#include<numeric>
using namespace std;
typedef pair<int, int> pii;
typedef unsigned long long ull;
typedef long long ll;
#define mp make_pair

//int main13R1APB()
int main()
{
	ifstream fin("B-small-attempt1.in");
	ofstream fout("B-small-attempt1.out");
	//ifstream fin("test.in");
	//ofstream fout("test.out");	

	unsigned int numberOfCases;
	fin >> numberOfCases;

	int N;
	ull E,R;
	vector<ull> v;
	for (unsigned int zz=1; zz<=numberOfCases; ++zz)
	{
		fin >> E >> R >> N;
		v.resize(N);
		for (int i=0; i<N; ++i)
			fin >> v[i];

		int distance = E/R;
		ull extra = E%R, other = R-extra;

		R = min(R,E);
		multiset<ull> x;

		//ull result = R * v[0];
		ull result = 0;
		for (int i=0; i+1<N; ++i)
		{
			x.insert(v[i]);
			if ((i+1)*R <= E)
			{
				result += R * (*x.rbegin());
			}
			else
			{
				result += extra * (*x.rbegin());
				if (x.count(v[i-distance]) > 0)
					x.erase(x.find(v[i-distance]));
				result += other * (*x.rbegin());
			}
		}

		x.insert(v.back());
		result += extra * (*x.rbegin());

		ull best = v.back();
		for (int i=1; i<= distance; ++i)
		{
			result += best * R;
			if (N-i-1 >= 0)
				best = max(best, v[N-i-1]);
		}

		fout << "Case #" << zz << ": " << result << endl;
	}

	return 0;
}