#include <iostream>
#include <cstdlib>
#include <string>
#include <cmath>
#include <algorithm>
using namespace std;
void QuickSort(long L, long H);
void inp();
long T, N;
long i, j,t;
double a[1500], b[1500], c[3000];
long d[3000];
void solve1();
void solve2();
int main()
{
    freopen("D-large.in","r",stdin);
    freopen("D.out","w",stdout);
	cin >> T;
	for (i = 1; i <= T; i++)
	{
		inp();
		QuickSort(1, t);
		/*for (i = 1; i <= t; i++)
		{
            cout << c[i] << " " <<endl;
            }*/
        cout<<"Case #"<<i<<": ";
		solve1();
		solve2();
		
	}
	//system("pause");
	return 0;
}
void QuickSort(long L, long H)
{
	long i, j;
    double x;
	i = L;
	j = H;
	x = c[(L + H) / 2];
	do
	{
		while (c[i] < x) i++;
		while (c[j] > x) j--;
		if (i <= j)
		{
			swap(c[i], c[j]);
			swap(d[i], d[j]);
			i++;
			j--;
		}
	} while (i <= j);
	if (L < j) QuickSort(L, j);
	if (i < H) QuickSort(i, H);
}
void inp()
{
     t = 0;
     memset(a,0,sizeof(a));
     memset(b,0,sizeof(b));
     memset(c,0,sizeof(c));
     memset(d,0,sizeof(d));
	cin >> N;
	for (j = 1; j <= N; j++)
	{
		cin >> a[j];
		t++;
		c[t] = a[j];
		d[t] = 1;
	}
	for (j = 1; j <= N; j++)
	{
		cin >> b[j];
		t++;
		c[t] = b[j];
		d[t] = 2;
	}
	//cout << "t = " << t << endl;
}
void solve1()
{
	long N1, N2;
	N1 = N2 = 0;
	long ans1 = N;
	for (j = 1; j <= 2 * N; j++)
	{
		if (d[j] == 2) N2++;
		if (d[j] == 1)
		{
			N1++;
			if (N2 < N1) {ans1--; N1--;}
		}
	}
	cout << ans1 << " ";
}
void solve2()
{
	long N1, N2;
	N1 = N2 = 0;
	long ans2 = 0;
	for (j = 2 * N; j >= 1; j--)
	{
		if (d[j] == 2) N2++;
		if (d[j] == 1)
		{
			N1++;
			ans2 = max(ans2,N1-N2);
		}
	}
	cout << ans2 << endl;
}
