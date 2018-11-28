#include <algorithm>
#include <cstdio>
#include <vector>
#include <string>
#include <sstream>
#include <set>
#include <map>
using namespace std;

int N;
int M;
int P;

vector<int> get_order(vector<int> v)
{
	if (v.size() <= 2) {
		sort(v.begin(), v.end());
		return v;
	}

	vector<int> a, b, x, y;
	for (size_t i = 0; i < v.size(); i += 2) {
		a.push_back(min(v[i], v[i+1]));
		b.push_back(max(v[i], v[i+1]));
	}

	x = get_order(a);
	y = get_order(b);
	x.insert(x.end(), y.begin(), y.end());

	return x;
}

int main(void)
{
	int tc;
	scanf("%d", &tc);
	for (int T = 1; T <= tc; ++T) {
		scanf("%d %d", &N, &P);
		M = 1 << N;
		vector<int> arr, v;
		for (int i = 0; i < M; ++i)
			arr.push_back(i);
		v = get_order(arr);
		map<int,int> nums;
		for (int i = 0; i < P; ++i)
			nums[v[i]] = 1;
		int biggest = nums.rbegin()->first;
		int in_all = 0;
		while (nums[in_all+1] == 1)
			in_all += 1;
		printf("Case #%d: %d %d\n", T, in_all, biggest);
	}
	return 0;
}
