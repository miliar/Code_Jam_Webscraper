#include <cstdio>
#include <iostream>
#include <numeric>
#include <fstream>
#include <map>
#include <algorithm>
#include <bitset>
#include <set>
#include <vector>
#include <utility>
#include <cstring>
#include <string>
#include <cctype>
#include <cmath>
#include <climits>
using namespace std;
typedef vector<int> vi;
typedef vector< vi > vvi;
typedef pair<int,int> pi;
typedef vector< pi > vpi;
typedef vector< vpi > vvpi;
#define rep(i,a,b) for(i = a;i<=b;i++)
#define all(c) (c).begin(),(c).end()
#define present(c,x) (c).find(x)!=(c).end()
#define gpresent(c,x) find(all(c),x)
#define tr(c,it) for( vector<int>::iterator it = (c).begin();it!=(c).end();it++ )
#define accu(c) accumulate(all(c),0)
#define scalar(c1,c2) inner_product(all(c1),(c2).begin(),0)
#define maxel(c) max_element(all(c))
#define minel(c) min_element(all(c))
#define Size(C) C.size();
#define fx first
#define sx second
#define pb(a) push_back(a)
#define mp(a,b) make_pair(a,b)
#define inf -300010
#define ll long long
#define M 1000000007

ifstream in("B-small-attempt0.in",ios::in);
ofstream out("output.out",ios::out);
  
 int T,n,m,pat[110][110],a[110][110],vis[110][110],flag = 0;
 
 void fill(){
 	int i,j;
	rep(i,1,n){
		rep(j,1,m){
			a[i][j] = 2;
		}
	}
 }
 
 void input(){
 	int i,j;
 	rep(i,1,n){
 		rep(j,1,m){
 			in>>pat[i][j];
 		}
 	}
 }
 
 void dfs(int i,int j ,int val){
 
 	if(pat[i][j]!=1){
 		flag = 1;
 		return;
 	}
 	
 	a[i][j] = 1;
 	vis[i][j]++;
 	
 	//traverse on row
 	if(val==0){
 		if(j+1<=m)
 			dfs(i,j+1,0);
 	}
 	//traverse on column
 	else{
 		if(i+1<=n)
 			dfs(i+1,j,1);
 	}
 	
 	if(flag){
 	   if(vis[i][j]==1)
 		a[i][j] = 2;
 	   vis[i][j]--;
 	}
 }
 
 bool check(){
 	int i,j;
 	rep(i,1,n){
 		rep(j,1,m){
 			if(a[i][j]!=pat[i][j])
 				return 0;
 		}
 	}
 	return 1;
 }

 int main(){
  int t,i,j;
  in>>T;
  rep(t,1,T){
  	in>>n>>m;
  	memset(vis,0,sizeof(vis));
  	fill();
	input();
  	//dfs on col.
  	rep(j,1,m){
  		flag = 0;
  		if(pat[1][j]==1)
  			dfs(1,j,1);
  	}
  	//dfs on row.
  	rep(i,1,n){
  		flag = 0;
  		if(pat[i][1]==1)
  			dfs(i,1,0);
  	}
  	
  	if(check()){
  		out<<"Case #"<<t<<": YES\n";
  	}
  	else
  		out<<"Case #"<<t<<": NO\n";
  }
  return 0;
 }
