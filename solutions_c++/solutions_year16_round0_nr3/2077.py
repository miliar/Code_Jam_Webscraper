#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define mp make_pair
#define SZ(v) ((int)((v).size()))

int N = 6;
int J = 3;

long long get(vector<long long> v){
	long long res = 0;
	for (int i=(int)(v.size() - 1); i>=0; i--){
		res *=2;
		res += v[i];
	}
	return res;
}

long long divs(long long a){
	for (long long i=3; i<=sqrt(a); i+=2){
		if (a % i == 0)
			return i;
	}
	return 1;
}

vector<long long> display(){
	vector<long long> sol;
	sol.pb(3); //2
	sol.pb(2); //3
	sol.pb(3); //4
	sol.pb(2); //5
	sol.pb(7); //6
	sol.pb(2); //7
	sol.pb(3); //8
	sol.pb(2); //9
	sol.pb(3); //10
	return sol;
}


bool check(vector<long long> v, long long div, long long base){
	long long p = 1;
	long long curr = 0;
	for (int i=(int)(v.size()-1); i>=0; i--){
		curr += p * v[i];
		curr %= div;
		p *= base;
	}
	return curr == 0;
}
	

void gen(vector<long long> &v, int pos, int nb_ones){
	if (J == 0)
		return;
	if (pos == N - 1){
		if (nb_ones % 6 != 0)
			return;
		int mod3 = 0;
		int mod7 = 0;
		for (int i=0; i < SZ(v); i++){
			int add = 1;
			if ((i + 1) % 2 != 0)
				add = -1;
			if (v[i] == 1){
				mod3 += add;
				mod7 += add;
			}
		}
		if (mod3 % 3 != 0 || mod7 % 7 != 0)
			return;
		for (long long e : v){
			cout << e;
		}
		J--;
		vector<long long> divs = display();
		for (unsigned int i=0; i<divs.size(); i++){
			/*if (!check(v, divs[i], i+2)){
				cout << "ERROR" << endl << divs[i] << endl;
				exit(0);
				return;
			}*/
			cout << " " << divs[i];
		}
		cout << endl;
		return;
	}
	v[pos] = 0;
	gen(v, pos + 1, nb_ones);
	v[pos] = 1;
	gen(v, pos + 1, nb_ones + 1);
}


int main(){
	int T;
	cin >> T >> N >> J;
	cout << "Case #1:" << endl;
	vector<long long> v = vector<long long>(N, 1);
	gen(v, 1, 2);
	//cout << J;
}			

