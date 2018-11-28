#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <cmath>
using namespace std;
const int maxn = 10000;
bool notPrime[maxn]={};
vector<int>primes;
void getPrimes(){
	for(int i=2;i<maxn;i++){
		if(!notPrime[i]){
			primes.push_back(i);
			for(int j=i*2;j<maxn;j+=i)
				notPrime[j] = true;
		}
	}
	// for(int i=0;i<20;i++)
	// 	cerr<<primes[i]<<endl;
}
bool isPrime(int n){
	if(n<maxn)
		return !notPrime[n];
	for(int i=0;i<primes.size();i++){
		int cur = primes[i];
		if(n % cur == 0)
			return false;
		if(n/cur < cur)
			break;
	}
	return true;
}
const int testPrime = 20;
bool test(unsigned long long cur, int n, vector<int>&ans){
	for(int base = 2; base <= 10; base++){
		// if(base % 2 == 1){
		// 	ans.push_back(2);
		// 	continue;
		// }
		int flag = -1, tim = 0;
		for(int i = 1; i < testPrime; i++){
			int remain = 0;
			for(int len=n-1;len>=0;len--){
				remain = remain * base;
				if(cur & (1ULL << len))
					remain++;
				if(tim == 0 && len == 0 && remain == primes[i])
					flag = -2;
				if(remain >= primes[i])
					tim++;
				remain %= primes[i];
			}
			if(remain != 0){
			}
			else if(flag != -2){
				flag = primes[i];
				break;
			}
		}
		if(flag < 0)
			return false;
		else
			ans.push_back(flag);
	}
	return true;
}
int main(){
	getPrimes();
	int n=30, j=500;
	unsigned long long inc = 0;
	cout << "Case #1:" << endl;
	while(j){
		unsigned long long cur = (inc << 1) + 1 + (1ULL<<(n+1));
		vector<int>ans;
		// cout << inc << endl;
		if(test(cur,n+2,ans)){
			j--;
			//cout << "get one " << cur << endl;
			for(int i=n+1;i>=0;i--)
				if(cur&(1ULL<<i))
					cout << "1";
				else
					cout << "0";

			for(int i=0;i<9;i++)
				cout << " " << ans[i];
			cout << endl;
		}
		inc++;
		if(inc >= 1ULL << n)
			break;
	}
	return 0;
}