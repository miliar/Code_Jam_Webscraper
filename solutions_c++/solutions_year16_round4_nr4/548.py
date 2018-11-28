#include<bits/stdc++.h>
using namespace std;

#define scl(x) scanf("%lld",&x)
#define sc(x)  scanf("%d",&x)
#define ll long long
#define lop(i,n) for(int i=0;i<n;++i)
typedef pair<int,int> ii;
typedef pair<ll,ll> pll;

int n,arr[4];
bool ok(int idx,int mask,int mask2){
	if(idx==n)return 1;
	int p=arr[idx];
	bool foundany=0;
	lop(i,n){
		if(!(mask2&(1<<i)) )continue;
		if(!( mask&(1<< (p*n+i) ) ))continue;
		if(!ok(idx+1,mask,mask2^(1<<i) ) )return 0;
		foundany=1;
	}
	return foundany;
}
int main(){
#ifndef ONLINE_JUDGE
	freopen("i.txt","r",stdin);
	freopen("o.txt","w",stdout);
#endif
	// code for 1case for now
	int t;
	sc(t);
	lop(C,t){
		sc(n);
		int mask1=0;
		lop(i,n)lop(j,n){
			char c;
			cin>>c;
			mask1^=(c-'0')*(1<<(i*n+j));
		}
		int out=1e9;
		lop(mask2,1<<(n*n)){
			if((mask1&mask2)!=mask1)continue;

			bool can=1;
			lop(i,n)arr[i]=i;
			do{
				if(!ok(0,mask2,(1<<n)-1)){
					can=0;
					break;
				}
			}while(next_permutation(arr,arr+n));

			if(can)out=min(out,__builtin_popcount(mask2)-__builtin_popcount(mask1));
		}
		printf("Case #%d: %d\n",C+1,out);
	}
};
