#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define mp make_pair
#define SZ(v) ((int)((v).size()))
#define LE(s) ((int)((s).size()))

typedef __int128 ll;

ll BIG = 100000000000LL;
ll solA, solB;
ll difference;
string a, b;

ll absol(ll nb){
	if (nb < 0)
		return (-nb);
	return nb;
}

void res(ll ta, ll tb){
	if (absol(ta - tb) < difference){
		difference = absol(ta - tb);
		solA = ta;
		solB = tb;
	}
	if (absol(ta - tb) == difference){
		if (ta < solA){
			solA = ta;
			solB = tb;
		}
		if (ta == solA && tb < solB){
			solB = tb;
		}
	}
}

void show(ll nb, int len){
	stack<int> s;
	while (nb > 0){
		s.push((int)(nb%10));
		nb /= 10;
	}
	for (int i = 0; i< len - ((int)(s.size())); i++){
		cout << "0";
	}
	while (!s.empty()){
		cout << s.top();
		s.pop();
	}
}


void recurse(ll diff, int ind, ll _a, ll _b){
	//show(_a, 10);
	//cout << endl;
	//show(_b, 10);
	//cout << endl;
	if (ind == LE(a)){
		res(_a, _b);
		return;
	}
	if (a[ind] == '?' && b[ind] == '?'){
		if (diff == 0){
			ll cpa = 10*_a + 0;
			ll cpb = 10*_b + 0;
			recurse(0, ind + 1, cpa, cpb);
			cpa = 10*_a + 1;
			cpb = 10*_b + 0;
			recurse(1, ind + 1, cpa, cpb);
			cpa = 10*_a + 0;
			cpb = 10*_b + 1;
			recurse(-1, ind + 1, cpa, cpb);
		}
		else if (diff < 0){
			ll cpa = 10*_a + 9;
			ll cpb = 10*_b + 0;
			recurse(10*diff + 9, ind + 1, cpa, cpb);
		}
		else {
			ll cpa = 10*_a + 0;
			ll cpb = 10*_b + 9;
			recurse(10*diff - 9, ind + 1, cpa, cpb);
		}
	}
	else if (a[ind] == '?'){
		ll dig = b[ind] - '0';
		//show(dig, 10);
		//cout << endl;
		if (diff == 0){
			{
				ll cpa = 10*_a + dig;
				ll cpb = 10*_b + dig;
				recurse(0, ind + 1, cpa, cpb);
			}
			if (dig > 0){
				ll cpa = 10*_a + dig - 1;
				ll cpb = 10*_b + dig;
				recurse(-1, ind + 1, cpa, cpb);
			}
			if (dig < 9){
				ll cpa = 10*_a + dig + 1;
				ll cpb = 10*_b + dig;
				recurse(1, ind + 1, cpa, cpb);
			}
		}
		else if (diff < 0){
			ll cpa = 10*_a + 9;
			ll cpb = 10*_b + dig;
			recurse(10*diff + 9 - dig, ind + 1, cpa, cpb);
		}
		else{
			ll cpa = 10*_a;
			ll cpb = 10*_b + dig;
			recurse(10*diff - dig, ind + 1, cpa, cpb);
		}
	}
	else if (b[ind] == '?'){
		ll dig = a[ind] - '0';
		//show(dig, 10);
		//cout << endl;
		if (diff == 0){
			{
				ll cpb = 10*_b + dig;
				ll cpa = 10*_a + dig;
				recurse(0, ind + 1, cpa, cpb);
			}
			if (dig > 0){
				ll cpa = 10*_a + dig;
				ll cpb = 10*_b + dig - 1;
				recurse(1, ind + 1, cpa, cpb);
			}
			if (dig < 9){
				ll cpa = 10*_a + dig;
				ll cpb = 10*_b + dig + 1;
				recurse(-1, ind + 1, cpa, cpb);
			}
		}
		else if (diff < 0){
			ll cpa = 10*_a + dig;
			ll cpb = 10*_b;
			recurse(10*diff + dig, ind + 1, cpa, cpb);
		}
		else{
			ll cpa = 10*_a + dig;
			ll cpb = 10*_b + 9;
			recurse(10*diff + dig - 9, ind + 1, cpa, cpb);
		}
	}
	else {
		ll diga = a[ind] - '0';
		ll digb = b[ind] - '0';
		//show(diga, 10);
		//cout << endl;
		//show(digb, 10);
		//cout << endl;
		recurse(10*diff + diga - digb, ind + 1, 10 * _a + diga, 10*_b + digb);
	}
}


int main(){
	BIG *= 10000000000LL;
	int T;
	cin >> T;
	for (int i=1; i<=T; i++){
		cin >> a >> b;
		difference = BIG;
		recurse(0, 0, 0, 0);
		cout << "Case #" << i << ": ";
		show(solA, LE(a));
		cout << " ";
		show(solB, LE(a));
		cout << endl;
	}
}		
