

#include <iostream>
#include <fstream>
using namespace std;


int myn(long long *p, int n) {
	long long m=p[0], pm=0;
	for(int i=1;i<=n;i++) { 
		if (p[i]<m) { m=p[i]; pm=i; }
	}
	return pm;
}

int main(int argc, char *argv[]) {
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");
	int T;
	fin>>T;
	for(int I=0;I<T;I++) {
		int n;
		fin>>n;
		long long *a=new long long[n];
		for(int i=0;i<n;i++) { fin>>a[i]; }
		
		long long *p=a; 
		int cm=0; n--;
		while(n>1) {
			int pm=myn(p,n);
			if (pm<n-pm) {
				for(int i=pm;i>0;i--) { 
					p[i]=p[i-1];
				}
				cm+=pm; p++;
			} else {
				for(int i=pm;i<n;i++) { 
					p[i]=p[i+1];
				}
				cm+=n-pm;
			}
			n--;
		}
		fout<<"Case #"<<I+1<<": "<<cm<<endl;
		delete []a;
	}
	fin.close();
	fout.close();
	return 0;
}

