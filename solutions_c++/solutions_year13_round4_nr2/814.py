#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
int cs;
int n, p;
int ansind(int n, int p){
	if(p<=(1<<(n-1))){
		return 1;
	}else if(p==(1<<n)){
		return (1<<n);
	}else{
		return ansind(n-1,p-(1<<(n-1)))*2+1;
	}
	return 0;
}
int ansdep(int n, int p){
	//printf("%d %d %d\n",n,p,p<(1<<(n/2)));
	if(p<=(1<<(n-1))){
		return ansdep(n-1,p)*2;
	}else if(p==(1<<n)){
		return (1<<n)-1;
	}else{
		return (1<<n)-2;
	}
}
void input(){
	scanf("%d%d",&n,&p);
}
void solve(){
	printf("Case #%d: %d %d\n",cs+1,ansind(n,p)-1,ansdep(n,p));
}
int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	int zz;
	scanf("%d",&zz);
	for(cs=0; cs<zz; cs++){
		input();
		solve();
	}
	return 0;
}
