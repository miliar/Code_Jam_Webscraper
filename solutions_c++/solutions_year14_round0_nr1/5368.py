#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cmath>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<cstring>

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define VI vector<int>
#define PII pair<int,int>
#define st first
#define nd second
#define mp make_pair
#define pb push_back
#define lint long long int

using namespace std;


int main(){
	int z; scanf("%d",&z);
	int casenr=0;
	while(z--){
		casenr++;
		printf("Case #%d: ",casenr);
		int ans[2];
		int tab[4][4][2];
		FOR(i,0,2){
			scanf("%d",&ans[i]);
			FOR(j,0,4) FOR(k,0,4) scanf("%d",&tab[j][k][i]);
		}
		FOR(i,0,2) ans[i]--;

		int ile[17];
		FOR(i,0,17) ile[i] = 0;

		FOR(i,0,2){
			FOR(k,0,4)
				ile[tab[ans[i]][k][i]]++;		

		}
		VI pos;
		FOR(i,0,17) if(ile[i]==2) pos.pb(i);
		if(pos.size()==0) printf("Volunteer cheated!\n");
		if(pos.size()==1) printf("%d\n",pos[0]);
		if(pos.size()>=2) printf("Bad magician!\n");
	}
	return 0;
}
  

