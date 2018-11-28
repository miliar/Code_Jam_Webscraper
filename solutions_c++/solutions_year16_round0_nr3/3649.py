#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

const int PNum = 100001000;

int T, N, J;
bool coin[35];
bool isP[PNum];
vector <int> prime;

void input(){
	scanf("%d%d", &N, &J);
	coin[0] = coin[N - 1] = 1;
}

void output(vector<int> & v){
	cerr << "One Found !" << endl;
	for (int i = N - 1; i >= 0; --i){
		printf ("%d", coin[i]);
	}
	for (int i = 0; i < v.size(); ++i){
		printf(" %d", v[i]);
	}
	printf("\n");
}

void add(){
	bool s = true;
	int j = 1;
	while (s){
		if (coin[j]){
			s = true;
			coin[j] = false;
		} else {
			s = false;
			coin[j] = true;
		}
		++j;
	}
}

bool isPrime(long long num){
	if (num < PNum){
		return isP[PNum];
	}
	return false;
}

int isntPrime(int base){
	long long fact = 1;
	long long num = 0;
	for (int i = 0; i < N; ++i){
		if (coin[i]){
			num += fact;
		}
		fact *= (long long) base;
	}
//	if (!isPrime(num))
//		return 0;
	for (int i = 0; i < prime.size(); ++i){
		if (!(num % prime[i])){
			if (num / prime[i] != 1)
				return prime[i];
		}
	}
	return 0;
}

bool prove(){
	vector<int> v;
	for (int i = 2; i <= 10; ++i){
		int d = isntPrime(i);
		if (d){
			v.push_back(d);
		}
	}
	if (v.size() == 9){
		output(v);
		return true;
	}
	return false;
}

void eratos(){
	for (int i = 2; i < PNum; ++i){
		if (!isP[i]){
			prime.push_back(i);
			for (int j = 2 * i; j < PNum; j += i){
				isP[j] = true;
			}
		}
	}
}

void output(int t){
	eratos();
	cerr << "End of Eratosthenes" << endl;
	printf ("Case #%d: \n", t);
	for (int j = 0; j < J && !coin[N]; ){
		if (prove()){
			++j;
		}
		add();
	}
}

int main(){
	freopen ("c.in", "r", stdin);
	freopen ("out.txt", "w", stdout);
	scanf ("%d", &T);
	for (int i = 1; i <= T; ++i){
		input();
		output(i);
	}
	return 0;
}