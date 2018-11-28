#include <iostream>
#include <ostream>
#include <sstream>
#include <string>
#include <cmath>
#include <vector>
using namespace std;

string NumberToString ( int a ){
	stringstream ss;
	ss << a;
	return ss.str();
}

bool es_palindrom(int a){
	string s = NumberToString(a);
	for(int i=0; i < (s.size()/2); ++i)
		if(s[i] != s[s.size()-1-i]) return false;

	return true;
}

int main(){
	int n;
	cin >> n;

	vector<int> memoria(32,-1);

	for(int k = 0; k < n; ++k){
		int inf, sup;
		cin >> inf >> sup;
		inf = (int)sqrt(inf-1)+1;
		sup = (int)sqrt(sup);
		int con = 0;
		for(int i = inf; i <= sup; ++i){
			if(memoria[i-1] == -1){
				if(es_palindrom(i)){
					if(es_palindrom(i*i)){
						memoria[i-1] = 1;
						++con;
					}
					else memoria[i-1] = 0;
				}
				else memoria[i-1] = 0;
			}
			else if(memoria[i-1] == 1) ++con;
		}
		cout << "Case #" << k + 1 << ": " << con << endl;
	}
}
