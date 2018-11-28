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
#include <bitset>
#include <list>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define PB push_back
#define MP make_pair

#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,l,h) for(i=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;

int T,N,M;
char str[105][105];
bool ok[105][105][5];

int getD(char c){
	if (c=='<')
		return 0;
	if (c=='^')
		return 1;
	if (c=='>') 
		return 2;
	if (c=='v') 
		return 3;
	return 4;
}
int main()
{
	freopen("i.txt","r",stdin);
	scanf("%d",&T);
	for (int testcase=1;T--;testcase++){
		printf("Case #%d: ",testcase);
		scanf("%d%d",&N,&M);
		for (int i=0;i<N;i++)
			scanf("%s",str[i]);
		memset(ok,false,sizeof(ok));
		for (int i=0;i<N;i++)
			for (int j=0;j<M;j++){
				if (j>0 && (getD(str[i][j-1])!=4 || ok[i][j-1][0]))
					ok[i][j][0]=true;
				if (i>0 && (getD(str[i-1][j])!=4 || ok[i-1][j][1]))
					ok[i][j][1]=true;
			}
		for (int i=N-1;i>=0;i--)
			for (int j=M-1;j>=0;j--){
				if (j+1<M && (getD(str[i][j+1])!=4 || ok[i][j+1][2]))
					ok[i][j][2]=true;
				if (i+1<N && (getD(str[i+1][j])!=4 || ok[i+1][j][3]))
					ok[i][j][3]=true;
			}
		int ans=0;
		bool good=true;
		for (int i=0;i<N;i++)
			for (int j=0;j<M;j++){
				if (getD(str[i][j])==4) continue;
				bool mark[4];
				bool can=false;
				for (int d=0;d<4;d++){
					mark[d]=ok[i][j][d];
					if (mark[d])
						can=true;
				}
				if (!can)
					good=false;
				if (!mark[getD(str[i][j])])
					ans++;
			}
		if (!good)
			puts("IMPOSSIBLE");
		else
			printf("%d\n",ans);
	}
        return 0;
}
