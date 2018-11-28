#include<iostream>
#include<vector>
#include<map>
#include<algorithm>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#define MAX 10000001
using namespace std;
int cnt[MAX];
bool isFair(long long val){
	long long tmp = 0, bak = val;
	while(val){
		tmp = tmp*10 + val%10;
		val = val/10;
	}
	if(tmp == bak) return true;
	return false;
}
int main(){
	freopen("C-large-1.in", "r", stdin);
	freopen("C-large-1.out", "w", stdout);
	long long i, b, e;
	int T;
	cin>>T;
	for(i=1; i<MAX; i++){
		cnt[i]=cnt[i-1];
		if(isFair(i)&&isFair(i*i)) ++cnt[i];
	}
	for(int t=0; t<T; ++t){
		cin>>b>>e;
		b = ceil(sqrt((double)b));
		e = floor(sqrt((double)e));
		cout<<"Case #"<<t+1<<": "<<cnt[e]-cnt[b-1]<<endl;
	}
	return 0;
}