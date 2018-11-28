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
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int tt,tc;
    RD(tt);
    FOR1(tc,tt)
    {
    	int ori[5][5],aft[5][5];
    	int x,y,i,j;
    	RD(x);
    	FOR1(i,4)
			FOR1(j,4)
				RD(ori[i][j]);
		RD(y);
		FOR1(i,4)
			FOR1(j,4)
				RD(aft[i][j]);
		int ha[17];
		CLR(ha);
		FOR1(i,4)
			ha[ori[x][i]]++;
		FOR1(i,4)
			ha[aft[y][i]]++;
		int flg=0,ind=0;
		FOR1(i,16)
			if (ha[i]==2) flg++,ind=i;
		printf("Case #%d: ",tc);
		if(flg==0) PR("Volunteer cheated!");
		else if (flg==1) PR(ind);
		else PR("Bad magician!");
    }
    return 0;
}
