#include <bits/stdc++.h>
using namespace std;

#define FOR(i, a, b) for(int i = a; i < b; ++i)
#define FORR(i, n) FOR(i, 0, n)
typedef pair<bool, int> bi;
typedef long long ll;
bi isPrime(ll n) {
	n = abs(n); // números negativos
	if(n < 3) return bi(n == 2LL, n);	// casos especiais
	if((n % 2LL) == 0) return bi(false, 2); // números pares

	for(ll i = 3LL; i*i <= n; i += 2LL)	// caso geral
		if(n % i == 0) return bi(false, i);
	return bi(true, n);
}

ll converte(string num, ll base) {
	ll valor = num[0]-'0';
	int j = 0;
	while(j < 15) {
		j++;
		valor *= base;
		valor += num[j]-'0';
	}
	return valor;
}

string toBinary(ll n) {
	string s;
	while(n) {
		s += n%2+'0';
		n /= 2;
	}
	reverse(s.begin(), s.end());
	return s;
}

int main() {
	printf("Case #1:\n");
	int n, falta = 50, t;
	scanf("%d", &t);
	scanf("%d %d", &t, &falta);
	bool ok = true;
	vector<int> vec(9, 0);
	for(n = 32769; n <= 65535; n += 2) {
		string snum = toBinary(n);
		//cerr << "convertendo " << snum << " para " << converte(snum, 10) << endl;
		ok = true;
		FOR(i, 2, 11) {
			bi res = isPrime(converte(snum, i));
			if(res.first) {
				ok = false;
				break;
			}
			else vec[i-2] = res.second;
		}
		if(ok) {
			falta--;
			printf("%s", snum.c_str());
			FORR(i, 9) printf(" %d", vec[i]);
			printf("\n");
			if(falta == 0) break;
		}
	}
	return 0;
}
