#include<fstream>

using namespace std;

int main() {
	string s;
	char last;
	int n;
	int cnt;
	ifstream is;
	is.open("B-large.in");
	ofstream os;
	os.open("outB.txt");
	is>>n;
	for(int i=0; i<n; i++) {
		is>>s;
		cnt = 0;
		last = '0';
		for(int j=0; j<s.size(); j++){
			if(s[j] == '-' && last == '0') cnt++;
			else if (s[j] == '-' && last == '+') cnt+=2;
			last = s[j];
		}
		os<<"Case #"<<i+1<<": "<<cnt<<endl;
	}
	return 0;
}



