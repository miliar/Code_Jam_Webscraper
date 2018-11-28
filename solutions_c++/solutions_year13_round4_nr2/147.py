#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <cstdio>
#include <cstring>
using namespace std;

#define debug(x) cerr<<#x<<"="<<(x)<<endl;

long long solve1(int N, long long P){
	if(P==(1ll<<N))
		return P-1;
	if(N==0 || P <= (1ll<<(N-1)))
		return 0;
	long long sub=solve1(N-1, P-(1ll<<(N-1)));
	return 2*(sub+1);
}

long long solve2(int N, long long P){
	if(P==(1ll<<N))
		return P-1;
	return (1ll<<N)-2-solve1(N, (1ll<<N)-P);	
}

int main(){
	int cases;
	string line;
	getline(cin, line);
	istringstream(line)>>cases;
	for(int i=1; i<=cases; i++){
		int N;
		long long P;
		scanf("%d %lld", &N, &P);
		cout<<"Case #"<<i<<": "<<solve1(N, P)<<" "<<solve2(N, P)<<endl;
	}
	return 0;
}
