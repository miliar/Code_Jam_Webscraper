/*
 * a.cpp
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

int a[10][10];
int b[10][10];

int main(void){

	int T;
	cin >> T;
	REP(i,T){
		int r;
		cin >> r;

		int j,k;
		for(j=1;j<=4;j++){
			for(k=1;k<=4;k++){
				cin >> a[j][k];
			}
		}

		int s;
		cin >> s;

		for(j=1;j<=4;j++){
			for(k=1;k<=4;k++){
				cin >> b[j][k];
			}
		}

		int c=0,n;
		for(j=1;j<=4;j++){
			for(k=1;k<=4;k++){
				if(a[r][j]==b[s][k]){
					c++; n=a[r][j];
				}
			}
		}

		if(c==0) cout << "Case #" << i+1 << ":" << ' ' << "Volunteer cheated!" << endl;
		else if(c==1) cout << "Case #" << i+1 << ":" << ' ' << n << endl;
		else cout << "Case #" << i+1 << ":" << ' ' << "Bad magician!" << endl;

	}

	return 0;
}



