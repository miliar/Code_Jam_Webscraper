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


void solve(int K, int C, int S) {
	if(S < K) {
		cout << " IMPOSSIBLE\n";
		return;
	}
	string rslt= "";
	int i=0;
	for (i=1;i<=S;i++) {
		cout << " " << i;
	}
	cout <<"\n";
}

int main() {
	ifstream file("test.txt");
	string str, rslt;
	int i=0, n=0, C=0, K=0, S=0, T = readNextInt(&file);

    for(n=0; n<T;n++) {
    	getline(file, str);
		vector<string> p;
		split(str, ' ', p);
		i=0;
		K = atoi(p[0].c_str());
		C = atoi(p[1].c_str());
		S= atoi(p[2].c_str());
		cout<<"Case #" << n+1<<":";
		solve(K, C, S);


    }
    return 0;
}
