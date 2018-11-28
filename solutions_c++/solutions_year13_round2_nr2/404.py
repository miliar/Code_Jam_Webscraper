#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <sstream>
#include <functional>
#include <map>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <list>
#include <numeric>
using namespace std;
const double PI = 3.14159265358979323846;
const double EPS = 1e-12;
const int INF = 1<<25;
typedef pair<int,int> P;
typedef long long ll;
typedef unsigned long long ull;

ll fact[20];

ll comb(int n,int m){
	return fact[n]/(fact[n-m]*fact[m]);
}


int main(){
	fact[0] = 1;
	for(int i = 1; i < 20; i++)fact[i] = i*fact[i-1];
	int T;
	cin>>T;
	for(int Case = 1; Case <= T; Case++){
		ll N,X,Y;
		cin>>N>>X>>Y;
		X = abs(X);
		ll M = X+Y+1;
		if(M*(M+1)/2 <= N){
			printf("Case #%d: 1.0\n",Case);
			continue;
		}
		//cout<<"PASS1"<<endl;
		N -= (M-2)*(M-1)/2;
		//cout<<"N:"<<N<<endl;
		if(N <= Y || !X){
			printf("Case #%d: 0.0\n",Case);
			continue;
		}
		//cout<<"PASS2"<<endl;

		if(N >= M+Y){
			printf("Case #%d: 1.0\n",Case);
			continue;
		}
		//cout<<"PASS3"<<endl;

		ll p = 0;
		for(int i = Y+1; i <= N; i++) p += comb(N,i);

		//cout<<"PASS4"<<endl;

		printf("Case #%d: %0.8f\n",Case,(double)p/(1<<N));

		

	}
	return 0;
}
