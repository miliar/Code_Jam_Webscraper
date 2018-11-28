#include <iostream>
#include <fstream>
#include <conio.h>
#include <stdio.h>
#define _USE_MATH_DEFINES
#include <algorithm>
#include <climits>
#include <bitset>
#include <math.h>
#include <string>
#include <vector>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <map>
#include <set>
using namespace std;

int main(){
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	int t;
	bool ok;
	cin >> t;
	int n,m;
	vector<vector<int>>vec;
	for(int k=0; k<t; ++k){
		scanf("%d%d", &n,&m);
		vec.clear();
		vec.resize(n,vector<int>(m));
		int ones=0,twos=0;
		for(int i=0; i<n; ++i){
			for(int j=0; j<m; ++j){
				scanf("%d", &vec[i][j]);
				if(vec[i][j]==1)ones++;
				else twos++;
			}
		}
		set<pair<int,int>>a,b;
		ok = true;
		for(int i=0; i<n; ++i){
			if(vec[i][0]==1){
				ok = true;
				for(int j=1; ok && j<m; ++j){
					if(vec[i][j]!=vec[i][j-1])ok=false;
				}
				if(ok){
					for(int j=0; j<m; ++j) a.insert(make_pair(i,j));
				}
			}
			else{
				ok = true;
				for(int j=1; ok && j<m; ++j){
					if(vec[i][j]!=vec[i][j-1])ok=false;
				}
				if(ok){
					for(int j=0; j<m; ++j) b.insert(make_pair(i,j));
				}
			}
		}

		for(int i=0; i<m; ++i){
			if(vec[0][i]==1){
				ok = true;
				for(int j=1; ok && j<n; ++j){
					if(vec[j][i]!=vec[j-1][i])ok=false;
				}
				if(ok){
					for(int j=0; j<n; ++j) a.insert(make_pair(j,i));
				}
			}
			else{
				ok = true;
				for(int j=1; ok && j<n; ++j){
					if(vec[j][i]!=vec[j-1][i])ok=false;
				}
				if(ok){
					for(int j=0; j<n; ++j) b.insert(make_pair(j,i));
				}
			}
		}
		cout << "Case #" << k+1 << ": ";
		if(a.size()==ones){
			printf("YES\n");
		}
		else{
			printf("NO\n");
		}
	}

	return 0;
}