#include <bits/stdc++.h>

using namespace std;

typedef long long LL;
#define pb push_back

int ntest;
int k,c,s;
vector<int> pr;
bool vis[10000005];

LL transform(int x, int bs){
	LL res = 0;
	for(int i=15; i>-1; i--){
		res*=bs;
		if( x &(1<<i) ){			
			res+=1;
		}
	}
	return res;
}

vector<int> fat(int x){
	vector<int> res;
	for(int i=2; i<11; i++){
		LL temp = transform(x,i);
		for(int j=0; j<pr.size() && pr[j] < temp; j++){
			if( temp % pr[j] == 0 )	{
				res.pb(pr[j]);
				break;
			}
		}
	}
	return res;
}

void printRes(int x, vector<int> ft){
	for(int i=15; i>-1; i--){
		if( x&(1<<i) )
			printf("1");
		else 
			printf("0");
	}
	for(int i=0; i<9; i++){
		printf(" %d",ft[i]);
	}
	printf("\n");
}

void solve(){
	printf("Case #1:\n");	
	int cnt = 0;
	int x = (1<<15)+1;
	while(cnt<50){
		vector<int> ft = fat(x);
		if(ft.size() == 9){		
			cnt++;			
			printRes(x,ft);
		}
		x+=2;
	}	
}

int main(){
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	for(int i=2; i<10000000; i++){
		if(!vis[i]){
			pr.pb(i);
			for(LL j = 1LL*i*i; j<10000000; j+=i) vis[j] = 1;
		}
	}
	solve();	
	return 0;
}
	
