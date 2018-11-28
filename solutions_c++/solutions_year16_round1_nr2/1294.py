#include<fstream>
using namespace std;

int main() {
	int n;
	ifstream is;
	is.open("B-large.in");
	ofstream os;
	os.open("outB.txt");
	is>> n;
	for(int i=0; i<n; i++) {
		int a;
		int x[2501];
		for(int j = 0; j<2501;j++) x[j] = 0;
		is>>a;
		for(int j = 0; j<2*a*a-a;j++){
			int b;
			is>>b;
			x[b] ++;
		}
		os<<"Case #"<<i+1<<": ";
		int aux = 0, j=0;
		for(;aux<a-1;j++){
			if(x[j] % 2 !=0){
				os<<j<<" ";
				aux++;
			} 
		}
		for(;aux<a;j++){
			if(x[j] % 2 !=0){
				os<<j<<endl;
				aux++;
			} 
		}
	}
	return 0;
}



