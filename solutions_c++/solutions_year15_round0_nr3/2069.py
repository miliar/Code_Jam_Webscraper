#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;
int cal[8][8]={{0,1,2,3,4,5,6,7},
				{1,4,3,6,5,0,7,2},
				{2,7,4,1,6,3,0,5},
				{3,2,5,4,7,6,1,0},
				{4,5,6,7,0,1,2,3},
				{5,0,7,2,1,4,3,6},
				{6,3,0,5,2,7,4,1},
				{7,6,1,0,3,2,5,4}};
string a,b;
int n,l;
bool dfs(int dep,int now,int v){
	if(dep==1){
		for(int i=now;i<n*l;i++){
			if(v==dep){
				if(dfs(dep+1,i,0))return 1;
			}
			v=cal[v][b[i]];
		}
	}
	else if(dep==2){
		for(int i=now;i<n*l;i++){
			if(v==dep){
				if(dfs(dep+1,i,0))return 1;
			}
			v=cal[v][b[i]];
		}
	}
	else{
		for(int i=now;i<n*l;i++){
			v=cal[v][b[i]];
		}
		if(v==3)return 1;
	}
	return 0;
}
int main()
{
    freopen("C-small-attempt4.in","r",stdin);
	freopen("out.out","w",stdout);
	int T;cin>>T;
	int cs=1;
	while(T--){
		cin>>l>>n;
		cin>>a;
		for(int i=0;i<l;i++){
			a[i]=a[i]-'i'+1;
		}
		b="";
		for(int i=0;i<n;i++)b+=a;
		printf("Case #%d: %s\n",cs++,dfs(1,0,0)?"YES":"NO");
	}
	return 0;
}