#include <iostream>
#include <fstream>
#include <string>

using namespace std;

string trim(string );
int distBetween(string, string);

string trim(string s) {
	string r = "";
	char rec = '1';
	for(int i = 0; i < s.size(); i++) {
		if(s[i] != rec) {
			r += s[i];
			rec = s[i];
		}
	}
	return r;
}
int distBetween(string a, string b) {
	string x = trim(a);
	string y = trim(b);
	if( x.compare(y) != 0 ) {
		return -1;
	}
	else {
		int count = 0, i, j, bal = 0;
		for(i=0,j=0;;) {
			while(i < a.size() && a[i] == b[j]) {
				i++;
				count++;
			}
			i--;
			while(j < b.size() && b[j] == a[i]) {
				count--;
				j++;
				if(count == bal-1) {
					count = bal+1;
					while(j < b.size() && b[j] == a[i]) {
						count++;
						j++;
					}
				}
			}
			i++;
			if(i==a.size() && j==b.size()) {
				break;
			}
			bal = count;
		}
		return count;
	}
}
int main(int argc, char* argv[]) {
	if( argc != 3 ) {
		cout << "Usage: " << argv[0] << " <input file name> <output file name>" << endl;
		return 1;
	}
	ifstream in(argv[1]);
	if( !in.is_open() ) {
		cout << "Unable to open the file: " << argv[1] << endl;
		return 1;
	}
	ofstream out(argv[2]);
	
	int T;
	in >> T;
	for(int t = 0; t < T; t++) {
		int N;
		in >> N;
		string *a = new string[N];
		for(int n = 0; n < N; n++) {
			in >> a[n];
		}
		int dist[N][N];
		bool flag = true;
		long min = 999999;
		for(int i = 0; i < N; i++) {
			int sum = 0;
			for(int j = 0; j < N; j++) {
				if(i==j) {
					continue;
				}
				if(a[i].size() <= a[j].size()) {
					dist[i][j] = distBetween(a[i], a[j]);
				}
				else {
					dist[i][j] = distBetween(a[j], a[i]);
				}
				if(dist[i][j] == -1) {
					flag = false;
					break;
				}
				sum += dist[i][j];
			}
			if(min > sum) {
				min = sum;
			}
		}
		if(!flag) {
			out << "Case #" << (t+1) << ": Fegla Won" << endl;
		}
		else {
			out << "Case #" << (t+1) << ": " << min << endl;
		}
	}
	return 0;
}