#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

int main() {
	ifstream inp("B-large.in");
	cin.rdbuf(inp.rdbuf());
	ofstream out("output.txt");
	cout.rdbuf(out.rdbuf());
	int T; cin>>T;
	for(int t=1; t<=T; t++) {
		double c, f, x; cin>>c>>f>>x;
		double res = x/2.0;
		double tmp = 0.0;
		for(int i=0;;i++) {
			tmp+=c/(2+i*f);
			if (tmp+x/(2+(i+1)*f)<res) res=tmp+x/(2+(i+1)*f);
			else break;
		}
		cout<<"Case #"<<t<<": ";
		cout<<fixed<<setprecision(7)<<res<<endl;
	}
	return 0;
}
