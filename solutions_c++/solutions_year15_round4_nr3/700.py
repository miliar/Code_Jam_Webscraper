#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <mutex> 
#include <bitset>
#include <set>
#include <map>
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
#define TT 30
std::mutex mtx;
int T, nmtx = 0;
#define OK(); for(;;){mtx.lock();nmtx++;mtx.unlock();break;}

typedef struct{
	int a[1002];
	int b[1002];

	int s[21][12];
	int cnt[21];
	int n;
	int ans;
	int val[21];

	int m[8000], ncnt;
}tres;
tres res[TT];

#define M 10
#define N 100008


void solve(int t)
{
	int all = 1 << (res[t].n - 1);

	if (all < 1)all = 1;
	res[t].ans = 1000000;
	res[t].val[0] = 1;
	res[t].val[1] = 2;
	int ncur = res[t].ncnt + 1;
	for (int r = 0; r < all; ++r) {
		for (int r1 = r, cur = 2; cur < res[t].n; r1 >>= 1, ++cur)
		{
			res[t].val[cur] = 1 + (r1 & 1);
		}
		
		memset(&res[t].m, 0, sizeof(int) * ncur);
		for (int i = 0; i < res[t].n; ++i)
		{
			for (int j = 0; j < res[t].cnt[i]; ++j)
			{
				int toFind;
				if (i >= 2)toFind = res[t].s[i][j];
				else if (i == 0)toFind = res[t].a[j];
				else toFind = res[t].b[j];

				res[t].m[toFind] |= res[t].val[i];
			}
		}
		int sum = 0;
		for (int i = 0; i < ncur; ++i)
		{
			if (res[t].m[i] == 3)
			{
				sum += 1;
			}
		}
		if (sum < res[t].ans)
			res[t].ans = sum;
	}
	OK();
}
#define KH 5101000
char tmp[KH];
#define inputFile "C-small-attempt2.in"
int main()
{
	freopen(inputFile, "rt", stdin);
	//freopen("B-small-attempt0.in", "rt", stdin);
	freopen("B.out", "wt", stdout);

	cin >> T;
	for (int t = 0; t < T; ++t) {
		cin >> res[t].n;
		cin.getline(tmp, KH);
		for (int i = 0; i < res[t].n; ++i)
		{
			cin.getline(tmp, KH);
			int slen = strlen(tmp);
			res[t].cnt[i] = 1;
			for (int j = 0; j < slen; ++j)if (tmp[j] == ' ')res[t].cnt[i] += 1;
			memset(tmp, 0, slen + 2);
		}
	}
	ifstream fin(inputFile);
	fin >> T;
	//freopen(inputFile, "rt", stdin);
	map<string, int>cur;int ncur = 0;
	map<string, int>::iterator it;
	for (int t = 0; t < T; ++t)
	{
		cur.clear();
		ncur = 0;
		fin >> res[t].n;

		for (int i = 0; i < res[t].n; ++i)
		{
			for (int j = 0; j < res[t].cnt[i]; ++j) {
				string h;
				fin >> h;
				int me;
				it = cur.find(h);
				if (it != cur.end()) {
					me = it->second;
				}
				else {
					me = ncur;
					cur.insert(make_pair(h, ncur));
					ncur++;
				}

				if (i == 0) {
					res[t].a[j] = me;
				}
				else if (i == 1)
				{
					res[t].b[j] = me;
				}
				else {
					res[t].s[i][j] = me;
				}
			}
		}
		res[t].ncnt = ncur;
		thread * ÒThread = new thread(std::bind(&solve, t));
	}

	for (; nmtx < T;) { this_thread::sleep_for(std::chrono::milliseconds(200)); }

	for (int t = 0; t < T; ++t)
	{
		cout << "Case #" << t + 1 << ": " << res[t].ans;
		cout << endl;
	}
	re 0;
}