#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <sstream>

using namespace std;

string int2str(int i){
	stringstream ss;
	ss << i;
	return ss.str();
}

int str2int(string s) {
	int res;
	stringstream ss;
	ss << s; ss >> res;
	return res;
}

int main () {
	vector<int> v,vsq,vres;
	map<int,bool> esPalin,esDoble;
	for (long long i =1 ; i <= 10000; ++i) {
		string curr = int2str(i);
		string rev  = string(curr.rbegin(),curr.rend());
		if (i == str2int(rev)) {
			v.push_back(i);
			esPalin[i] = true;
		}
	}
	for (int i = 0 ; i < v.size(); ++i) {
		if (esPalin[v[i]]&&esPalin[v[i]*v[i]])
			esDoble[v[i]*v[i]] = true;
	}
	
	int acum = 0;
	for (int i = 0; i <= 1000; ++i) {
		if (esDoble.find(i) != esDoble.end()) ++acum;
		vres.push_back( acum );
	}
	int T,A,B;
	cin >> T;
	for (int i = 1 ; i <= T ; ++i) {
		cin >> A >> B;
		cout << "Case #" << i << ": " << (vres[B]-vres[A-1]) << endl;
	}
	return 0;
}