/*
 Author : Komal Nagar
 Contest Name : codejam 
 Problem Name : Ominous Omino
 */
#include <iostream>
#include <vector>
#include <set>
#include <queue>
#include <deque>
#include <map>
#include <stack>
#include <string>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
using namespace std;

#define maxN 100001
#define INF 99999999
#define LL long long
#define mod 1000000007

int main(int argc, char const *argv[]) {
	int t,x,r,c;
	cin>>t;
	string result;

	for(int i=1;i<=t;i++){
		cin>>x>>r>>c;
		int totalDim = r*c;
		//cout<<x<<" "<<r<<" "<<c<<endl;
		if(totalDim%x == 0 && x-1 <= min(r,c))
			result = "GABRIEL";
		else
			result = "RICHARD";

		cout<<"Case #"<<i<<": "<<result<<endl;
	}

	return 0;
}
