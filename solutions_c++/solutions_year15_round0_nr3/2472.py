#include<fstream>
#include<iostream>
#include<string>

using namespace std;

char qmult(char a, char b) {
	if (a == '+') return b;
	if (b == '+') return a;
	if (a == '-') {
		if (b == '-') return '+';
		if (b == 'i') return 'x';
		if (b == 'j') return 'y';
		if (b == 'k') return 'z';
		if (b == 'x') return 'i';
		if (b == 'y') return 'j';
		if (b == 'z') return 'k';
	}
	if (a == 'i') {
		if (b == '-') return 'x';
		if (b == 'i') return '-';
		if (b == 'j') return 'k';
		if (b == 'k') return 'y';
		if (b == 'x') return '+';
		if (b == 'y') return 'z';
		if (b == 'z') return 'j';
	}
	if (a == 'j') {
		if (b == '-') return 'y';
		if (b == 'i') return 'z';
		if (b == 'j') return '-';
		if (b == 'k') return 'i';
		if (b == 'x') return 'k';
		if (b == 'y') return '+';
		if (b == 'z') return 'x';
	}
	if (a == 'k') {
		if (b == '-') return 'z';
		if (b == 'i') return 'j';
		if (b == 'j') return 'x';
		if (b == 'k') return '-';
		if (b == 'x') return 'y';
		if (b == 'y') return 'i';
		if (b == 'z') return '+';
	}
	if (a == 'x') return qmult('-', qmult('i', b));
	if (a == 'y') return qmult('-', qmult('j', b));
	if (a == 'z') return qmult('-', qmult('k', b));
	
	
	
}

bool is_correct(long long l, long long x, string elem_str) {
	long long my_str_len = l * x;
	long long y = x % 4;
	if (y == 0) return false;		
	
	char elem_res = '+';
	for (int i = 0; i < l; ++ i) {
		elem_res = qmult(elem_res, elem_str[i]);		
	}
	//cout << "elem_res= " << elem_res << " ";
	
	char res = '+';	
	for (int i = 0; i < y; ++ i) {
		res = qmult(res, elem_res);			
	}
	//cout << " res= " << res << " ";		
	
	if (res != '-') {
		//cout << "\nTotalfail\n";
		return false;
	}
	
	//cout << "reshead: ";
	char reshead = '+';	
	long long p = -1;
	while ((p < my_str_len - 1) && (reshead != 'i')) {
		++ p;
		reshead = qmult(reshead, elem_str[p % l]);		
	}
		
	//cout << "restail: ";
	char restail = '+';
	long long q = my_str_len;	
	while ((q > 0) && (restail != 'k')) {
		--q;
		restail = qmult(elem_str[q % l], restail);		
	}
	
	if (p >= my_str_len) return false;
	if (q < 0) return false;
	
	//cout << p << " " << q << endl;
	if (p + my_str_len - q >= my_str_len) {
		//cout << "len\n";
		return false;
	}
	return true;
	
}


int main()
{
	long long t;
	ifstream inputfile("inc.txt");
	ofstream outputfile("outc.txt");
	inputfile >> t;
	
	long long l,  x;
	string elem_str;
	for (int i = 0; i < t; ++ i)
	{
		inputfile >> l >> x >> elem_str;
		//cout << "Case #" << i + 1 << ":\n";
		outputfile << "Case #" << i + 1 << ": ";
		if (is_correct( l, x, elem_str))
			outputfile << "YES" << endl;
		else
			outputfile << "NO" << endl;
	}
}
