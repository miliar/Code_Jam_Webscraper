#include <fstream>
#include <string>
using namespace std;
ifstream in("in.txt");
ofstream out("out.txt");
	

string solve() {
	int n, n1, a[4], b[4], tmp;
	in >> n;
	for (int i = 0; i<4;i++)
		for (int j=0;j<4;j++) {
			if (i == n-1) in >> a[j];
			else in >> tmp;
		}
	in >> n1;
	for (int i = 0; i<4;i++)
		for (int j=0;j<4;j++) {
			if (i == n1-1) in >> b[j];
			else in >> tmp;
		}
	int ans = 0;
	int answer;
	for (int i=0;i<4;i++) {
		for (int j=0;j<4;j++) {
			if (a[i] == b[j]) {
				ans++;
				answer = a[i];
			}
		}
	}
	if (ans == 0) return "Volunteer cheated!";
	if (ans > 1) return "Bad magician!";
	char * buf = new char[2];
	return itoa(answer,buf,10);
}

int main() {
	int t;
	in >> t;
	for (int i = 0; i < t; i++) {
		out << "Case #" << i + 1 << ": " << solve() << endl; 
	}
	return 0;
}