# include <cstdio>
# include <queue>

using namespace std;

int n;
int a[1024];
priority_queue <int> pq, pq2;

void read ()
{
	int i, p;
	scanf ("%d", &n);
	for (i = 0; i < n; i ++)
		scanf ("%d", &a[i]);

}

int ans;

void solve ()
{
	int i, curr = 0, p = 0, t;
	for (i = 0; i < n; i ++)
		pq.push (a[i]);
	while (!pq.empty ())
	{
		t = pq.top ();
		pq.pop ();
		ans = min (ans, t + p + curr);
		///printf ("%d %d\n", t, p);
		/**if (t & 1 && t != 1)
		{
			curr ++;
			pq2.push (t - 1);
			while (!pq.empty ())
			{
				t = pq.top ();
				pq.pop ();
				pq2.push (t - 1);
			}
			while (!pq2.empty ())
			{
				t = pq2.top ();
				pq2.pop ();
				pq.push (t);
			}
			continue;
		}**/
		if (t <= 1)
			continue;
		p ++;
		pq.push (t / 2 + t % 2);
		pq.push (t / 2);
	}
}

void solve2 ()
{
	int i, curr = 0, p = 0, t, k;
	for (k = 1; k <= 1024; k ++)
	{
		for (i = 0; i < n; i ++)
			if (a[i] > k)
				pq.push (a[i]);
		p = 0;
		while (!pq.empty ())
		{
			t = pq.top ();
			pq.pop ();
			
			p += t / k;
			if (t % k == 0)
				p --;
		}
		ans = min (ans, k + p);
	}
}

int main ()
{
	int i, t, t1;
	scanf ("%d", &t);
	for (t1 = 1; t1 <= t; t1 ++)
	{
		read ();
		ans = 1e9;
		solve ();
		solve2 ();	
		printf ("Case #%d: ", t1);
		printf ("%d\n", ans);
	}
}

