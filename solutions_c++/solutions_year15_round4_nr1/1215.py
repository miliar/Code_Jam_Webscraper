#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <mutex> 
#include <bitset>
#include <set>
#include <string>
#include <thread>
#include <string.h>
#include <math.h>
#include <fstream>
using namespace std;
#define re return
#define LL long long
#define EPS 0.00000000001
#define MOD 1000000000
#define INF 2000000000
#define TT 104
std::mutex mtx;
int T, nmtx = 0;
#define OK(); for(;;){mtx.lock();nmtx++;mtx.unlock();break;}

#define H 110
typedef struct{
	int r, c, ans;
	char a[H][H];
}tres;
tres res[TT];


typedef struct{
	int c, r; bool vert; bool left; bool down;
}tall;
void solve(int t)
{
	tall all[4 * H]; memset(&all, 0, sizeof(tall) * 4 * H);
	int sum = 0;
	int cntH[H], cntV[H];
	memset(&cntH, 0, sizeof(int)*H);
	memset(&cntV, 0, sizeof(int)*H);
	for (int ri = 0; ri < res[t].r; ++ri)
	{
		bool bOK = false; int ilast = -1;
		for (int ci = 0; ci < res[t].c; ++ci) if (res[t].a[ri][ci] != '.')
		{
			ilast = ci;
			cntH[ci] += 1;
			if (res[t].a[ri][ci] == '<' && !bOK) {
				all[sum].r = ri;
				all[sum].c = ci;
				all[sum].vert = false;
				all[sum].left = true;
				sum += 1;
			}
			bOK = true;
		}
		if (ilast != -1 && res[t].a[ri][ilast] == '>') {
			all[sum].r = ri;
			all[sum].c = ilast;
			all[sum].vert = false;
			all[sum].left = false;
			sum += 1;
		}
	}
	for (int ci = 0; ci < res[t].c; ++ci)
	{
		bool bOK = false; int ilast = -1;
		for (int ri = 0; ri < res[t].r; ++ri) if (res[t].a[ri][ci] != '.')
		{
			cntV[ri] += 1;
			ilast = ri;
			if (res[t].a[ri][ci] == '^' && !bOK)
			{
				all[sum].r = ri;
				all[sum].c = ci;
				all[sum].vert = true;
				all[sum].down = false;
				sum += 1;
			}
			bOK = true;
		}
		if (ilast != -1 && res[t].a[ilast][ci] == 'v')
		{
			all[sum].r = ilast;
			all[sum].c = ci;
			all[sum].vert = true;
			all[sum].down = true;
			sum += 1;
			
		}
	}
	for (int ci = 0; ci < res[t].c; ++ci)
	{
		for (int ri = 0; ri < res[t].r; ++ri) if (res[t].a[ri][ci] != '.')
		{
			if (!(cntV[ri] > 1 || cntH[ci] > 1))
			{
				res[t].ans = -1;
				return;
			}
		}
	}
	res[t].ans = sum;
}

int main()
{
	//freopen("A.in", "rt", stdin);
	freopen("A-large.in", "rt", stdin);
	freopen("A.out", "wt", stdout);

	cin >> T;
	for (int t = 0; t < T; ++t) {
		cin >> res[t].r >> res[t].c;
		for (int i = 0; i < res[t].r; ++i)
		{
			cin >> res[t].a[i];
		}

		solve(t);
	}

	for (int t = 0; t < T; ++t)
	{
		cout << "Case #" << t + 1 << ": ";
		if (res[t].ans >=0)
			cout<< res[t].ans;
		else cout << "IMPOSSIBLE";
		cout << endl;
	}
	re 0;
}