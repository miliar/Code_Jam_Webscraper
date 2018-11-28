/*
 * A.cpp
 *
 *  Created on: 11 Apr 2016
 *      Author: xing
 */


#include <string.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
#include <algorithm>
#include <queue>
#include <unordered_set>
#include <unordered_map>

using namespace std;

//#define DEBUG

void solve(int index){
	char cl;
	string S;
	int K;

	getline(cin, S, ' ');
	cin>>K;
	S = S.substr(1);
#ifdef DEBUG
	cout<<"S: "<<S<<endl;
	cout<<"K "<<K<<endl;
#endif
	int res = 0, n = S.size();
	for(int i = 0;i<=n-K;i++){
		if(S[i] == '-'){
			res++;
			for(int j = 0;j<K;j++){
				S[i+j] = (S[i+j] == '-')?'+':'-';
			}
		}
#ifdef DEBUG
	cout<<"i "<<i<<endl;
	cout<<"S: "<<S<<endl;

#endif
	}

	for(int i = 0;i<K && n-1-i>=0;i++){
		if(S[n-1-i] == '-'){
			cout<<"Case #"<<index<<": IMPOSSIBLE"<<endl;
			return;
		}

	}


	cout<<"Case #"<<index<<": "<<res<<endl;


}

int main(){
	int T;

	cin>>T;

	for(int i = 0;i<T;i++){
		solve(i+1);
	}

}
