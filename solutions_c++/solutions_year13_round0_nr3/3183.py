#include<iostream>
#include<fstream>
#include<string>
#include <sstream>

using namespace std;

long long pripad(long long o, long long d);
bool is_palindrome(long long cislo);

int main() {
	ifstream myReadFile;
	myReadFile.open("input.in");
	ofstream myWriteFile;
	myWriteFile.open("output.out");
	string output;
	if (myReadFile.is_open()) {
		myReadFile >> output;
		int pocet_pripadu = atoi(output.c_str());
		//pocet_pripadu = 4;
		cout << pocet_pripadu<<"\n";
		for (int i = 1;i<=pocet_pripadu;i++) {
			myReadFile >> output;
			long long o = atoi(output.c_str());
			myReadFile >> output;
			long long d = atoi(output.c_str());
			long long reseni = pripad(o, d);
			cout<<"Case #"<<i<<": "<<reseni<<"\n";
			myWriteFile<<"Case #"<<i<<": "<<reseni<<"\n";
		}
	}
	myReadFile.close();
	myWriteFile.close();
	cin>>output;
	return 0;
}

long long pripad(long long o, long long d) {
	long long navrat = 0;
	o = long long(ceil(sqrt(float(o))));
	d = long long(sqrt(float(d)));
	for (long long i = o; i<=d;++i) {
		if (is_palindrome(i)) {
			if (is_palindrome(i*i)) {
				navrat++;
			}
		}
	}
	return navrat;
}

bool is_palindrome(long long cislo) {
	std::ostringstream s;
	s << cislo;
	string retezec;
	retezec = s.str();
	int index_1 = 0;
	int index_2 = retezec.size()-1;
	bool pokracuj = true;
	while (pokracuj) {
		if (retezec.at(index_1)!=retezec.at(index_2)) {
			pokracuj = false;
			return false;
		}
		index_1++;
		index_2 --;
		if (index_1>index_2) {
			pokracuj = false;
		}
	}
	return true;
}