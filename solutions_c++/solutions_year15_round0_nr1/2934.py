/*
 * a.cpp
 *
 *  Created on: 2015/04/05
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

		int mx;
		string s;
		cin >> mx >> s;
		int sum=0,ad=0;
		if(s[0]-'0'==0){
			ad++; sum=1;
		}else{
			sum+=s[0]-'0';
		}

		int i;
		for(i=1;i<=mx;i++){
			if(i<=sum) sum+=s[i]-'0';
			else{
				if(s[i]-'0'!=0){
					ad+=i-sum;
					sum+=i-sum+s[i]-'0';
				}
			}
		}



		cout << "Case #" << t+1 << ": " << ad << endl;

	}


	return 0;
}



