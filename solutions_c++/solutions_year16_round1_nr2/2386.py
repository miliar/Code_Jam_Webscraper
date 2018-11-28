#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;
int n, m;
#define MAXSIZE 60
typedef struct _node
{
	int arr[MAXSIZE];
}node;
node list[3*MAXSIZE];
int map[MAXSIZE][MAXSIZE];
bool vis[MAXSIZE];

bool cmp(const node &a, const node &b)
{
	for(int i=0; i<n; i++)
	{
		if(a.arr[i]==b.arr[i])
			continue;
		else
			return a.arr[i]<b.arr[i];
	}
}

bool fin;
void sol(int start, int row) // 0 0
{
	if(row==n) // finish
	{
		int pos;
		int cnt = 0;
		/* check col */
		for(int i=0; i<n; i++) // col
		{
			node tmp;
			for(int j=0; j<n; j++)
				tmp.arr[j] = map[j][i];
			bool found = false;
			for(int k=0; k<m && !found; k++) // check all list
			{
				if(vis[k])
					continue;
				bool sm = true;
				for(int j=0; j<n; j++)
				{
					//printf("check %d %d\n", tmp.arr[j], list[k].arr[j]);
					if(tmp.arr[j]!=list[k].arr[j])
					{
						sm = false;
						break; // try next
					}
				}
				if(sm)
				{
					found = true;
					//cout << "found" << endl;
					break;
				}
			}
			if(!found)
				cnt++, pos=i;
			if(cnt>1)
				return;
		}
		if(cnt==1)
		{

			/* debug */
			//for(int i=0; i<n; i++)
			//{
				//for(int j=0; j<n; j++)
					//printf("%d ", map[i][j]);
				//cout << endl;
			//}

			fin = true;
			for(int i=0; i<n; i++)
				printf("%d ", map[i][pos]);
			cout << endl;
		}
		return;
	}

	for(int i=start; i<m && !fin; i++)
	{
		if(vis[i])
			continue;
		/* check upper row */
		bool ok = true;
		for(int j=0; j<n && row>0; j++)
		{
			//printf("compare %d %d\n", map[row-1][j], list[i].arr[j]);
			if(map[row-1][j]>=list[i].arr[j])
			{
				ok = false;
				break;
			}
		}
		if(!ok)
			continue;

		/* accept and try */
		vis[i] = true;
		for(int j=0; j<n; j++) // set map
			map[row][j] = list[i].arr[j];
		sol(i+1, row+1);
		vis[i] = false; // backtrack
	}
}

int main()
{
	int t;
	cin >> t;
	for(int cas=1; cas<=t; cas++)
	{
		scanf("%d", &n);
		m = 2*n-1;
		for(int i=0; i<m; i++)
			for(int j=0; j<n; j++)
				scanf("%d", &(list[i].arr[j]));

		sort(list, list+m, cmp);
		/* debug */
		//for(int i=0; i<m; i++)
		//{
			//for(int j=0; j<n; j++)
				//printf("%d ", list[i].arr[j]);
			//cout << endl;
		//}
		
		memset(vis, false, sizeof vis);
		fin = false;
		printf("Case #%d: ", cas);
		sol(0, 0);
	}
	return 0;
}
