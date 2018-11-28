#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

struct disco {
	int f1,f2,x;
	disco(){}
	disco(int _x, int _s1=-1):f1(_s1),f2(-1),x(_x){}
	bool add(int s) {
		if (f2!=-1) return false; 
		if (f1==-1) { f1=s; return true; }
		if (f1+s>x) return false;
		f2=s; return true;
	}
	bool is_full() {return f1!=-1&&f2!=-1;}
};

int main(int argc, char *argv[]) {
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	int T;
	fin>>T;
	for(int I=0;I<T;I++) {
		int n,x;
		fin>>n>>x;
		int *s=new int[n];
		for(int i=0;i<n;i++) { 
			fin>>s[i];
		}
		
		vector<disco> d;
		sort(s,s+n);
		d.reserve(n);
		int h=n/2-1;
		for(int i=n-1;i>h;i--) { 
			d.push_back(disco(x,s[i]));
		}
		for(int i=h;i>=0;i--) { 
			bool added=false;
			for(int j=0;j<d.size();j++) { 
				if (d[j].add(s[i])) { added=true; break; }
			}
			if (!added) d.push_back(disco(x,s[i]));
		}
		fout<<"Case #"<<I+1<<": "<<d.size()<<endl;
		delete []s;
	}
	fin.close();
	fout.close();
	return 0;
}

