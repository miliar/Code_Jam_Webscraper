#include <cstring>
#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
	vector<double> a, b;
	vector<double>::iterator temp;
	int TC, N,c, ans1,ans2,cnt,ind;
	double tmp;
	scanf("%d", &TC);
	c = 1;
	while (TC--){
		a.clear();
		b.clear();
		scanf("%d", &N);
		ans1 = ans2 = cnt = 0;
		for (int i = 0; i < N; ++i)
		{
			scanf("%lf", &tmp);
			a.push_back(tmp);
		}
		for (int i = 0; i < N; ++i)
		{
			scanf("%lf", &tmp);
			b.push_back(tmp);
		}
		sort(a.begin(), a.end());
		sort(b.begin(), b.end());
		ind = cnt = 0;
		for (int i = 0; i < N; ++i)
		{
			while(b[i] > a[ind] && ind <= N) ind++;
			if (ind < N) {
				cnt++;
				ind++;
			}
			else break;
		}
		ans1 = cnt;
		ind = cnt = 0;
		for (int i = 0; i < N; ++i)
		{
			while(a[i] > b[ind] && ind <= N) ind++;
			if (ind < N) {
				cnt++;
				ind++;
			}
			else break;
		}
		printf("Case #%d: %d %d\n", c++, ans1,N-cnt);
	}
	return 0;
}