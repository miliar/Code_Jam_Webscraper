#include <fstream>
#include <math.h>
#include <vector>
using namespace std;

void plusnum(int* num){
	int i = 1;
	while (i < 16){
		if (num[i] == 0){
			num[i] = 1;
			for (int j = 1; j < i; j++) num[j] = 0;
			return;
		}
		i++;
	}
	return;
}

long long account(int* num, int p){
	long long x = 1,s = 0;
	for (int i = 0; i < 16; i++){
		s = s + num[i] *x;
		x = x *p;
	}
	return s;
}

long long isprime(long long s){
	for (long long i = 2; i <= sqrt(s);i++)
		if (s % i == 0) return i;
	return -1;
}


int main(){
	int t,n,j;
	ifstream in("C-small-attempt0.in");
	ofstream out("jamcoin.out");
	in >> t >>n >> j;
	int num[16] ;
	int  result = 0;
	num[0] = 1; num[15] = 1;
	long long s, x;
	vector<int> q;
	out << "Case #1:" << endl;
	while (result < j){
		plusnum(num);
		q.clear();
		for (int i = 2; i <= 10; i++){
			s = account(num,i);
			x = isprime(s);
			if (x == -1) break; else q.push_back(x);
		}
		if (q.size() == 9) {
			for (int i = 15; i >=0; i--) out << num[i];
			out << ' ';
			for (int i = 0; i < 9;i++) out << q[i] << ' ' ;
			out << endl;
			result++;
		}
	}
	
}
