#include<fstream>
using namespace std;

void main(){
	ifstream ulaz;
	ulaz.open("ulaz.in");
	ofstream izlaz;
	izlaz.open("izlaz.out");
	long long br = 0;
	long long t, r;
	int T;
	ulaz>>T;
	for(int count = 1; count<=T; count++){
		ulaz>>r>>t;
		long long r1 = r, r2 = r+1;
		br = 0;
		while(t>0){
			if((t-=(r2-r1)*(r2+r1)) >=0){
				br++;
				r1 = ++r2;
				r2++;
			}
		}
		izlaz<<"Case #"<<count<<": "<<br<<endl;

	}


	ulaz.close();
	izlaz.close();

}