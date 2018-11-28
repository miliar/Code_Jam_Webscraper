#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <stdint.h>


using namespace std;
vector <string> options;
vector <string> buf;
uint64_t k, c;

bool full(string str){
	char x = str[0];
	for (int i = 1; i < str.length(); i++)
		if (str[i] != x)
			return false;
	return true;
}

int bestPos(){

	int max = 0, imax = 0;
	for (int i = 0; i < options[0].length(); i++){
		int current = 0;
		for (int j = 0; j < options.size(); j++)
			if (options[j][i] == 'G')
				current++;
		if (current >= max){
			buf.clear();
			max = current;
			imax = i;
			int size;
			for (int j = 0; j < options.size(); j++)
				if (options[j][i] != 'G')
					buf.push_back(options[j]);
		}
	}

	options = buf;
	return imax;
}

void complex(string current, int complexity, string original){
	string str = "";
	if (full(current))
		return;
	if (complexity == c){
		//cout << original << endl;
		//cout << current.length() << endl;
		for (int i = 0; i < current.length(); i++)
			if ((i )  %original.length() == 0)
				cout << ' ' << current[i];
			else cout << current[i];
				cout << endl; 
		options.push_back(current);
	}
	else {
		for (int i = 0; i < current.length(); i++)
			if (current[i] == 'G')
				for (int j = 0; j < original.length(); j++)
					str += "G";
			else str += original;
			complex(str, complexity + 1, original);
	}
}

void possibleOriginals(string current){

	if (current.length() == k)
		complex(current, 1, current);
	else{
		possibleOriginals(current + "G");
		possibleOriginals(current + "L");
	}
}

uint64_t power(uint64_t x, uint64_t y){
	if (y == 0)
		return 1;
	uint64_t bufe = x;
	for (uint64_t i = 1; i < y; i++)
		x *= bufe;
	return x;
}


int main()
{
	int t;
	uint64_t s;
	//cout << power(10, 18);
	cin >> t;
	for (int i = 1; i <= t; i++){
		stringstream str;
		uint64_t x;
		cin >> k;
		cin >> c;
		cin >> s;
		x = k;
		if (c!=1)
			str <<' '<< 1 ;
	//	cout <<(unsigned long long) pow(k, c-1) << endl;
		for (uint64_t j = power(x, c - 1); j <= power(k, c); j += power(x, c - 1)){
				if (c != 1 && j + 1 <= power(k, c))

					str << ' ' << j + 1;
				else if (c == 1) str << ' ' << j ;
		//	cout << j << endl;
		}
	
		
		//possibleOriginals("G");
		//possibleOriginals("L");
		
		cout << "Case #"<<i<<":";
		if (k == 1 && s >= 1)
		cout << ' '<<1 << endl;
		else
		cout << str.str() << endl;
	}
	return 0;
}