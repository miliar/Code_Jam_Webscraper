#include <iostream>
#include <fstream>

using namespace std;

void mkfals(int* digs);
bool checkdigs(int* digs);
string checkall(int* digs, string num);
void check(int* digs, string num);

int main() {
	ifstream in;
	ofstream out;
	string fname, num;
	cout << "Input file: ";
	cin >> fname;
	
	in.open(fname.c_str());
	out.open("out2.txt");
	
	int T, N;
	int* digs = new int [10];
	
	mkfals(digs);
	
	in >> T;
	
	
	for (int i = 0; i<T; i++) {
		in >> num;
		string end = checkall(digs, num);
		out << "Case #" << i + 1 << ": " << end << endl;
		mkfals(digs);
	}
	
	
	return 0;
}


void mkfals(int* digs){
	for (int i = 0; i < 10; i++) {
		digs[i] = false;
	}
}

bool checkdigs(int* digs){
	for (int j = 0; j < 10; j++) {
		if (!digs[j])
			return false;
	}
	return true;
}

string checkall(int* digs, string num){
	if(stoi(num) == 0)
		return "INSOMNIA";
	
	check(digs, num);
	int count = 2;
	string n;
	while (!checkdigs(digs)) {
		n = to_string(count*stoi(num));
		check(digs, n);
		count++;
	}
	return n;
}

void check(int* digs, string num){
	if (num.length() < 1)
		return;
	
	int cur = stoi(num.substr(0,1));
	
	string rest = num.substr(1);
	
	for (int i = 0; i < 10; i++) {
		if (!digs[i])	
			digs[i] = i == cur;
	}
	
	check(digs, rest);
}