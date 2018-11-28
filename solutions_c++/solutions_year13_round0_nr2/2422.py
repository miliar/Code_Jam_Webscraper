#include <stdio.h>
#include <string.h>
#include <string>
#include <algorithm>
#include <vector>
#include <iostream>
#include <queue>
using namespace std;

int n,m;
int b[110][110];
int p[110][110];

class node
{
	public:
		int i,j,b;
};

bool cmp (const node &a, const node &b)
{
	if (a.b!=b.b)
		return a.b>b.b;
	if (a.i!=b.i)
		return a.i<b.i;
	return a.j<b.j;
}

int main ()
{
	freopen ("B.in","r",stdin);
	freopen ("B.out","w",stdout);
	
	int t,o=1;
	scanf ("%d",&t);

	while (t--)
	{
		int i,j;
		scanf ("%d %d",&n,&m);
		for (i=0;i<n;i++)
			for (j=0;j<m;j++)
				scanf ("%d",&b[i][j]);

		bool f = true;

		vector <node> v;

		for (i=0;i<n;i++)
			for (j=0;j<m;j++)
			{
				node s;
				s.i = i;
				s.j = j;
				s.b = b[i][j];
				v.push_back(s);
			}

		sort (v.begin(),v.end(),cmp);

		for (i=0;i<v.size();i++)
		{
			int mi = v[i].i,mj = v[i].j, mx = v[i].b;
			if (mx == p[mi][mj])
				continue;
			bool cc = true,dc = false;
			for (int k=0;k<n;k++)
				if (b[k][mj]>mx)
				{
					cc = false;
					break;
				}
			if (cc)
			{
				dc = true;
				for (int k=0;k<n;k++)
					p[k][mj] = mx;
			}
			cc = true;
			for (int k=0;k<m;k++)
				if (b[mi][k]>mx)
				{
					cc = false;
					break;
				}
			if (cc)
			{
				dc = true;
				for (int k=0;k<m;k++)
					p[mi][k] = mx;
			}
			if (!dc)
			{
				f = false;
				break;
			}
		}

		/*for (i=0;i<n;i++)
		{
			for (j=0;j<m;j++)
				if (b[i][j]>b[0][j]||b[i][j]>b[n-1][j]||b[i][j]>b[i][0]||b[i][j]>b[i][m-1])
				{
					f = false;
					break;
				}
			if (!f)
				break;
		}*/

		printf ("Case #%d: ",o++);
		if (f)
			printf ("YES\n");
		else
			printf ("NO\n");
	}

	return 0;
}
