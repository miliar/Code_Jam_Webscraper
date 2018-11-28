#include<bits/stdc++.h>
#define endl '\n'
#define pb push_back
#define pii pair<int, int>
#define mp make_pair
#define ll long long
#define ld long double
using namespace std;

int getDigitsMask(int x){
	if(x==0) return 1;
	int res = 0, digit;
	while(x != 0){
		digit = x%10;
		res |= (1 << digit);
		x /= 10;
	}
	return res;
}

int main(){
	ios_base::sync_with_stdio(0);
	int ncases, caseNumber = 1;
	ll n;
	cin >> ncases;
	while(ncases--){
		cin >> n;
// 		cout << getDigitsMask(n) << endl;
		
		if(n == 0){
			cout << "Case #" << caseNumber << ": INSOMNIA" << endl;
			caseNumber++;
			continue;
		}
		
		ll res = n;
		int mask = getDigitsMask(n);
		while(mask != 1023){
			res += n;
			mask |= getDigitsMask(res);		
// 			cout << "n: " << res << " mask: " << mask << endl;
		}
		
		cout << "Case #" << caseNumber << ": " << res << endl;
		caseNumber++;
	}
	return 0;
}