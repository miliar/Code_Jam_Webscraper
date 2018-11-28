//Aleksander Łukasiewicz
#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;

#define x first
#define y second

const int MAXN = 100;

int t, n, m;
int lawn[MAXN + 3][MAXN + 3];
int rows[MAXN + 3], columns[MAXN + 3];
pair< int, pair<int,int> > fields[MAXN*MAXN + 3];

inline void read()
{
    scanf("%d %d", &n, &m);
    for(int i=0; i<n; i++) for(int j=0; j<m; j++)
	scanf("%d", &lawn[i][j]), fields[i*m+j] = make_pair(lawn[i][j], make_pair(i,j));

    memset(rows, 0, (n+1)*sizeof(int));
    memset(columns, 0, (m+1)*sizeof(int));
}

int main()
{
    scanf("%d", &t);
    for(int pp=1; pp<=t; pp++)
    {
	read();
	sort(fields, fields+n*m);
	bool spr=true;
	for(int i=n*m-1; i>=0; i--)
	{
	    if(rows[ fields[i].y.x ]>fields[i].x && columns[ fields[i].y.y ]>fields[i].x)
	    {
		spr = false; break;
	    }
	    rows[ fields[i].y.x ] = rows[ fields[i].y.x ]==0 ? fields[i].x : rows[ fields[i].y.x ];
	    columns[ fields[i].y.y ] = columns[ fields[i].y.y ]==0? fields[i].x : columns[ fields[i].y.y ];
	}

	printf("Case #%d: ", pp);
	puts(spr ? "YES" : "NO");
    }

return 0;
}