/**
 *	Author : hkbharath
 *	Problem :
 *	Lang : C++
 */	

#include <bits/stdc++.h>

#define _ ios_base::sync_with_stdio(0);cin.tie(0);
#define FOR(a,b,c) for(int a=b;a<=c;++a)
#define RFOR(a,b,c) for(int a=b;a>=c;--a)
#define LOOP(a) FOR(xx,1,a)
#define PB(b) push_back(b)
#define MP(a,b) make_pair(a,b)
#define MOD 1000000007
using namespace std;

typedef long long int64;
typedef pair<int,int> pii;
typedef vector<int> vi;

void solve(int tt){
	int ch1,ch2;
	scanf("%d",&ch1);
	int g1[4][4],g2[4][4];
	FOR(i,0,3)FOR(j,0,3)scanf("%d",&g1[i][j]);
	scanf("%d",&ch2);
	FOR(i,0,3)FOR(j,0,3)scanf("%d",&g2[i][j]);
	int ct1[17]={0},ct2[17]={0};
	ch1--;ch2--;
	FOR(i,0,3){
		ct1[g1[ch1][i]]++;
		ct2[g2[ch2][i]]++;
	}
	int cnt=0,eq;
	FOR(i,1,16){
		//printf("%d %d\n",ct1[i],ct2[i]);
		if(ct1[i] && ct2[i])cnt++,eq=i;
	}
	if(cnt==1)
		printf("%d\n",eq);
	else if(cnt==0)
		printf("Volunteer cheated!\n");
	else
		printf("Bad magician!\n");
}

int main(){
	int t,it;
	scanf("%d",&t);
	for(it=1;it<=t;it++){
		printf("Case #%d: ",it);
		solve(it);
	}
}
