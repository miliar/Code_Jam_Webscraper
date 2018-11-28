#include <iostream>
#include <cstdio>
#include <cstring>
#include <fstream>

using namespace std;
ifstream fin("B-large.in");
ofstream fout("B.large.txt");

long long q1(long long v, int l){
	long long r = 0, s = v;
	while (s > 0){
		--l;
		r += (1ll << l);
		s = (s - 1) >> 1;
	}
	return r + 1;
}

long long q2(long long v, int l){
	long long r = 0, s = (1ll << l) - v - 1;
	for (int i = 0; i < l; ++i){
		if (s == 0)
			r += 1ll << (l - 1 - i);
		else 
			s = (s - 1) >> 1;
	}
	return r + 1;
}

int main(){
/*
for (int i = 0; i < 16; ++i)
		cout << q1(i, 4) <<" ";
	cout << endl;
	for (int i = 0; i < 16; ++i)
		cout << q2(i, 4) <<" ";
	cout << endl;
	*/
//	cout << q2(253, 8) << endl;
	int test;
	fin >> test;
	for (int i = 1; i <= test; ++i){
		fout << "Case #" << i << ": ";
		long long ret = 0, n, p;

		fin >> n >> p;
		long long l = 0, r = (1ll << n) - 1;
		while (l != r){
			long long mid = (l + r + 1) >> 1;
			if (q1(mid, n) <= p)
				l = mid;
			else r = mid - 1;
		}
		fout << r << " ";
		
		l = 0;
		r = (1ll << n) - 1;
		while (l != r){
			long long mid = (l + r + 1) >> 1;
			if (q2(mid, n) <= p)
				l = mid;
			else
				r = mid - 1;
		}
		fout << r << endl;
	}
	system("pause");
	return 0;
}