#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cstdio>
#include <vector>
#include <string>
#include <cassert>
#include <fstream>
#include <iomanip>
#include <cstdlib>
#include <numeric>
#include <sstream>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <cassert>
using namespace std;

long long myPow(long long a, int b){
	long long rez = 1;
	for(int i=0; i<b; i++){
		rez*=a;
	}
	return rez;
}

int main(){
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int ntests;
	cin>>ntests;
	for(int testnum=0; testnum<ntests; testnum++){
		int K, C, S;
		cin>>K>>C>>S;
		assert(K==S);
		long long kc = myPow(K,C-1);
		cout<<"Case #"<<testnum+1<<":";
		for(int i=0; i<S; i++) cout<<' '<<(kc*i+1);
		cout<<endl;
	}
	return 0;
}
