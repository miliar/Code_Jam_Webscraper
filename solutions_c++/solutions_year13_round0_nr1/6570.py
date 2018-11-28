/*
	Name: ONUR YILDIZ
 	School: Fatih Koleji
	Country: Turkiye
*/

#include <iostream>
#include <algorithm>
#include <cstdio>
#include <ctime>
#include <cstdlib>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <cmath>
#include <map>
#include <set>
#include <string>
#include <cstring>

#define p_q priority_queue
#define SFOR(i,a) for(i=a.begin();i!=a.end();++i)
#define VFOR(i,a) for(i=0;i<a.size();i++)
#define FOR(a,b,c) for(a=b;a<=(int)c;a++)
#define ROF(a,b,c) for(a=b;a>=(int)c;a--)
#define FILL(a,b) memset(a,b,sizeof(a))
#define Vall(v) v.begin(),v.end()
#define Aall(A,N) A+1,A+N+1
#define pii pair < int , int > 
#define pll pair <  ll ,  ll >
#define pdd pair < dbl , dbl >
#define vii vector < pii >
#define si set < int >
#define vi vector< int >
#define dbl double
#define ll long long
#define INF (int)1e9
#define LINF (ll)1e16
#define sqr(a) ((a)*(a))
#define mkp make_pair
#define pb push_back
#define f first
#define s second
#define eps 1e-6
#define b(a,b) ( (a)-(b) > +eps)
#define k(a,b) ( (a)-(b) < -eps)
#define e(a,b) ( k(a,b) && k(b,a) )

using namespace std;

int N,__T;
char T[5][5];
int yon[4][2]={{1,0},{0,1},{1,1},{-1,1}};

bool ol(char a,char hed)
{
	if(a=='T' || a==hed) return 1;
	return 0;
}

int main()
{
	int i,j,q,a,b,k,y;
	bool xx,yy;
	string str;
	scanf(" %d",&__T);
	FOR(q,1,__T)
	{
		//CLEAR
		FOR(i,1,4)
			scanf("%s",T[i]+1);
		
		str="Draw";
		FOR(i,1,4)
			FOR(j,1,4)
			{
				if(T[i][j]=='.')
					str="Game has not completed";
				
				FOR(y,0,3)
				{
					xx=yy=1;
					if(!ol(T[i][j],'X')) xx=0;
					if(!ol(T[i][j],'O')) yy=0;
					a=i; b=j;
					FOR(k,1,3)
					{
						a+=yon[y][0];
						b+=yon[y][1];
						if(!ol(T[a][b],'X')) xx=0;
						if(!ol(T[a][b],'O')) yy=0;
					}
					if(xx)
					{
						str="X won";
						goto d;
					}
					if(yy)
					{
						str="O won";
						goto d;
					}
				}
			}
		goto d;
		if(0)
		{
d:
			printf("Case #%d: %s\n",q,str.c_str());
		}
	}

	return 0;
}
