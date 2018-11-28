#include <cstdlib>
#include <iostream>
#include <string>
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
//############################################################################
#include <rapidcheck.h>
using namespace rc;
// rc::check("Test", [](){ const auto i = *rc::gen::inRange(0, 10); return i < 10 && i >= 0; });
// https://github.com/emil-e/rapidcheck/
#include <boost/multiprecision/cpp_int.hpp> //MULTIPRECISION
#include <boost/foreach.hpp> //BOOST_FOREACH( single, sequence ) {}
using namespace boost::multiprecision;
//###########################################################################

bool noMaj(vector<int>& list, int n){
	for(int i = 0 ; i < list.size() ; i++){
		if((float)list[i]/(float)n > 0.5)
			return false;
	}
	return true;
}

string process(vector<int>& list){
	int number = 0;
	char rem;
	string result("");
	for(int n : list)
		number += n;
	while(number > 0){
		rem= max_element(list.begin(), list.end()) - list.begin();
		list[rem]--;
		result.append(1, rem+65);
		number--;
		if(!noMaj(list, number)){
			if(number <= 0)
				cout << "ERREUR 1" << endl;
			rem = max_element(list.begin(), list.end()) - list.begin();
			list[rem]--;
			result.append(1, rem+65);
			number--;
		}
		if(!noMaj(list, number)){
			cout << "ERREUR 2 n"  << number << endl;
			for(int n : list)
				cout << n << " ";
			cout << endl;
		}
		if(number != 0) result += " ";
	}
	return result;
}

//###########################################################################

string process2(string s){
	return s;
}

//###########################################################################

/*
void testFunc()
	RC_ASSERT( process(s) == process(s) );
};
*/

int main() {
	string s;
	int T, N;
	vector<int> list;
	//check("TEST", testFunc);
	cin >> T;
	for(int l = 0 ; l < T ; l++) {
		cin >> N;
		list.resize(N);
		for(int i = 0 ; i < N ; i++)
			cin >> list[i];
		//TRAITEMENT
		cout << "Case #" << l+1 << ": " << process(list) << endl;
		///////////
	}
	return 0;
}
