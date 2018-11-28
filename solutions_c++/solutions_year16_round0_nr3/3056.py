#include <bits/stdc++.h>
using namespace std;

vector <int> v;
vector <int> dziel;

void rozbij (long long x) {
	while (x!=0) {
		if (x%2==0) v.push_back (0);
		else v.push_back (1);
		x/=2;
	}
	reverse (v.begin(), v.end());
}

long long liczba (long long p) {
	long long pot=1;
	long long res=0;
	for (int i=0; i<v.size(); i++) {
		if (v[i]==1) res+= pot;
		pot*=p;
	}
	return res;
}

int  pierwszosc (long long x) {
	int pier= sqrt (x);
	for (int i=2; i<=pier+1 ; i++) {
		if (x % i ==0) return i;
	}
	return -1;
}

void wypisz () {
	for (int i=v.size()-1; i>=0; i--) cout << v[i];
	cout << " ";
	for (int i=0; i<dziel.size(); i++) cout << dziel[i] << " ";
	cout << "\n";
}

int main () {
	int n, c,  J, ile=0;
	cin >> c >> n >> J;
	cout << "Case #1:\n";
	for (long long i= (1<<(n-1))+1; i< (1<<n); i+=2) {
		rozbij (i);
		bool ok=true;
		for (long long p=2; p<=10; p++) {
			long long x= liczba (p);
			int dzielnik=pierwszosc (x);
			if (dzielnik==-1) {
				ok=false;
				break;
			}
			dziel.push_back (dzielnik);
			
		}
		if (ok==true) {
			ile++;
			wypisz ();
		}
		v.clear();
		dziel.clear();
		if (ile==J) break;
	}
}