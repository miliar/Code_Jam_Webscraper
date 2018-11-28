#include <iostream>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <string>
#include <algorithm>
#include <cmath>
#include <queue>
#include <cstring>

using namespace std;
#define clr(A) memset(A,0,sizeof(A))


typedef long long LL;
typedef unsigned long long ULL;

typedef pair<int,int> P;
const int INF = 1000000009;
const int mm = 10005;
priority_queue<int> que;
int mp[10][10];
int linv[10], rinv[10];
int pre[mm],suc[mm];
int a[mm];
int cal(int x,int y){
	int res = 1;
	if(x < 0) res *= -1, x = -x;
	if(y < 0) res *= -1, y = -y;
	return res*mp[x][y];
}

int main(){
//    freopen("wcbao.in","r",stdin);
//    freopen("wcbao.out","w",stdout);
    int T, c = 0;
    char st[mm];
    mp[1][1] = 1; mp[1][2] = 2;  mp[1][3] = 3;  mp[1][4] = 4;
    mp[2][1] = 2; mp[2][2] = -1; mp[2][3] = 4;  mp[2][4] = -3;
    mp[3][1] = 3; mp[3][2] = -4; mp[3][3] = -1; mp[3][4] = 2;
    mp[4][1] = 4; mp[4][2] = 3;  mp[4][3] = -2; mp[4][4] = -1;
    cin >> T;
    while(T--){
    	int L, X;
    	scanf("%d%d%s",&L,&X,st);
    	int l = strlen(st);
    	int n = l * X;
    	for(int j = 0; j < l; j++){
    		if(st[j] == 'i') a[j] = 2;
    		if(st[j] == 'j') a[j] = 3;
    		if(st[j] == 'k') a[j] = 4;
    	}
    	int p = 0;
    	while(--X){
    		for(int j = 0; j < l; p++,j++)
    			a[p+l] = a[p];
    	}
    	pre[0] = a[0];
    	for(int j = 1; j < n; j++)
    		pre[j] = cal(pre[j-1],a[j]);
    	int x = cal(2,pre[n-1]);x = cal(2,x); x = cal(2,x);
    	x = cal(x,4); x = cal(x,4);x = cal(x,4);
    	if(x != 3){
    		printf("Case #%d: NO\n", ++c);
    		continue;
    	}

    	int tmp = a[n-1];
    	if(tmp == 4) suc[n-1] = 1;
    	//suc[n-1] = a[n-1];
    	for(int j = n-2;j>=0;j--)
    	{
    		if(tmp != 4) tmp = cal(a[j],tmp);
    		if(tmp == 4) suc[j] = 1;
    	//	suc[j] = cal(a[j],suc[j+1]);
		}
    	bool found = false;
    	for(int i = 0; !found && i < n - 2; i++)
    	if(pre[i] == 2 && suc[ i + 2]) found = 1;
    	printf("Case #%d: %s\n",++c,found?"YES":"NO");
    }
    return 0;
}
