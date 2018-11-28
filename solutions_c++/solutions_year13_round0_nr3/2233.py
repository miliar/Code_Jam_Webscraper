#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>

typedef long long ll;
ll p10[17];
std::vector<ll> pals;

bool pal(ll num){
	bool pos = true;
	int cur = 15;
	while(num/p10[cur] == 0) cur--;
	for(int i = 0; i <= cur/2; i++){
		//printf("%d %d\n", ((num%p10[i+1])/p10[i]),  ((num%p10[cur-i+1])/p10[cur-i]));
		if(((num%p10[i+1])/p10[i]) != ((num%p10[cur-i+1])/p10[cur-i])) pos = false;
	}
	return pos;
}

void genpal(int size, int pos, ll cnum){
	ll a, b, nnum;
	int fin;
	if(size%2==1)
		fin = (size/2);
	else
		fin = ((size-1)/2);
	for(int i = 0; i <= 9; i++){
		nnum = cnum;
		if(i == 0 && pos == 0) continue;
		a = i*p10[pos];
		b = i*p10[(size-1)-pos];
		if(pos == (size-1)-pos){
			nnum += a;
		}
		else
			nnum += (a+b);
		//printf("%d %d %d %lld %lld %lld\n", size, pos, (size/2+(size%2==1?1:0)), a, b, nnum);
		if(pos == fin){
		//	printf("%lld\n", nnum);
			pals.push_back(nnum);
		}
		else
			genpal(size, pos+1, nnum);
	}
}

int main(){
	int t;
	ll a, b, coun = 0;
	scanf("%d", &t);
	p10[0] = 1;
	for(int i = 1; i < 17; i++) p10[i] = p10[i-1]*10;
	for(int x = 1; x <= t; x++){
		pals.clear();
		coun = 0;
		int bot = 15, top=15;
		scanf("%lld %lld", &a, &b);
		int c = (int)(sqrt(a)+0.5);
		int d = (int)(sqrt(b)+0.5);
		while(c/p10[bot] == 0) bot--;
		while(d/p10[top] == 0) top--; 
		bot++; top++;
		for(int i = bot; i <= top; i++){
			genpal(i, 0, 0); //generate palindrome
		}
		std::sort(pals.begin(), pals.end());

		for(int i = 0; i < (int)pals.size()-1; i++){
			ll temp = pals[i]*pals[i];
			if(temp > b) break;
			if(pal(temp) && temp >= a) coun++;
		}

		printf("Case #%d: %lld\n", x, coun);
	}
	return 0;
}