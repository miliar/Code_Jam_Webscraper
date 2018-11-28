#include<iostream>
#include<vector>
#include<stack>
#include<string.h>
#include<map>
using namespace std;
long long getLen(long long val){
	if(!val) return 0;
	long long cnt = 0;
	while(val != 0){
		cnt ++;
		val /=2;
	}
	return cnt;
}
long long getFirst(long long len){
	return (1 << (len - 1)) + 1;
}
string getBinaryRep(long long val){
	string rRet;
	while(val != 0){
		rRet += ('0' + (val%2));
		val /= 2;
	}
	return string(rRet.rbegin(), rRet.rend());
}
long long getValInBase(long long val, long long base){
	long long ret = 0;
	long long mult = 1;
	while(val > 0){
		ret += mult*(val%2);
		val /= 2;
		mult *= base;
	}
	return ret;
}
long long reverseVal(long long val){
	string bin = getBinaryRep(val);
	long long ret = 0;
	for(int i = bin.size() - 1; i >= 0; -- i){
		ret = ret*2 + (bin[i] -'0');
	}
	return ret;
}
map<long long, long long> mp;
int j;
void recurse(long long left, long long curr, long long len, long long val, long long base){
	if(!j || getLen(base + curr) > getLen(base))
		return;
	if(left < len){
		curr = (curr << (left + len));
		if(mp.count(base + curr) == 0){
			j--;
			mp[base+curr] = val;
		}
		return;
	}
	recurse(left - 1, curr << 1, len, val, base);
	recurse(left - len, (curr << len) + val, len, val, base);
} 
int main(){
	int t;
	long long n;
	cin >> t >> n >> j;
	cout << "Case #1:" << endl;
	long long start = getFirst(n);
	long long val = 3;
	while(j && getLen(val)*2 <= n){
		long long len = getLen(val);
		start = val + (val << (n-len));
		recurse(n - len*2, 0, len, val, start);
		val += 2;
	}
	map<long long, long long> :: iterator it;
	int out = 0;
	for(it = mp.begin(); it != mp.end(); ++ it){
		cout << getBinaryRep(it->first);
		for(int i = 2; i < 11; ++ i){
			cout << ' ' << getValInBase(it->second, i);
		}
		cout << endl;
		out ++;
	}
	return 0;
}