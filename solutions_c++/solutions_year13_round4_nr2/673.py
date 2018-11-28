#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <iterator>
//#include <iostream>
using namespace std;

ifstream cin("B-Large.in");
ofstream cout("B-Large.out");

long long countL(long long xc, long long N){
	long long cnt = 0;
	while(xc>=1LL){
		cnt++;
		xc--;
		xc = xc/2;
	}
	return cnt;
}
long long countW(long long yc,long long N){
	long long cnt = 0;
	long long rm = (1LL << N)-1-yc;
	while(rm>=1LL){
		cnt++;
		rm--;
		rm = rm/2;
	}
	return cnt;
}
bool mustrec(long long xc, long long P, long long N){
	long long nL = countL(xc,N);
	long long z = (1LL<<nL)-1;
	z = (z << (N-nL));
	return(z<=P);

}
bool canrec(long long yc, long long P,long long N){
	long long nL = countW(yc,N);
	long long z = (1LL<<(N-nL))-1;	
	return(z<=P);
}
long long solvex(long long N, long long P){
	long long lb = 0;
	long long ub = (1LL << N) -1;
	while(ub-lb>1){
		long long mid = (lb+ub)/2;
		if(mustrec(mid,P,N)){
			lb = mid;
		}
		else ub = mid;
	}
	if(mustrec(ub,P,N)) return ub;
	else return lb;
}
long long solvey(long long N, long long P){
	long long lb = 0;
	long long ub = (1LL << N) -1;
	while(ub-lb>1){
		long long mid = (lb+ub)/2;
		if(canrec(mid,P,N)){
			lb = mid;
		}
		else ub = mid;
	}
	if(mustrec(ub,P,N)) return ub;
	else return lb;
}

int main(){
	long long T;
	cin >> T;
	for(long long t=0;t<T;t++){
		long long N;
		long long P;
		cin >> N;
		cin >> P;
		
		long long x = solvex(N,P-1);
		long long y = solvey(N,P-1);
		cout << "Case #" << t+1 << ": " << x <<" " << y << endl;

	}
	system("pause");
	return 0;
}