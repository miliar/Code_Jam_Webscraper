//#include <stdio.h>
//#include <algorithm>
//using namespace std;
//int ary[20] = { 9,8,7,100,5,4,3,2,1}, temp[20];
//int n = 9;
//void merge(int l, int r)
//{
//
//	int mid = (l + r) / 2;
//	if (l < r) {
//		merge(l, mid);
//		merge(mid + 1, r);
//	}
//
//	int i, j, k;
//	k = l, i = l, j = mid + 1;
//	while (i <= mid && j <= r) {
//		if (ary[i] < ary[j]) temp[k++] = ary[i++];
//		else temp[k++] = ary[j++];
//	}
//	while (i <= mid)
//		temp[k++] = ary[i++];
//	while (j <= r)
//		temp[k++] = ary[j++];
//	for (int i = l; i <= r; i++)
//		ary[i] = temp[i];
//
//}
//int hoare(int l, int r)
//{
//	int pivot = ary[l];
//	int i, j;
//	i = l + 1, j = r;
//	while (true) {
//		while (ary[i] < pivot)i++;
//		while (ary[j] > pivot)j--;
//		if (i < j)swap(ary[i], ary[j]);
//		else
//		{
//			swap(ary[j], ary[l]);
//			return j;
//		}
//	}
//
//}
//void quick(int l, int r)
//{
//	if (l < r)
//	{
//		int s = hoare(l, r);
//		quick(l, s);
//		quick(s + 1, r);
//	}
//}
//
//
//
//int main()
//{
//	//merge(0, n - 1);
//	quick(0, n - 1);
//	for (int i = 0; i < n; i++)printf("%d\n", ary[i]);
//	return 0;
//}
#include <stdio.h>
int main()
{
	freopen("B-large.in", "r",stdin);
	freopen("B-large.out", "w", stdout);
	char v;
	int t, cnt = 1;
	scanf("%d", &t);
	while (t--)
	{
		int res = 0;
		char in[101];
		bool chk[101] = { false }; // + : true
		scanf("%s", in);
		int i;
		for (i = 0; in[i] != NULL; i++) {
			if (in[i] == '+')chk[i] = true;
		}

		for (int j = 0; j < i - 1; j++)
			if (chk[j] != chk[j + 1])res++;
		if (!chk[i - 1])res++;
		printf("Case #%d: %d\n", cnt++, res);

	}
	return 0;
}