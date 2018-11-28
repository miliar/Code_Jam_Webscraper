#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>

typedef long long ll;

using namespace std;

void fill(set<int> &s, ll n){
	
	while(n) {
		s.insert(n % 10);
		n /= 10;
	}
}


int main(){
	
	ifstream fin;
	ofstream fout;

	fin.open("input.txt");
	fout.open("output.txt");


	
	int t;
	fin >> t;

	for(int q = 0; q < t; q++){
		ll n;
		fin >> n;
		set<int> s;

		ll num = n;
		
		while(n != 0 && s.size() < 10){
			fill(s,num);
			num += n;
		}

		if(n)
			fout << "Case #" << q + 1 << ": " << num - n << endl;
		else fout << "Case #" << q + 1 << ": INSOMNIA" << endl;
	}
	return 0;
}