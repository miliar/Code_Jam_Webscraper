/*
 * B.Haircut.cpp
 *
 *  Created on: Apr 18, 2015
 *      Author: Yasser
 */

#include<iostream>
#include<cstdio>
#include<vector>
#include<queue>
#include<algorithm>
#include<cmath>

using namespace std;

vector<int> v;

int main(){

	freopen("test.in","rt",stdin);
	freopen("results.txt", "wt", stdout);
	int T,B,N;
	cin>>T;
	for(int tt= 0;tt<T;tt++) {
		v.clear();
		cin >>B>>N;
		v.resize(B);
		int x=1;
		for(int i=0;i<B;i++) {
			cin>>v[i];
			x = (x*v[i]) / std::__gcd(x,v[i]);
		}
		int c =0;
		for(int i=0;i<B;i++){
			c+= (x/v[i]);
		}
		N %= c;
		if(!N) N = c;

		priority_queue<pair<int,int>, vector<pair<int,int> >, greater<pair<int,int> > > q;
		for(int i=0;i<B;i++) {
			q.push(make_pair(0,i+1));
		}
		for(int i=0;i+1<N;i++) {
			pair<int,int> p = q.top();
			q.pop();
			q.push(make_pair(p.first+v[p.second-1], p.second));
		}
		printf("Case #%d: %d\n", tt+1, q.top().second);
	}

	return 0;
}
