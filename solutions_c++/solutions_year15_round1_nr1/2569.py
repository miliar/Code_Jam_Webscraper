#pragma warning(disable:4996)
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>


using namespace std;
typedef long long LL;

int comp(const void * elem1, const void * elem2)
{
	int f = *((int*)elem1);
	int s = *((int*)elem2);
	if (f > s) return  1;
	if (f < s) return -1;
	return 0;
}
int main() {
	FILE *fin = freopen("A-large.in", "r", stdin);
	assert(fin != NULL);
	FILE *fout = freopen("out.txt", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++){
		cout << "Case #" << t << ": ";
		int n;
		cin >> n;
		LL *arrayX = new LL[n];
		LL *arrayX0 = new LL[n];
		LL *arrayY = new LL[n];
		for (int i = 0; i < n; i++) cin >> arrayX[i];
		for (int i = 0; i < n; i++) arrayX0[i] = arrayX[i];
		for (int i = 0; i < n - 1; i++)  arrayY[i] = arrayX[i + 1] - arrayX[i];
		qsort(arrayX, n, 8, comp);
		qsort(arrayY, n-1, 8, comp);
		LL k = arrayY[0];
		LL ret1 = 0;
		LL ret2 = 0;

		for (int i = 0; i < n-1; i++){
			if (arrayY[i] < 0 )
			ret1 += arrayY[i] ;
		
			if (k < 0)
			{
				if (arrayX0[i] < -1 * k)
				{
					ret2 += arrayX0[i];
				}
				else{
					ret2 += (-k);
				}
			}
			else{
				ret2 = 0;
			}

		}
		ret1 = -1 * ret1;
		cout << ret1 <<" "<<ret2<< endl;
		delete[] arrayX;
		delete[] arrayY;
	}

	exit(0);
}
