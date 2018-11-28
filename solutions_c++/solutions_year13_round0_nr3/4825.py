#include <iostream>
#include <vector>
#include <cstdio>
#include <string>
#include <sstream>
#include <cstring>
#include <climits>
#include <algorithm>

typedef unsigned long long ull;

using namespace std;

int main(){

	vector<ull> par, fair;
	ull A, B, i, tmp;
	int t, T, cnt;
	
	string str, rstr;
	
	for(i=1; i<10000; ++i){
		
		stringstream ss;
		ss << i;
		ss >> str;
		rstr = string(str.rbegin(), str.rend());
		
		if(str == rstr)
			par.push_back(i);
	}
	
	for(t=0; t<par.size(); ++t){
		
		tmp = par[t]*par[t];
		
		if(binary_search(par.begin(), par.end(), tmp)){
			fair.push_back(tmp);
		}
	}
	
	scanf("%d", &T);
	
	vector<ull>::iterator lo, hi;
	
	for(t=1; t<=T; ++t){
	
		cin>>A>>B;
		
		cnt = 0;
		
		for(int j=(int)(lower_bound(fair.begin(), fair.end(), A) - fair.begin());
			(j<fair.size()&&fair[j]<=B); j++){
			cnt++;
		}
			
		printf("Case #%d: %d\n", t, cnt);
	}
		
	return 0;
}