/*
 * cjb.cpp
 *
 *  Created on: 2013/04/13
 *      Author: DO
 */

#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstdlib>
#include<vector>
#include<string>
#include<stack>
#include<queue>
#include<deque>
#include<set>
#include<map>
#include<algorithm>
#include<functional>
#include<utility>
#include<cmath>
#include<complex>
#include<iomanip>

using namespace std;

#define REP(i,s,e) for(int i=int(s);i<=int(e);i++)
#define rep(i,n) for(int i=0;i<int(n);i++)
#define pi 3.14159265358979


int main(void){

	int t,n,m;
	cin >> t;
	rep(i,t){
		cin >> n >> m;

		int a[n][m],b[n][m];
		rep(j,n){
			rep(k,m){
		cin >> a[j][k];
		b[j][k]=0;
		}
		}

		rep(j,n){
			vector<int>v1;
			rep(k,m) v1.push_back(a[j][k]);
			sort(v1.begin(),v1.end());
				rep(l,m){
					if(a[j][l]!=v1[m-1]) b[j][l]=-1;
			}
		}

		rep(j,m){
			vector<int>v2;
			rep(k,n) v2.push_back(a[k][j]);
			sort(v2.begin(),v2.end());
				rep(l,n){
					if(a[l][j]==v2[n-1] && b[l][j]==-1) b[l][j]=0;

			}
		}

		bool f=false;
		rep(j,n){
			rep(k,m){
		       if(b[j][k]==-1){
			   f=true;
		       break;
			}
			}
			if(f) break;
		}


		if(f) cout << "Case #" << i+1 << ": " << "NO" << endl;
		else cout << "Case #" << i+1 << ": " << "YES" << endl;

	}

	return 0;
}


