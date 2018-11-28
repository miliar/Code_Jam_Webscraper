#include <cstdlib>
#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <boost/foreach.hpp> //BOOST_FOREACH( single, sequence ) {}

//############################################################################

//#include <rapidcheck.h>

/*
rc::check("Test du test",
			[](const string s){ RC_ASSERT(process(s) == 1); });
*/
// rc::check("Test", [](){ const auto i = *rc::gen::inRange(0, 10); return i < 10 && i >= 0; });
//  https://github.com/emil-e/rapidcheck/blob/master/doc/generators_ref.md

//############################################################################

//#include <boost/multiprecision/cpp_int.hpp> //MULTIPRECISION
//#include <boost/algorithm/algorithm.hpp> //ALGORITHM
//#include <boost/sort/spreadsort/spreadsort.hpp> //TRI

//using namespace boost::multiprecision;
//using namespace boost::algorithm;
//using namespace boost::spreadsort;

using namespace std;

//###########################################################################


string process(string s){
	string ret = "";
	BOOST_FOREACH(char c, s){
		if(ret.empty() || c >= ret.front())
			ret.insert(ret.begin(), c);
		else ret.insert(ret.end(), c);
	}
	return ret;
}

int main() {
	string s;
	int i = 1, T;
	cin >> T;
	for(int l = 0 ; l < T ; l++) {
		cin >> s;
		//TRAITEMENT
		cout << "Case #" << i++ << ": " << process(s) << endl;
		///////////
	}
	return 0;
}
