#include <fstream>
#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;


int main(void){
	unsigned T;
	ifstream fin("D-large.in");
	ofstream fout("out.txt");
	fin>>T;
	for (unsigned t=1; t<=T; t++){
		unsigned n;
		fin >> n;
		vector<double> a(n,0.0);
		vector<double> b(n,0.0);
		for (unsigned i=0; i<n; i++){
			fin >> a[i];
		}
		for (unsigned i=0; i<n; i++){
			fin >> b[i];
		}
		sort(a.begin(),a.end());
		sort(b.begin(),b.end());
		unsigned r1=0, r2=0;
		int la = 0, lb=0, ra =n-1,rb=n-1;
		while (la<=ra && lb<=rb){
			if (a[la]>b[lb]){
				r1++;
				la++;
				lb++;
			}else {
				la++;
				rb--;
			}
		}
		la = 0;lb=0; ra =n-1; rb=n-1;
		while (la<=ra && lb<=rb){
			if (a[ra]<b[rb]){
				r2++;
				ra--;
				rb--;
			}
			else {
				ra--;
				lb++;
			}
		}
		r2 = n - r2;
		fout << "Case #"<<t<<": "<<r1<<" "<<r2<<endl;
	}
	fin.close();
	fout.close();
	return 0;
}
