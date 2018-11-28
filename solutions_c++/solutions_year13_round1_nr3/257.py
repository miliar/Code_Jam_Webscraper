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
int R,N,M,K;
int a[100];
int x[100],pro[100],S;
void create(int t,int p){
	if(t>N){
		pro[++S]=p;
		return;
	}
	create(t+1,p*x[t]);
	create(t+1,p);
}
int find(int s){
	for(int i=1;i<=S;i++) if(pro[i]==s) return(1);
	return(0);
}
int pan(){
	int i;
	for(i=1;i<=K;i++){
		if(find(a[i])==0) return(0);
	}
	return(1);
}
int ans;
void dfs(int t){
	if(t>N){
		S=0;
		create(1,1);
		if(pan()){
			for(int i=1;i<=N;i++) ans=ans*10+x[i];
		}
		return;
	}
	int i;
	for(i=2;i<=M&&ans==0;i++){
		x[t]=i;
		dfs(t+1);
	}
}
void work(){
	int i;
	ans=0;
	for(i=1;i<=K;i++) cin>>a[i];
	dfs(1);
	if(ans==0) for(i=1;i<=N;i++) printf("2");
	else cout<<ans;
	cout<<endl;
}
void init(){
	cin>>R>>N>>M>>K;
	int i;
	for(i=1;i<=R;i++){
		work();
	}
}
int main(){
    freopen("C-small-1-attempt0.in","r",stdin);
    freopen("c.out","w",stdout);
    long long T,i;
    cin>>T;
    for(i=1;i<=T;i++){
		printf("Case #%d: \n",i);
		init();
	}
}
