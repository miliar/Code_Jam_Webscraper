#include <iostream>
#include <string>
#include <cmath>
using namespace std;

class Number {
public:
	bool sign;
	char sym;

	Number(bool s, char sy) {
		sign = s;
		sym = sy;
	}
	Number times(Number x) {
		bool sgn = !(this->sign^x.sign);
		char symbol;
		if (this->sym=='1') {
			symbol = x.sym;
		}
		else if (x.sym=='1') {
			symbol = this->sym;
		}
		else if (this->sym==x.sym) {
			sgn = !sgn;
			symbol = '1';
		}
		else {
			int diff = (x.sym - this->sym + 3) % 3;
			symbol = 'i'+'j'+'k' - this->sym - x.sym;
			if (diff==2) {
				sgn = !sgn;
			}
		}
		return Number(sgn, symbol);
	}
};

bool check(int x, string& num) {
	Number res(true, '1');
	//bool mul = false;
	for (int i=0;i<num.size();i++) {
		Number tmp(true, num[i]);
		res = res.times(tmp);
		//if (num[i] != num[0])
		//	mul = true;
		//if (res.sign && res.sym=='i')
			//foundi = true;
	}
	if (res.sign && res.sym=='1') return false;
	string newnum = "";
	if (res.sym=='1') {
		if (x%2==0) return false;
		newnum = num+num;
	}
	else {
		if (x%2!=0 || x%4==0) return false;
		for (int i=0;i<min(4, x);i++)
			newnum += num;
	}
	int foundi = -1;
	int foundk = -1;
	res.sign = true;
	res.sym = '1';
	for (int i=0;i<newnum.size();i++) {
		Number tmp(true, newnum[i]);
		res = res.times(tmp);
		if (res.sign && res.sym=='i') {
			foundi = i + 1;
			break;
		}
	}
	if (foundi==-1) return false;
	res.sign = true;
	res.sym = '1';
	for (int i=newnum.size()-1;i>=0;i--) {
		Number tmp(true, newnum[i]);
		res = tmp.times(res);
		if (res.sign && res.sym=='k') {
			foundk = newnum.size()-i;
			break;
		}
	}
	if (foundk==-1) return false;
	return foundi+foundk <= x*num.size();
	//if (!res.sign && res.sym=='1' && x%2==0) return false;
	//if (res.sym!='1' && x%2!=0) return false;
	//if (res.sym!='1' && x%2==0 && x%4==0) return false;

	//if (!foundi) return false;
	

	//return mul;
}

int main() {
	freopen("C-small-attempt2.in", "r", stdin);
	freopen("C-small-attempt2.out", "w", stdout);

	int Tn, T;
	cin >> Tn;
	for (T=1;T<=Tn;T++) {
		bool ans = false;
		int l, x;
		string num;
		cin >> l >> x >> num;

		cout << "Case #" << T << ": " << (check(x, num)?"YES":"NO") << endl;
	}
}