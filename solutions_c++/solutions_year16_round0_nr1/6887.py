#include<iostream>
#include<fstream>

using namespace std;

int main() {
	ifstream fin;
	ofstream fout;
	
	fin.open("A-large.in");
	fout.open("output.out");
	
	int t, n;
	
	fin>>t;
	for (int testcase=0; testcase<t; testcase++) {
		fin>>n;
		if (n==0) {
			fout<<"Case #"<<(testcase+1)<<": INSOMNIA"<<"\n";
			continue;
		}
		int i = 1, r, a[10]={0,0,0,0,0,0,0,0,0,0};
		while (i<10000) {
			r = i*n;
			while (r>0) {
				a[r%10]++;
				r/=10;
			}
			int allFlag = 1;
			for (int j=0;j<10;j++) {
				if (a[j]==0) {
					allFlag = 0;
					break;
				}
			}
			if (allFlag) {
				break;
			}
			i++;
		}
		if (i>=10000) {
			cout<<"\nPossible Error (n="<<n<<")";
		}
		fout<<"Case #"<<(testcase+1)<<": "<<i*n<<"\n";
	}
	
	
	return 0;
}
