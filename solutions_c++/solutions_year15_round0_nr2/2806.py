/*
 * b.cpp
 *
 *  Created on: 2015/04/11
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
typedef pair<int,int> P;
typedef long long ll;

int main(void){

	int T;
	cin >> T;
	REP(t,T){

		int D;
		cin >> D;
		vector<int>plate;
		REP(i,D){
			int x;
			cin >> x;
			plate.push_back(x);
		}


		sort(plate.begin(),plate.end());


		if(plate[D-1]<=3) cout << "Case #" << t+1 << ": " << plate[D-1] << endl;
		else{

		int mx=plate[D-1];

		int i,j;
		int ans=1e9;
		for(i=1;i<=mx;i++){

			vector<int>:: iterator a;
			a=upper_bound(plate.begin(),plate.end(),i);

			int c=0;
			for(j=a-plate.begin();j<D;j++){
				if(plate[j]>i){
					c+=(plate[j]+i-1)/i-1;
				}
			}

			ans=min(ans,c+i);

		}



		cout << "Case #" << t+1 << ": " << ans << endl;


		}



	}


	return 0;
}



