#include <bits/stdc++.h>
using namespace std;
#define ull unsigned long long int
std::string dec2bin(ull n)
{
    std::string res;
    while (n)
    {
        res.push_back((n & 1) + '0');
        n >>= 1;
    }
    if (res.empty())
        res = "0";
    else
        std::reverse(res.begin(), res.end());
   return res;
}

ull ipow(int base, int exp)
{
    ull result = 1;
    while (exp)
    {
        if (exp & 1)
            result *= base;
        exp >>= 1;
        base *= base;
    }

    return result;
}
ull con(const char * s, int b){
	int l=strlen(s), i; ull sum =0;
	for (i = l-1; i>=0;i--)	sum += (s[i]-'0')*ipow(b, l-i-1);
	return sum;
}
bool prime(ull n) {
	if (n<2) return false;
	if (n<=3) return true;
	if (!(n%2) || !(n%3)) return false;
	for (int i=5;i*i<=n;i+=6)
		if (!(n%i) || !(n%(i+2))) return false;
	return true;
}
int firstDivisor(ull n){
	for (ull i = 2; i < n; i++){
		if (n % i == 0) return i;
	}
	return -1;
}

int main(){
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	int cases, n, j; cin >> cases >> std::ws;
	for (int i = 0; i < cases; i++){
		set<string> visited;
		cin >> n >> j >> std::ws; cout << "Case #" << (i+1) << ":\n";
		ull a = ipow(2, (n-2));
		for (ull p = 0; p < a; p++){
			string jam; for (int a = 0; a < n; a++) jam+='0';
			jam[0] = '1'; jam[n-1] = '1';
			string s = dec2bin(p);
			for (int v = 0; v < s.size(); v++){
				jam[n-1-s.size() + v] = s[v];
			}
			if (visited.count(string(jam))) continue;
			bool valid = true;
			vector<int> divs; divs.reserve(500);
			for (int b = 2; b <= 10; b++){
				if (prime(con(jam.c_str(), b))){
					valid = false; 
					break;
				}else{
					int num = firstDivisor(con(jam.c_str(),b));
					if (num == -1){
						valid = false; 
						break;
					}
					divs.emplace_back(num);
				}
			}
			if (valid){
				cout << jam;
				visited.insert(string(jam));
				j--;
				for (int x = 0; x < divs.size(); x++) cout << " " << divs[x];
				cout << "\n";
				if (j == 0) break;
			}
		}
	}
	return 0;
}