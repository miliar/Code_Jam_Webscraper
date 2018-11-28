//============================================================================
// Name        : codejamR1B-A.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <set>
#include <utility>
#include <algorithm>
#include <stdlib.h>
#include <string.h>
#include <sstream>
#include <iterator>

using namespace std;


int solve(){
	int A, N;
	cin>>A>>N;

	vector<int> sizes;
	sizes.push_back(0);
	for(int i=0; i<N; ++i){
		int s;
		cin>>s;
		sizes.push_back(s);
	}
	if(A == 1){
		return N;
	}
	sort(sizes.begin(), sizes.end());
	vector<int> need;
	need.push_back(0);
	int cur = A;
	for(int i=1; i<N+1; ++i){
		if(sizes[i]<cur){
			need.push_back(need[i-1]);
			cur+=sizes[i];
		}else{
			int x = 1;
			int il = 0;
			double rel = (double)(sizes[i]-1)/(double)(cur-1);
			while(rel >= x){
				il++;
				x<<=1;
			}
			cur = x*cur - x + 1 + sizes[i];
			need.push_back(need[i-1]+il);
		}
		//cout<<cur<<" "<<need[i]<<endl;
	}
	int min = 1000;
	for(int i=N; i>=0; --i){
		int v = need[i]+N-i;
		if(v < min){
			min = v;
		}
	}
	return min;
}


int main() {
	int T;
	cin>>T;
	for(int i=0; i<T; ++i){
		int ans = solve();
		cout<<"Case #"<<i+1<<": "<<ans<<endl;
	}
	return 0;
}
