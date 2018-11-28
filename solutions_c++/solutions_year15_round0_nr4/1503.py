#include<iostream>
#include<map>
#include<string>
#include<string.h>
#include<vector>
#include<stdio.h>
#include <cstdio>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <sstream>
#include <cmath>
#include <bitset>
#include <limits.h>
#include <limits>
#include <utility>
#include <set>
#include <fstream>
#include <numeric>
#include <functional>
#define LL long long int
#define R(i) freopen(i,"r",stdin)
#define W(i) freopen(i,"w",stdout)
#define R_W R("i.txt"),W("o.txt");
#define FOR(i,f,t) for(int i=f;i<t;i++)
#define r(e) for(int i=0;i<e;i++)
#define oo (LL)numeric_limits<int>::max()
#define readVector(n,in,v) r(n){cin>>in;v.push_back(in);}
#define readGrid(n,m,data) r(n)FOR(j,0,m){cin>>data[i][j];}
#define all(x) x.begin(),x.end()
#define DFS_WHITE -1
#define DFS_BLACK 1
using namespace std;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
vector< vi > AdjList;
int solution[5][5][5];
int main(){
	ifstream myfile ("sols.txt");
	for(int i=0;i<64;i++){
		int a,b,c,d;
		myfile>>a>>b>>c>>d;
		solution[a][b][c]=d;
	}
	int t;
	int cases=1;
	cin >> t;
	while (t--){
		int x,r,c;
		cin>>x>>r>>c;
		if(solution[x][r][c]==0){
			printf("Case #%d: %s\n",cases++,"RICHARD");
		}else{
			printf("Case #%d: %s\n",cases++,"GABRIEL");
		}		
	}
}