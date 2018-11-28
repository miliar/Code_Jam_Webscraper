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

char table[10][10];

char table2[10][10];

int a,b;
int count(int x,int y){
	int res = 0;
	FOR(i,-1,2) FOR(j,-1,2){
		if(x+i>=0 && x+i<a  && y+j<b && y+j>=0){
			if(table[x+i][y+j]=='*') res++;
		}
	}
	return res;
}

vector<PII> nbs(int x, int y){
	vector<PII> res;
	FOR(i,-1,2) FOR(j,-1,2){
		if(x+i>=0 && x+i<a  && y+j<b && y+j>=0){
			res.pb(mp(x+i,y+j));
		}
	}
	return res;
}

void memo(){
	FOR(i,0,a) FOR(j,0,b) table2[i][j] = table[i][j];
}

void wroc(){
	FOR(i,0,a) FOR(j,0,b) table[i][j] = table2[i][j];
}


int main(){
	int z; scanf("%d",&z);
	int casenr=0;
	while(z--){
		casenr++;
		printf("Case #%d: \n",casenr);
		int m;
		scanf("%d%d%d",&a,&b,&m);
		bool done = false;
		FOR(i,0,(1<<(a*b))){
			if(done) break;
			int mask = i;
			int ile = 0;
			FOR(k,0,a) FOR(l,0,b){
				if(mask%2==0) table[k][l] = '?';
				else { table[k][l] = '*'; ile++;}
				mask/=2;
			}
			if(ile!=m) continue;
			FOR(x,0,a) FOR(y,0,b){
				if(done) break;
				if(table[x][y]!='*'){
					memo();
					table[x][y]='.';
					int nowy = 0;
					if(count(x,y)==0) nowy = 1;
					while(nowy!=0){
						nowy = 0;
						FOR(x2,0,a) FOR(y2,0,b){
							if(table[x2][y2]=='.' && count(x2,y2)==0){
								vector<PII> p = nbs(x2,y2);
								FOR(j,0,p.size()){
									if(table[p[j].st][p[j].nd]=='?'){
										nowy++;
										table[p[j].st][p[j].nd]='.';
									}
								}

							}
						}
					}
					bool flaga = true;
					FOR(x2,0,a) FOR(y2,0,b){
						if(table[x2][y2]=='?'){ 
							flaga = false;
							break;
						}
					}
					if(flaga){
						table[x][y] = 'c';
						done = true;
					}
					else wroc();
				}
			}
			
			
		}
		if(done)
		FOR(i,0,a){
			FOR(j,0,b) putchar(table[i][j]);
			printf("\n");
		}
		else printf("Impossible\n");
	}
	return 0;
}
  

