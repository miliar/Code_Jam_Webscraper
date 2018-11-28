#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <set>
#include <list>
#include <map>
#include <deque>

using namespace std;

int t,T;
ifstream ein;
ofstream aus;

void runtestcase()
{
	int N, K;
	ein >> N >> K;
	vector<int> a(1001,0);
	for (int i=K-1; i<N;i++)
	{
		int Si;
		ein >> Si;
		a[i] = Si;
		for (int k=1;k<K;k++)
			a[i] -= a[i-k];
	}
	vector<int> mn(K,0);
	vector<int> mx(K,0);
	vector<int> l(K,0);
	int smn=0;
	for (int k=0;k<K;k++)
	{
		mn[k] = a[k];
		mx[k] = a[k];
		for (int i=k;i<N;i+=K)
		{
			mn[k] = min(mn[k], a[i]);
			mx[k] = max(mx[k], a[i]);
		}
		smn += mn[k];
		l[k] = mx[k]- mn[k];
	}
	int sk = ((smn % K) + K ) % K;
	sort(l.begin(),l.end());
	int re = l[K-1];
	int sl = sk;
	for (int k=0;k<K;k++)
	{
		sl += l[k];
	}
	if (sl > re * K)
		re++;
	aus << re;
}

void main()
{
	ein.open("B-large.in");
	aus.open("ausgabe.txt");

	ein >> T;
	for (t = 1; t <= T; t++)
	{
		printf("%d\n", t);
		aus << "Case #" << t << ": ";
		runtestcase();
		aus << endl;
	}

	aus.close();
	ein.close();
}