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
//
//
//

#include <stdio.h>

int main()
{
	int chk;
	int n, t, i;
	freopen("A-small-attempt1.in", "r",stdin);
	freopen("A-small-attempt1.out", "w", stdout);
	scanf("%d", &t);
	int cnt = 1;
	while (t--)
	{
		chk = 0;
		scanf("%d", &n);
		if (n == 0) {
			 printf("Case #%d: INSOMNIA\n", cnt++);
			continue;
		}
		for (i = 1; i*n <= n * 100; i++)
		{
			int temp = i*n;
			while (temp)
			{
				chk |= 1 << (temp % 10);
				temp /= 10;
			}
			if (chk == (1 << 10) - 1)break;
		}
		printf("Case #%d: ", cnt++);
		if (chk == (1 << 10) - 1)printf("%d\n", n*i);
		else printf("INSOMNIA\n");

	}
	return 0;
}