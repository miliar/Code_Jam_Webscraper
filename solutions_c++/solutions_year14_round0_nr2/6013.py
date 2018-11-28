/*
 * b.cpp
 *
 *  Created on: 2014/04/12
 *      Author: DO
 */

#include<iostream>
#include<sstream>
#include<fstream>
#include<string>
#include<vector>
#include<deque>
#include<queue>
#include<stack>
#include<set>
#include<map>
#include<algorithm>
#include<functional>
#include<utility>
#include<bitset>
#include<cmath>
#include<cstdlib>
#include<ctime>
#include<cstdio>

using namespace std;

#define REP(i,n) for(int i=0;i<int(n);i++)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
typedef long long ll;

int main(void){

	int T;
	cin >> T;
	REP(i,T){

		double C,F,X;
		cin >> C >> F >> X;
		double cookie=2.0,ans=0.0;
		while(1){
			double a=C/cookie,b=X/(cookie+F),c=X/cookie;
			if(a+b>=c){
				ans+=c; break;
			}else{

				ans+=a; cookie+=F;

			}
		}

		cout << "Case #" << i+1 << ":" << ' ';
		cout.precision(10);
		cout << fixed << ans << endl;
	}


	return 0;
}



