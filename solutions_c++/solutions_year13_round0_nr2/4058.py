//Bismillahir Rahmanir Rahim
//#pragma warning(disable:4786)
//#pragma comment(linker,"/STACK:514850816")
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <climits>
#include <string>
#include <sstream>
#include <queue>
#include <stack>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <algorithm>
using namespace std;

#define sz 101
int in[sz][sz];
int row[sz];
bool rchk[sz];

int main(){
	freopen("G:\\Coding\ 4\ Contest\\contests\\codejam13\\B-large.in","r",stdin);
	freopen("G:\\Coding\ 4\ Contest\\contests\\codejam13\\B-large.out","w",stdout);
	int i, t, cas, j, n, m, mn, mx;
	bool f;
	scanf("%d",&t);
	for(cas=1;cas<=t;cas++){
		scanf("%d %d",&n,&m);
		for(i=0;i<n;i++)for(j=0;j<m;j++)scanf("%d",&in[i][j]);
		memset(rchk,0,sizeof(rchk));
		for(i=0;i<n;i++){
			mx = -1;
			for(j=0;j<m;j++){
				if(mx < in[i][j])mx = in[i][j];
			}
			row[i] = mx;
		}
		f = 1;
		for(i=0;i<m;i++){
			mx = -1;
			for(j=0;j<n;j++){
				if(mx < in[j][i])mx = in[j][i];
			}
			for(j=0;j<n;j++){
				if(in[j][i] < mx && row[j] != in[j][i]){f=0;break;}
			}
			if(!f)break;
		}
		printf("Case #%d: ",cas);
		f?puts("YES"):puts("NO");
	}
	return 0;
}