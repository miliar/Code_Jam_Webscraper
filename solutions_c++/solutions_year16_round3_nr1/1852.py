#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
using namespace std;

struct Pair {
	char A;
	int in;
	bool operator<(const Pair &o) const {
		return in>o.in;
	}
};

int main(int argc, char *argv[]) {
//	string fname = "A-sample";
//	string fname = "A-small-attempt2";
	string fname = "A-large";
	ifstream fin(fname+".in");
	ofstream fout(fname+".out");
	int T;
	fin>>T;
	for(int I=0;I<T;I++) {
		int n, nin=0;
		fin>>n;
		vector<Pair> p(n);
		for(int i=0;i<n;i++) { 
			p[i].A = 'A'+i;
			fin>>p[i].in;
			nin+=p[i].in;
		}
		cout<<"Case #"<<I+1<<"..."<<endl;
		fout<<"Case #"<<I+1<<":";
		while (!p.empty()) {
			fout << " ";
			sort(p.begin(),p.end());
			fout << p[0].A;
			p[0].in--; nin--;
			sort(p.begin(),p.end());
			
			if (p[1].in<=(nin-1)/2) {
				fout << p[0].A;
				p[0].in--; nin--;
			}
			if (p.back().in==0) p.erase(p.end()-1);
			if (p.front().in==0) p.erase(p.begin());
		}
		fout<<endl;
	}
	fin.close();
	fout.close();
	return 0;
}

