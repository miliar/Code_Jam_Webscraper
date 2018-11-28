#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <strstream>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define PB push_back
#define MP make_pair

#define FOR0(i,n) for(i=0;i<(n);++i)
#define FOR1(i,n) for(i=1;i<=(n);++i)
#define FOR(i,l,h) for(i=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)
#define DEBUG(x) cout << #x << "=" << x << endl
#define CLR(x) memset((x),0,sizeof((x)))

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;

void RD(int &x){scanf("%d",&x);}
void RD(double &x){scanf("%lf",&x);}
void RD(int &x,int &y){scanf("%d%d",&x,&y);}
void RD(double &x,double &y){scanf("%lf%lf",&x,&y);}
void RD(int &x,int &y,int &z){scanf("%d%d%d",&x,&y,&z);}
void RD(double &x,double &y,double &z){scanf("%lf%lf%lf",&x,&y,&z);}
void RD(char *s){scanf("%s",s);}

void PR(int x) {printf("%d\n",x);}
void PR(int x,int y) {printf("%d %d\n",x,y);}
void PR(double x) {printf("%.6lf\n",x);}
void PR(char x) {printf("%c\n",x);}
void PR(char x[]) {printf("%s\n",x);}
void PRI(char x[]) {printf("%s",x);}

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("output.txt","w",stdout);
	int r,c,m;
	int tc,tt;
	RD(tt);
	FOR1(tc,tt)
	{
		RD(r,c,m);
		int rev=0;
		if (r>c) {int tmp=r;r=c;c=tmp;rev=1;}
		char mine[100][100];
		CLR(mine);
		int ok=1;
		int i,j;
		printf("Case #%d:\n",tc);
		FOR0(i,r)
			FOR0(j,c)
				mine[i][j]='.';
		if (m==0)
			mine[0][0]='c';
		else if (r==1)
		{
			mine[0][0]='c';
			FOR0(i,m)
				mine[0][c-1-i]='*';
		}
		else if (r==2)
		{
			if (m==r*c-1)
			{
				FOR0(i,r)
					FOR0(j,c)
						mine[i][j]='*';
				mine[0][0]='c';
			}
			else if (m%2==0 && (r*c-m)>=4)
			{
				FOR0(i,2)
					FOR0(j,m/2)
						mine[i][j]='*';
				mine[r-1][c-1]='c';
			}
			else
				ok=0;
		}
		else
		{
			if (m<=(r-2)*(c-2))
			{
				FOR0(i,r-2)
				{
					FOR0(j,c-2)
					{
						mine[i][j]='*';
						m--;
						if (m==0) break;
					}
					if (m==0) break;
				}
				mine[r-1][c-1]='c';
			}
			else
			{

				if (r*c-m==1)
				{
					FOR0(i,r)
						FOR0(j,c)
							mine[i][j]='*';
					mine[r-1][c-1]='c';
				}
				else if (r*c-m==4)
				{
					FOR0(i,r)
						FOR0(j,c)
							mine[i][j]='*';
					mine[r-2][c-1]=mine[r-1][c-2]=mine[r-2][c-2]='.';
					mine[r-1][c-1]='c';
				}
				else if (r*c-m==6)
				{
					FOR0(i,r)
						FOR0(j,c)
							mine[i][j]='*';
					mine[r-3][c-1]=mine[r-3][c-2]=mine[r-2][c-1]=mine[r-1][c-2]=mine[r-2][c-2]='.';
					mine[r-1][c-1]='c';
				}
				else if (r*c-m>=8)
				{
					if (m<=c-2)
					{
						FOR0(i,m)
							mine[0][i]='*';
						mine[r-1][c-1]='c';
					}
					else if (m<=r+c-3)
					{
						FOR0(i,r)
							mine[i][0]='*';
						FOR1(i,m-r)
							mine[0][i]='*';
						mine[r-1][c-1]='c';
					}
					else
					{
						FOR0(i,r)
							FOR0(j,c)
								mine[i][j]='*';
						int cur=c-3;
						m=r*c-m;
						m-=8;
						mine[r-2][c-3]=mine[r-1][c-3]=mine[r-3][c-1]=mine[r-3][c-2]=mine[r-2][c-1]=mine[r-1][c-2]=mine[r-2][c-2]='.';
						mine[r-1][c-1]='c';
						while (m>0)
						{
							if (m==1)
							{
								mine[r-3][cur]='.';
								m--;
							}
							else if (m==2)
							{
								mine[r-1][cur-1]=mine[r-2][cur-1]='.';
								m-=2;
							}
							else if (m==4)
							{
								mine[r-1][cur-1]=mine[r-2][cur-1]='.';
								mine[r-1][cur-2]=mine[r-2][cur-2]='.';
								m-=4;
							}
							else if (m>=3)
							{
								mine[r-3][cur]=mine[r-1][cur-1]=mine[r-2][cur-1]='.';
								m-=3;
								cur--;
							}

						}
					}


				}
				else
					ok=0;
			}

		}
		if (ok)
		{
			if (rev)
			{
				FOR0(i,c)
					for(j=i+1;j<c;j++)
					{
						char tmp;
						tmp=mine[i][j];
						mine[i][j]=mine[j][i];
						mine[j][i]=tmp;
					}
				int tmp;
				tmp=r;
				r=c;
				c=tmp;
			}
			FOR0(i,r)
				PR(mine[i]);
		}
		else
			PR("Impossible");
	}
    return 0;
}
