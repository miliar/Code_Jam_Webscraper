#include <iostream>
#include <fstream>
#include <vector>
#include <array>
#include <math.h>
#include <map>
#include <string>
using namespace std;
typedef unsigned int Uint;
std::pair<long long, long long> getNumbers(string s);

int main(){
	ifstream in("in.txt");
	ofstream out("out.out");
	int n;
	in >> n;
	for (int i = 0; i < n; ++i){
		string s;
		in >> s;
		pair<long long, long long> h(getNumbers(s));
		long long P = h.first;
		long long Q = h.second;
		if (Q % P == 0){
			Q /= P;
			P = 1;
		}
		long long t = Q;
		while (t % 2 == 0)
			t /= 2;
		if (t != 1)
			out << "Case #" << i + 1 << ": impossible" << endl;
		}
		else{
			int n = 0;
			while (Q > P){
				P *= 2;
				n++;
			}
			out << "Case #" << i + 1 << ": " <<n<< endl;
		}
	}

}

std::pair<long long, long long> getNumbers(string s){
	pair<long long, long long> res;
	string t1;
	string t2;
	int i = 0;
	while (s[i] != '/'){
		t1.push_back(s[i]);
		++i;
	}
	++i;
	while (i != s.size()){
		t2.push_back(s[i]);
		++i;
	}
	long long p = 0, q = 0;
	int n = t1.size();
	for (int j = 0; j < n; j++){
		p += powl(10, n-1-j)*(t1[j] - '0');
	}
	n = t2.size();
	for (int j = 0; j < n; j++){
		q += powl(10, n-1-j)*(t2[j] - '0');
	}

	res.first = p;
	res.second = q;
	return res;
}