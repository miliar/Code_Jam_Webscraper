#include <vector>
#include <queue>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <deque>

#include <cassert>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <cstdlib>

#include <algorithm>
#include <functional>
#include <string>
#include <tuple>
#include <utility>

#include <iostream>
#include <sstream>

using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n); i++)
#define forsn(i,s,n) for(int i=(s);i<(int)(n); i++)
#define esta(x,v) (find((v).begin(),(v).end(),(x)) !=  (v).end())
#define index(x,v) (find((v).begin(),(v).end(),(x)) - (v).begin())
#define debug(x) cout << #x << " = "  << x << endl

typedef long long tint;
typedef unsigned long long utint;

void imprimirVector (vector<int> &v){
	if (!v.empty()){
		int p = v.size();
		cout << "[";
		forn(i,p-1)
			cout << v[i] << ",";
		cout << v[p-1] << "]" << endl;
	}else
		cout << "[]" << endl;
}

void addDigits(set<int> &s, tint n){
	while(n > 0){
		s.insert(n%10);
		n/=10;
	}
}

int main(){
	
	int T; cin >> T;
	forn(i,T){
		tint N; cin >> N;
		if(N==0){
			cout << "Case #" << i+1 << ": INSOMNIA\n";
			continue;
		}
		set<int> digits;
		addDigits(digits, N);
		int sum = N;
		while(digits.size() < 10){
			sum += N;
			addDigits(digits, sum);
		}
		cout << "Case #" << i+1 << ": " << sum << endl; 
	}
	return 0;
}
