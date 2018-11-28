#include<bits/stdc++.h>
using namespace std;
#define mp make_pair
typedef long long ll;
vector<pair<int,int> > m[5];
void init(){
	m[4].push_back(mp(1,1));
	m[4].push_back(mp(1,2));
	m[4].push_back(mp(1,3));
	m[4].push_back(mp(1,4));
	m[4].push_back(mp(2,2));
	m[4].push_back(mp(2,3));
	m[4].push_back(mp(2,4));
	m[4].push_back(mp(3,3));
	m[3].push_back(mp(1,1));
	m[3].push_back(mp(1,2));
	m[3].push_back(mp(1,3));
	m[3].push_back(mp(1,4));
	m[3].push_back(mp(2,2));
	m[3].push_back(mp(2,4));
	m[3].push_back(mp(4,4));
	m[2].push_back(mp(1,1));
	m[2].push_back(mp(1,3));
	m[2].push_back(mp(3,3));
}
int main(){
#ifndef ONLINE_JUDGE
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small-attempt0.out","w",stdout);
#endif
	int t;
	init();
	scanf("%d",&t);
	while(t--){
		static int cas=1;
		printf("Case #%d: ",cas++);
		int x,a,b;
		scanf("%d%d%d",&x,&a,&b);
		if(a>b) swap(a,b);
		if(binary_search(m[x].begin(),m[x].end(),mp(a,b))) puts("RICHARD");
		else puts("GABRIEL");
	}

	return 0;
}
