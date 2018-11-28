//#include <iostream>
//#include <cstdio>
//#include <cstring>
//#include<algorithm>
//#include<string>
//#pragma warning(disable:4996)
//using namespace std;
//int a[10000];
//
//int main(){
//	freopen("input.txt", "r", stdin);
//	freopen("B-small.out", "w", stdout);
//	int T;
//	cin >> T;
//	for (int o = 1; o <= T; o++){
//		int n, m;
//		cin >> n >> m;
//		memset(a, 0, sizeof(a));
//		for (int j = 0; j < n; ++j)
//		{
//			int x;
//			scanf("%d", &x);
//			a[x]++;
//		}
//		int count = 0;
//		for (int j = 0; j <= m; ++j)
//		{
//			while (a[j]>0)
//			{
//				for (int k = m - j; k >= j; --k)
//				{
//					if (a[k] > 0)
//					{
//						a[j]--;
//						a[k]--;
//						++count;
//					}
//					if (a[j] <= 0)break;
//				}
//			}
//			
//		}
//		printf("Case #%d: %d\n", o, count);
//	}
//}
