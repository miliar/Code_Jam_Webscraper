#include <fstream>

using namespace std;

int main(){
	ifstream in("A-large.in");
	ofstream out("A-large.out");
	int n;
	in >> n;
	for(int i=0;i<n;++i){
		int k;
		in >> k;
		int cnt=0,x=0;
		string s;
		getline(in,s);
		for(int j = 1;j<(int)s.size();++j){
			cnt += s[j] - 48;
			while(cnt < j){
				cnt += 1;
				x += 1;
			}
		}
		out << "Case #" << i+1 << ": " << x << endl;
	}
}
