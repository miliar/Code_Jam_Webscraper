#include <cstdio>
#include <iostream>
#include <map>
#include <numeric>
#include <utility>
#include <vector>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <cctype>
#include <cmath>
#include <set>
#include <queue>
#include <deque>
#include <list>
#include <bitset>

#define INF (int)1e9
#define LINF (LL)1e18
#define EPS 1e-9
using namespace std;

typedef long long int LL;
template <class T>
void dbg(T start,T end){
	while(start<end){
		cout << *start << " ";
		start++;
	}
	cout << endl;
}

vector <LL> sqpalin;
LL genpalin1(LL a){
	LL temp = a, ans = a;
	while (temp){
		ans = ans*10 + (temp%10);
		temp /= 10;
	}
	return ans;
}
LL genpalin2(LL b){
	LL temp = b/10, ans = b;
	while (temp){
		ans = ans*10 + (temp%10);
		temp /= 10;
	}
	return ans;
}
bool ispalin(LL a){
	LL rev = 0, temp = a;
	while(temp){
		rev = rev*10 + (temp%10);
		temp = temp/10;
	}
	if (rev == a) return true;
	return false;
}

int main(void){
	LL p, q;
	for(int i = 1; i < 100000; i++){
		p = genpalin1(i);
		q = genpalin2(i);
		p = p*p;
		q = q*q;
		if(ispalin(p)) sqpalin.push_back(p);
		if(ispalin(q)) sqpalin.push_back(q);
	}
	sort(sqpalin.begin(), sqpalin.end());
	//dbg(sqpalin.begin(), sqpalin.end());
	LL t, a, b;
	vector <LL> :: iterator x, y;
	scanf("%lld", &t);
	for(int i = 1; i <= t; i++){
		scanf("%lld%lld", &a, &b);
		x = lower_bound(sqpalin.begin(), sqpalin.end(), a);
		y = upper_bound(sqpalin.begin(), sqpalin.end(), b);
		cout << "Case #" << i << ": " << (y-x) << "\n";
	}

	return 0;
}
