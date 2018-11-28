#include<fstream>
#include<cstring>
using namespace std;

int main() {
	int n;
	ifstream is;
	is.open("A-large.in");
	ofstream os;
	os.open("outA.txt");
	is>>n;
	for(int i=0; i<n; i++) {
		string s;
		string s2 = "";
		is>>s;
		for(int i=0; i<s.size(); i++){
			if (s[i]>=s2[0]){
				s2 = s[i] + s2;
			}
			else
				s2 = s2 + s[i];
		}
		os<<"Case #"<<i+1<<": "<<s2<<endl;
	}
	return 0;
}



