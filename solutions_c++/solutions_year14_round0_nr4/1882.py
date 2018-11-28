/* bhupkas */

using namespace std;

#include "bits/stdc++.h"

double A[1004];
double B[1004];

#define EPS 1e-9

int main()
{
	int t;
	cin >> t;
	for(int tc = 1 ; tc <= t ; tc++)
	{
		int n;
		cin >> n;
		for(int i = 0 ; i < n ; ++i)	scanf("%lf",&A[i]);
		for(int i = 0 ; i < n ; ++i)	scanf("%lf",&B[i]);
		sort(A,A+n);
		sort(B,B+n);
		int l,k;
		l = k = 0;
		int re1,re2;
		re1 = re2 = 0;
		while(l < n && k < n)
		{
			if(A[l] < B[k])	l++,k++,re1++;
			else	k++;
		}		
		l = k = 0;
		while(l < n && k < n)
		{
			if(B[l] + EPS < A[k])	l++,k++,re2++;
			else	k++;
		}
		printf("Case #%d: ",tc);
		cout << re2 << " " << n - re1 << endl;
	}
	return 0;
}
