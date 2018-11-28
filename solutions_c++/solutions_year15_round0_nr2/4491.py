#include <stdio.h>
#include <vector>
#include <algorithm>
#include <math.h>
using namespace std;
int n;
const int INF = 987654321;
int sol(vector<int>& arr);
int main()
{
	FILE* in = fopen("B-small-attempt2.in", "r");
	FILE* out = fopen("out.out", "w");
	int t;

	fscanf(in,"%d", &t);
	for (int i = 0; i < t; i++)
	{
		fscanf(in,"%d", &n);
		vector<int>arr(n);
		for (int i = 0; i < n; i++)
			fscanf(in,"%d", &arr[i]);
		fprintf(out,"Case #%d: %d\n", i+1,sol(arr));
	}

	fclose(in);
	fclose(out);
}

int sol(vector<int>& arr) // 현재 상태가 arr일때, 끝나는 최소시간 반환
{
	int size = arr.size();
	bool isend = true;
	for (int i = 0; i < size; i++)
	{
		if (arr[i] > 0)
		{
			isend = false;
			break;
		}
	}

	if (isend)
		return 0;

	vector<int>tmp = arr;
	int idx = -1;
	int max = -1;
	for (int i = 0; i < size; i++)
	{
		tmp[i] = arr[i] - 1;
		if (arr[i] > max && arr[i] > 1)
		{
			max = arr[i];
			idx = i;
		}
	}

	int ret = INF;

	if (idx != -1)
	{
		vector<int>tmp2 = arr;
		vector<int>tmp3 = arr;

		tmp2.push_back(max / 2);
		tmp3.push_back(int(sqrt(max)));
		tmp2[idx] -= max / 2;
		tmp3[idx] -= int(sqrt(max));
		if (max > 1)
			ret = min(ret, 1 + sol(tmp2));
		if (max == 9)
			ret = min(ret, 1 + sol(tmp3));
	}

	ret = min(ret, 1 + sol(tmp));
	return ret;
}