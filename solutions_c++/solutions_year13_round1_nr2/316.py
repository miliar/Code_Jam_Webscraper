#include <string>
#include <vector>
#include <map>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <stack>
#include <set>
#include <sstream>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <stdio.h>
#include <time.h>
using namespace std;
int E,R,n;
int v[10002];
int f[10002];
bool done[10002];
int maxn;
void dfs(int x,int e,int s){
	if(x==n){
		s=s+e*v[n];
		if(s>maxn) maxn=s;
		return;
	}
	int i,e1;
	for(i=0;i<=e;i++){
		e1=e-i+R;
		if(e1>E) e1=E;
		dfs(x+1,e1,s+i*v[x]);
	}
}
void work(){
	cin>>E>>R>>n;
	int i;
	for(i=1;i<=n;i++) cin>>v[i];
	maxn=0;
	dfs(1,E,0);
	cout<<maxn<<endl;
}
int main(){
    freopen("B-small-attempt1.in","r",stdin);
    freopen("b.out","w",stdout);
    long long T,i;
    cin>>T;
    for(i=1;i<=T;i++){
		printf("Case #%d: ",i);
		work();
	}
}
