#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
using namespace std; 
    //freopen("./ipt", "r", stdin);
#define lson rt<<1
#define rson rt<<1|1
#define INF 0x3f3f3f3f
#define LL long long
#define uLL unsigned long long
#define mod 1000000007
#define pi 3.1415926535898
#define mxn 105
#define mxe 10005
#define left left_
#define right right_

int pool[5][5], pol[5][5];

int main(){
    //freopen("./A-small-attempt3.in", "r", stdin);
	int T, tt=0;
	cin>>T;
	while(++tt<=T){
		bool mp[20];
		memset(mp, 0, sizeof(mp));
		int a, b;
		cin>>a;
		for(int i=1; i<=4; ++i)
			for(int j=1; j<=4; ++j)
				cin>>pool[i][j];
		cin>>b;
		for(int i=1; i<=4; ++i)
			for(int j=1; j<=4; ++j)
				cin>>pol[i][j];
		int cnt=0;
		for(int i=1; i<=4; ++i)
			mp[pool[a][i]]=1;
		int ans=0;
		for(int i=1; i<=4; ++i)
			if(mp[pol[b][i]])
				++cnt, ans=pol[b][i];
		printf("Case #%d: ", tt);
		if(cnt==1)
			printf("%d\n", ans);
		if(cnt>1)
			printf("Bad magician!\n");
		if(!cnt)
			printf("Volunteer cheated!\n");
	}
	return 0;
}
