#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <string>
#include <sstream>
#include <vector>
#include <map>
#define CLR(x) memset(x,0,sizeof(x))
#define ll long long
using namespace std;

const int   Maxn=3200,Maxm=2500000,Mo=1000000007,oo=INT_MAX>>2;

int N,cnt;
string st,g;
map<string,int> id;
vector<int> Node[200];



int use[5000],mk[Maxn] ,ans;
void dfs(int id){
	if (id == N +1){
		memset(use,0,sizeof(use));
		for (int i=1;i<=N;i++){
			for (int j=0;j<Node[i].size();j++)
				use[Node[i][j]] |= mk[i]; 
		}	
		int tmp = 0;
		for (int i=1;i<=cnt;i++) tmp += (use[i] == 3);
		ans = min(ans , tmp);
		return;
	}
	mk[id] = 1;
	dfs(id+1);
	mk[id] = 2;
	dfs(id+1);
}


int main() {
	int T;
	cin >> T;
	int cs = 0 ;
	while(T--){
		// SAP.Init();
		ans = oo;
		cnt = 0;		
		id.clear();

		cin >> N;
		getline(cin,st);

		for (int i=1;i<=N;i++){
			Node[i].clear();
			getline(cin,st);
			istringstream sin(st);
			while(sin>>g){
				if (!id[g]) id[g] = ++cnt;
				Node[i].push_back(id[g]);
			}			
			// cout << i << endl;
			// for (int x=0;x<Node[i].size();x++)
				// cout << Node[i][x] <<" ";cout << endl;
		}
		// cout << cnt << endl;
		// for (int i=1;i<=N;i++)
		// 	for (int j=i+1;j<=N;j++){
		// 		int val =  0;
		// 		for (int x=0;x<Node[i].size();x++)
		// 			for (int y=0;y<Node[j].size();y++)
		// 				if(Node[i][x] == Node[j][y]){
		// 					val ++;
		// 					break;
		// 				}
				// if (val) {
				// 	SAP.build(i,j,val);
				// 	SAP.build(j,i,val);
				// 	cout << i <<" "<<  j <<" "<<val<< endl;
				// }
				//SAP.build(j,i,val);					
				
			// }
		mk[1] = 1;
		mk[2] = 2;
		dfs(3);
		printf("Case #%d: %d\n",++cs , ans );		
	}
    return 0;
}