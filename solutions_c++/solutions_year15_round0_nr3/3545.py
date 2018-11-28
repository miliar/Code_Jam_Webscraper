#include <stdlib.h>
#include <iostream>
#include <string>


using namespace std;


char multiply(char a, char b){
	switch (a){
	case 1:
		switch (b){
		case 1:
			return 1;
			break;
		case 'i':
			return 'i';
			break;
		case 'j':
			return 'j';
			break;
		case 'k':
			return 'k';
			break;
		}
		break;
	case 'i':
		switch (b){
		case 1:
			return 'i';
			break;
		case 'i':
			return -1;
			break;
		case 'j':
			return 'k';
			break;
		case 'k':
			return -'j';
			break;
		}
		break;
	case 'j':
		switch (b){
		case 1:
			return 'j';
			break;
		case 'i':
			return -'k';
			break;
		case 'j':
			return -1;
			break;
		case 'k':
			return 'i';
			break;
		}
		break;
	case 'k':
		switch (b){
		case 1:
			return 'k';
			break;
		case 'i':
			return 'j';
			break;
		case 'j':
			return -'i';
			break;
		case 'k':
			return -1;
			break;
		}
		break;
	}
	return a;
}

string exfo(string str, long X){
	string nstr = str;
	for (int i = 0; i < X - 1; i++){
		nstr += str;
	}
	return nstr;
}

bool can_it(const char* str, long length, int stage){
	//const char* cstr = str.c_str();
	bool sol = false;
	char prev = 1;
	bool pos = true;

	for (int i = 1; i <= length; i++){
		prev = multiply(prev, str[i - 1]);
		if (prev < 0){
			prev *= -1;
			pos = !pos;
		}
		switch (stage){
		case 2:
			if (pos && prev == 'k'){
				if (i == length){
					return true;
				}
			}
			break;
		default:
			if (pos){
				if (stage == 0 && prev == 'i'){
					sol = can_it(&str[i], length - i, stage + 1);
				}
				if (stage == 1 && prev == 'j'){
					sol = can_it(&str[i], length - i, stage + 1);
				}
			}
		}
		if (sol){
			return true;
		}
	}
	return false;

}


bool reality_check(const char* str, long length){
	char prev = 1;
	bool pos = true;
	for (int i = 0; i < length; i++){
		prev = multiply(prev, str[i]);

		if (prev < 0){
			prev *= -1;
			pos = !pos;
		}
	}
	
	if (!pos && prev == 1){
		return true;
	}
	return false;
}

int main(){
	int test_cases;
	cin >> test_cases;
	for (int i = 1; i <= test_cases; i++){
		int X, L;
		cin >> L;
		cin >> X;
		string str;
		cin >> str;
		str = exfo(str, X);
		const char* c = str.c_str();
		bool isit = reality_check(c, L*X);
		if (isit){
			isit = can_it(c, X*L, 0);
		}
		
		if (isit){
			cout << "Case #" << i << ": YES" << endl;
		}
		else {
			cout << "Case #" << i << ": NO" << endl;
		}

	}


	return 0;
}