#include <iostream>
#include <fstream>
#include <string>
#include<cstdlib>
#include<vector>
#include <sstream>
using namespace std;


void split(const string &s, char delim, vector<string> &elems) {
    stringstream ss(s);
    string item;
    while (getline(ss, item, delim)) {
        elems.push_back(item);
    }
}

int readNextInt(ifstream *file) {
	string str;
	getline(*file, str);
	return(atoi(str.c_str()));
}


long solve (int N) {
	if(N==0) {
		return -1;
	}
	bool d[10] = {false};
	long currval = 0;
	int tmp=0; // = some int
	int digit=0;
	while (!(d[0]&&d[1]&&d[2]&&d[3]&&d[4]&&d[5]&&d[6]&&d[7]&&d[8]&&d[9])) {
		currval += N;
		tmp=currval;
		while (tmp > 0) {
		    digit = tmp % 10;
		    tmp = tmp / 10;
		    d[digit]= true;
		}
	}
	return currval;
}

int main() {
	ifstream file("test.txt");
	string str;
	int n=0, N = 0, T = readNextInt(&file);
	long  rslt=0;
    for(n=0; n<T;n++) {
    	N = readNextInt(&file);
		rslt = solve(N);
		if(rslt>-1)
			cout<<"Case #" << n+1<<": "<<rslt<<"\n";
		else
			cout<<"Case #" << n+1<<": INSOMNIA\n";
    }
    return 0;
}
