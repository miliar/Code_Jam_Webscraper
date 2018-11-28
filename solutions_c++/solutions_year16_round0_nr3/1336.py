#include <iostream>
#include <cassert>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <bitset>
#include <unordered_map>
#include <unordered_set>
#include <cstring>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef string str;

template <typename T>
bool next_selection(T* begin, T* end, T** selectBegin, T** selectEnd){
	if(*(selectEnd-1)<end-1){
		(*(selectEnd-1))++;
		return true;
	}
	else if(selectBegin+1==selectEnd){
		*selectBegin=begin;
		return false;
	}
	else{
		bool result=next_selection(begin,end-1,selectBegin,selectEnd-1);
		*(selectEnd-1)=1+*(selectEnd-2);
		return result;
	}
}

ll facll(ll n){
	if(n)
		return n*facll(n-1);
	return 1;
}

ld facld(ll n){
	if(n)
		return (ld)n * facld(n-1);
	return 1.;
}

#define mp make_pair
#define x first
#define y second
#define pub push_back
#define puf push_front
#define pob pop_back
#define pof pop_front
#define hash unordered_map
#define sz size()

#define v(type) deque<type >
#define it(container) typeof((container).begin())
#define all(x) (x).begin(), (x).end()
#define select(x,i) (x).begin()+(i), (x).begin()+(i)+1
#define foreach(cit,container) for(typeof((container).begin()) cit = (container).begin(); cit != (container).end(); cit++)
#define foreachc(c,cit,container) ll c=0;for(typeof((container).begin()) cit = (container).begin(); cit != (container).end(); c++, cit++)
#define forn(i, n) for (ll i = 0; i < (ll)(n); ++i)
#define fornn(i, a, b) for (ll i = (ll)(a); i < (ll)(b); ++i)
#define fore(i, a, b) for (ll i = (ll)(a); i <= (ll)(b); ++i)

#define inf 9000000000000000000L
#define eps 1e-15

void init(){
}

ll toNum(str s){
	ll result=0;
	foreach(let,s){
		result<<=1;
		if(*let=='1')
			++result;
	}
	return result;
}

str toBinary(ll n){
	str result="";
	while(n>0){
		if(n%2)
			result='1'+result;
		else
			result='0'+result;
		n/=2;
	}
	return result;
}

bool valid(str s, ll N){
	if(s.sz!=N)
		return false;
	if(s[0]!='1')
		return false;
	if(s[N-1]!='1')
		return false;
	//check 3-divisibility for base 2
	ll sum=0;
	forn(i,N){
		if(s[i]=='1'){
			++sum;
			if(i%2)
				++sum;
		}
	}
	if(sum%3)
		return false;
	//check 2-divisibility for base 3
	sum=0;
	forn(i,N)
		if(s[i]=='1')
			++sum;
	if(sum%2)
		return false;
	//check 3-divisibility for base 4
	sum=0;
	forn(i,N)
		if(s[i]=='1')
			++sum;
	if(sum%3)
		return false;
	//check 7-divisibility for base 6
	sum=0;
	forn(i,N){
		if(s[i]=='1'){
			++sum;
			if(i%2)
				sum+=5;
		}
	}
	if(sum%7)
		return false;
	//all other divisibilitys will check out
	return true;
}

typedef str otype;
otype calcFunction(ll N, str lastResult) {
	ll num=toNum(lastResult)+1;
	otype result=toBinary(num);
	while(!valid(result, N)){
		++num;
		result=toBinary(num);
	}
	return result;
}

int main() {
	init();
	ofstream outfile("output.txt");
	ll tests = 0;
	cin >> tests;
	fore(test, 1, tests){
		//read input
		ll N,J;
		cin >> N >> J;
		//write output
		outfile << "Case #" << test << ":" << endl;
		cout << "Case #" << test << ":" << endl;
		str lastResult="1";
		forn(i,N-1)
			lastResult+="0";
		forn(i,J){
			otype result=calcFunction(N,lastResult);
			outfile << result << " 3 2 3 2 7 2 3 2 3" << endl;
			cout << result << " 3 2 3 2 7 2 3 2 3" << endl;
			lastResult=result;
		}
	}
	outfile.close();
	return 0;
}