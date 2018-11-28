#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>
using namespace std;
#define ull unsigned long long
vector <int> p;
int n,j;
const int MAXN=1e5;
int a[MAXN];
int num[33];
ull quickpow(ull a,ull b){
    ull r=1;
    ull base=a;
    while(b){
        if(b&1) r*=base;
        base*=base;
        b>>=1;
    }
    return r;
}
void sushu(){
	memset(a,0,sizeof(0));
    int m=sqrt(MAXN+0.5);
    for(int i=2;i<=m;i++){
        if(!a[i]){
            for(int j=i*i;j<=MAXN;j+=i){
                a[j]=1;
            }
        }
    }
}

int cal(int k){
	ull res=0;
	for(int i=1;i<=n;i++){
		if(num[i])
		res+=quickpow(k,i-1);
	}
	int i;
	if(res<MAXN){
		if(!a[res]) return -1;
		else{
			for(i=2;i<res;i++){
				if(!a[i]&&!(res%i)){
					p.push_back(i);
					break;
				}
			}
		}
	}else{
		int tmp=MAXN;
		bool flag=false;
		for(i=2;i<=tmp;i++){
			if(!a[i]&&!(res%i)){
				p.push_back(i);
				flag=true;
				break;
			}
		}
		if(!flag) return -1;
	}
	return i;
}
void solve(){
	for(int i=2;i<=n-1;i++){
		if(num[i]==1) {
			num[i]=0;
		}else{
			num[i]=1;
			return;
		}
	}
}
int main(){
	int t;
	scanf("%d",&t);
	sushu();
	int time=0;
	while(t--){
		++time;
		scanf("%d%d",&n,&j);
		memset(num,0,sizeof(num));
		num[n]=1;
		num[1]=1;
		int cnt=0;
		printf("Case #%d:\n",time);
		while(cnt<j){

			p.clear();
			int pp=0;
			for(int i=2;i<=10;i++){
				if(cal(i)==-1){
					pp++;
				}
			}

			if(!pp){
				int len=p.size();
				for(int i=n;i>=1;i--){
					printf("%d",num[i]);
				}
				printf(" ");
				for(int i=0;i<len;i++){
					printf("%d",p[i]);
					if(i!=len-1) printf(" ");
					else printf("\n");
				}
				cnt++;
			}
			solve();
		}
	}
	return 0;
}

