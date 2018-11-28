#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <bitset>
#include <cmath>
#include <numeric>
#include <iterator>
#include <iostream>
#include <cstdlib>
#include <functional>
#include <queue>
#include <stack>
using namespace std;
#define PB push_back
#define MP make_pair
#define SZ size()
#define ST begin()
#define ED end()
#define CLR clear()
#define ZERO(x) memset((x),0,sizeof(x))
typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int,int> PII;
const double EPS = 1e-8;

#define YES(x) cout << "Case #" << (x)  << ": YES" << endl
#define NO(x) cout << "Case #" << (x)  << ": NO" << endl;

int T,L,X;
string str;
bool ii,jj,kk;

struct ALPHA{
	char alp;
	int isPos;
	ALPHA(char _alp,bool _isPos = 1): alp(_alp),isPos(_isPos){}
};

ALPHA operator*(const ALPHA &a, const ALPHA &b){
	ALPHA res('1');
	res.isPos = a.isPos*b.isPos;
	if( a.alp=='1' ) res.alp = b.alp;
	if( b.alp=='1' ) res.alp = a.alp;
	if(a.alp==b.alp){
		res.alp = '1';
		res.isPos*=-1;
	}
	//i*j=k
	if( a.alp=='i'&&b.alp=='j' ) res.alp = 'k';
	//i*k=-j
	if( a.alp=='i'&&b.alp=='k' ) {
		res.alp = 'j';
		res.isPos *= -1;
	}
	if( a.alp=='j'&&b.alp=='i' ) {
		res.isPos *= -1;
		res.alp = 'k';
	}
	if(a.alp=='j'&&b.alp=='k'){
		res.alp='i';
	}
	if( a.alp=='k'&&b.alp=='i' ) res.alp = 'j';
	if( a.alp=='k'&&b.alp=='j' ) {
		res.isPos *= -1;
		res.alp = 'i';
	}
	return res;
}


int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin >> T;
	for(int cases = 1; cases<=T; cases++){
		cin >> L >> X;
		cin >> str;
		string b = str;
		for(int i=1;i<X;i++){
			str += b;
		}
		int i = 0;
		ALPHA a(str[i++],true);
		L = str.size();
		while(i<L&&!(a.alp=='i'&&a.isPos==1)) a = a*str[i++];
		if(i==L){
			NO(cases);
			continue;
		}
		a = ALPHA(str[i++],true);
		while(i<L&&!(a.alp=='j'&&a.isPos==1)) a = a*str[i++];
		if(i==L){
			NO(cases);
			continue;
		}
		a = ALPHA(str[i++],true);
		while(i<L) a = a*str[i++];
		if( a.alp=='k'&&a.isPos==1){
			YES(cases);
		} else NO(cases);
	}
	return 0;
}