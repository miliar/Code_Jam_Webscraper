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
#include <vector>
#include <math.h>
#define ll long long
using namespace std;
vector <ll> res;
ll n, k, pcnt;

bool isprime(ll v,vector <ll>& vec)
{
	if (v == 2)return true;
	if (v == 3)return false;
	if (!(v % 2)) {
		vec.push_back(2);
		return false;
	}
	for (ll i = 3; i <= sqrt(v); i += 2)
		if (!(v%i)) {
			vec.push_back(i);
			return false;
		}
	return true;
}
void PRINT(const vector <ll>&vec)
{
	for (int i = n - 1; i >= 0; i--)
	{
		if (vec[0] & (1 << i))printf("1");
		else printf("0");
	}
	printf(" ");
	for (int i = 1; i < 10; i++)
	printf("%lld ", vec[i]);
	printf("\n");
}
void dfs(ll v, int cnt)
{
	if (pcnt >=k)return;
	if (n-1 == cnt) {
		int i;
		vector <ll> val;
		val.push_back(v);
		for (i = 2; i <= 10; i++)
		{
			ll tp = 0;
			for (int j = 0; j < n; j++)
			{	
				if (v&(1 << j))tp += pow(i, j);
			}	
			if (isprime(tp,val))break;
		}
		if (i > 10) {
			pcnt++;
			PRINT(val);
		}
		return;
	}
	dfs(v + (1 << cnt), cnt + 1);
	dfs(v, cnt + 1);

}

int main()
{
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("C-small-attempt1.out", "w", stdout);
	int t, cnt = 1;
	scanf("%d", &t);
	while (t--)
	{
		pcnt = 0;
		scanf("%lld %lld", &n, &k);
		ll v = (1 << (n - 1));
		printf("Case #%d:\n",cnt++);
		dfs(v, 0);
	}
	return 0;
}