#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <math.h>
#include <hash_set>
#include <algorithm>
#include <map>
#include <set>
#include <stack>
 
#define _USE_MATH_DEFINES
#define TASK "secure"
 
using namespace std;


int main(){
	freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	bool ok;
	for(int t=0; t<T; ++t){
		int n;
		cin >> n;
		vector<string>vec(n);
		vector<vector<int>>reps(n);
		vector<vector<char>>blocks(n);
		for(int i=0; i<n; ++i){
			cin >> vec[i];
		}
		int num=0;
		for(int i=0; i<n; ++i){
			num=1;
			int j=1;
			for(j=0; j<vec[i].size(); ++j){
				num=1;
				while(j+1<vec[i].size() && vec[i][j]==vec[i][j+1]){
					j++;
					num++;
				}
				blocks[i].push_back(vec[i][j]);
				reps[i].push_back(num);
			}
			/*if(j<vec[i].size()){
				blocks[i].push_back(vec[i][j]);
				reps[i].push_back(num);
			}*/
		}
		int bsize=blocks[0].size();
		ok=true;
		for(int i=0; i<n; ++i){
			if(blocks[i].size() != bsize)ok=false;
		}
		if(!ok){
			cout << "Case #" << t+1 << ": " << "Fegla Won" << endl;
			continue;
		}
		for(int i=1; i<n; ++i){
			for(int j=0; j<bsize; ++j){
				if(blocks[i][j]!=blocks[0][j])ok=false;
			}
		}
		if(!ok){
			cout << "Case #" << t+1 << ": " << "Fegla Won" << endl;
			continue;
		}
		int res=0;
		int res1=99999999;
		int curr=0;
		for(int j=0; j<bsize; ++j){
			res1=99999999;
			curr=0;
			for(int i=1; i<1000; ++i){
				curr=0;
				for(int k=0; k<n; ++k){
					curr+=abs(i-reps[k][j]);
				}
				if(curr < res1)res1=curr;
			}
			res+=res1;
		}
		cout << "Case #" << t+1 << ": " << res << endl;
	}





	return 0;
}