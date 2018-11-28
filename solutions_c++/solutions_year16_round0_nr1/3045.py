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

inline void toDigits(long long a, bool used[]){
	while(a>0){
		used[a%10] = true;
		a/=10;
	}
}

inline bool allUsed(bool used[]){
	for(int i=0; i<10; i++){
		if(!used[i]) return false;
	}
	return true;
}

long long lastNum(long long n){
	bool used[10] = {false,};
	for(long long k=1; k<101LL; k++){
		long long last = n*k;
		toDigits(last, used);
		if(allUsed(used)){
			return last;
		}
	}
	assert(false);
}

int main(){
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int ntests;
	cin>>ntests;
	for(int testnum=0; testnum<ntests; testnum++){
		long long n;
		cin>>n;
		if(n==0){
			cout<<"Case #"<<testnum+1<<": "<<"INSOMNIA"<<endl;
			continue;
		}
		long long last = lastNum(n);
		if(last==-1){
			cout<<"Case #"<<testnum+1<<": "<<"INSOMNIA"<<endl;
		}else{
			cout<<"Case #"<<testnum+1<<": "<<last<<endl;
		}
	}
	return 0;
}
