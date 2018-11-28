#include <iostream>
#include <fstream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <cassert>

#define FOR(i,n) for(int i=0,_n=n;i<_n;i++)
#define FORR(i,s,n) for(int i=s,_n=n;i<_n;i++)
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define pli pair<ll,int>
#define vi vector<int>
#define fs first
#define sec second

#define maxn 100000

using namespace std;
typedef long long ll;

const ll MOD = 1000000007LL;

void solve(int zaporedna){
	int rez=0;
	int r,c;
	scanf("%d%d",&r,&c);
	vector <string> m;
	FOR(i,r){
		string tmp;
		cin >> tmp;
		m.pb(tmp);
	}
	vector <vector <bool> > kazem;
	vector <vector <bool> > drugi;
	vector <bool> prazen (c,0);
	FOR(i,r){
		kazem.pb(prazen);
		drugi.pb(prazen);
	}
	FOR(i,r){
		FOR(j,c){
			if(m[i][j]=='.')continue;
			if(m[i][j]=='>'){
				int p=j+1;
				while(p<c){
					if(m[i][p]!='.'){
						kazem[i][j]=1;
						break;
					}
					p++;
				}
			}
			if(m[i][j]=='<'){
				int p=j-1;
				while(p>=0){
					if(m[i][p]!='.'){
						kazem[i][j]=1;
						break;
					}
					p--;
				}
			}
			if(m[i][j]=='v'){
				int p=i+1;
				while(p<r){
					if(m[p][j]!='.'){
						kazem[i][j]=1;
						break;
					}
					p++;
				}
			}
			if(m[i][j]=='^'){
				int p=i-1;
				while(p>=0){
					if(m[p][j]!='.'){
						kazem[i][j]=1;
						break;
					}
					p--;
				}
			}
			if(kazem[i][j])continue;
			FOR(k,r){
				if(k!=i && m[k][j]!='.')drugi[i][j]=1;
			}
			FOR(k,c){
				if(k!=j && m[i][k]!='.')drugi[i][j]=1;
			}
		}
	}
	/*cout << "kazem\n";
	FOR(i,r){
		FOR(j,c){
			cout << kazem[i][j];
		}cout<<endl;
	}
	cout << "drugi\n";
	FOR(i,r){
		FOR(j,c){
			cout << drugi[i][j];
		}cout <<endl;
	}*/
	FOR(i,r){
		FOR(j,c){
			if(m[i][j]=='.')continue;
			if(kazem[i][j])continue;
			if(drugi[i][j])rez++;
			else{
				printf("Case #%d: IMPOSSIBLE\n",zaporedna);
				return;
			}
		}
	}
	printf("Case #%d: %d\n",zaporedna,rez);
}

int main(){
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)solve(i);
	return 0;
}
