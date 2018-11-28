/*
 * A.MushroomMonster.cpp
 *
 *  Created on: Apr 18, 2015
 *      Author: Yasser
 */

#include<iostream>
#include<cstdio>
#include<vector>
#include<cmath>
using namespace std;
vector<int> v;

int getWay1() {
	int ret = 0;
	for(int i=1;i<v.size();i++) {

		if(v[i] < v[i-1])
			ret+= (v[i-1] - v[i]);

	}
	return ret;

}

int getWay2(){

	int ret = 0;
	for(int i=0;i<10000;i++) {
		ret = 0;
		int j;
		for(j=1;j<v.size();j++) {
			if(v[j-1] - i > v[j] )
				break;
			ret += min(i,v[j-1]);

		}
		if(j == v.size()){
			cerr<<i<<endl;
			return ret;
		}
	}


	return ret;
}
int main() {

	freopen("test.in","rt",stdin);
	freopen("results.txt", "wt", stdout);

	int T,N;
	cin>> T;
	for(int tt=0;tt<T;tt++) {
		cin>>N;
		v.clear();
		v.resize(N);
		for(int i=0;i<N;i++) {
			cin>>v[i];
		}

		int x = getWay1();
		int y = getWay2();

		printf("Case #%d: %d %d\n",tt+1, x, y);
	}


	return 0;
}
