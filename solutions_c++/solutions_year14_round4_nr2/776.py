#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <cmath>

using namespace std;

void readArray(vector<int>&a, int n)
{
	a.resize(n);
	for (int i = 0; i < n; ++i)
		cin>>a[i];
}

int solve(vector<int>&a)
{
	int res = 0;
	while (a.size() > 2)
	{
		int imin = distance(a.begin(), min_element(a.begin(), a.end()));
		res += min(imin, abs((int)a.size()-1-imin));
		a.erase(a.begin() + imin);
	}
	return res;
}

int main()
{
	int T;
	cin>>T;
	vector<int> res(T);
//	#pragma omp parallel for
	for (int i = 0; i < T; ++i)
	{
		int N;
		vector<int> a;
		cerr<<i<<endl;
		cin>>N;
		readArray(a, N);
		res[i] = solve(a);
	}

	for (int i = 0; i < T; ++i)
		cout<<"Case #"<<(i+1)<<": "<<res[i]<<endl;
	return 0;

}

