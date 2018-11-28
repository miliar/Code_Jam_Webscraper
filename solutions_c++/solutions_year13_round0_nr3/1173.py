#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>
using namespace std;
#define ll long long
bool judge(ll n){
	ll bit[105], size = 0;
	while(n){
		bit[size++] = n % 10;
		n /= 10; 
	}
	for(int i = 0; i < size / 2; i++){
		if(bit[i] != bit[size - i - 1]) return false;
	}
	return true;
}
ll cnt[10005];
int csize = 0;
void gao(ll n){
	ll tmp = n;
	ll bit[105], size = 0;
	while(tmp){
		bit[size++] = tmp % 10; tmp /= 10;
	}
	tmp = n;
	for(int i = 0; i < size; i++){
		tmp *= 10;
		tmp += bit[i];
	}
	if(judge(tmp * tmp)){
	//	cout << tmp << " " << tmp * tmp << endl;
		cnt[csize++] = tmp * tmp;
	}
	tmp = n;
	for(int i = 1; i < size; i++){
		tmp *= 10;
		tmp += bit[i];
	}
	
	if(judge(tmp * tmp)){
	//	cout << tmp << " " << tmp * tmp << endl;
		cnt[csize++] = tmp * tmp;
	}
}
void init(){
	for(int i = 1; i <= 10000; i++){
		gao(i);
	}
	sort(cnt, cnt + csize);
	csize = unique(cnt, cnt + csize) - cnt;
	//for(int i = 0; i < csize; i++){
	//	cout << cnt[i] << endl;
	//}
}
int main() {
	freopen("C-large-1.in", "r", stdin);
	ll cas, c = 1, l, r;
	init();
	scanf("%I64d", &cas);
	while(cas--){
		scanf("%I64d%I64d", &l, &r);
		int pos1 = upper_bound(cnt, cnt + csize, l-1) - cnt;
		int pos2 = upper_bound(cnt, cnt + csize, r) - cnt;
		printf("Case #%I64d: %d\n", c++, pos2-pos1);
	}
}
 				    
