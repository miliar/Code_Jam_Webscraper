#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <string>
#include <algorithm>
#include <iostream>
#include <math.h>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

vi getVector(int n){
	vi r;
	while(n != 0){
		r.push_back(n % 10);
		n /= 10;
	}
	return r;
}

int main(){
	int T, N;
	cin >> T;
	for(int i = 1; i <= T; i++){
	//for(int i = 0; i <= 1000000; i++){
		cin >> N;
		set<int> s;
		ull tmp = N;
		while(true){
			if(N == 0) break;
			vi r = getVector(tmp);
			for(int j = 0; j < r.size(); j++){
				s.insert(r[j]);
			}
			if(s.size() == 10) break;
			tmp += N;
		}
		
		cout << "Case #" << i << ": ";
		if(s.size() < 10){
			cout << "INSOMNIA" << endl;
		}else{
			cout << tmp << endl;
		}
	}
}
