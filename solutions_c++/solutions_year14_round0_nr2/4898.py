#include <iostream>
#include <iomanip>
using namespace std;

#define FOR(I,A,B) for(int I=(A);I<=(B);I++)
#define REP(I,N) for(int I=0;I<(N);I++)

int main(){
	
	int T;
	cin >> T;

	REP(i,T){
		double c,f,x;
		cin >> c >> f >> x;

		double e = 2;
		double time = 0;

		while(1){
			if(x/e<c/e + x/(e+f)) break;
			time += c/e;
			e += f;
		}

		cout << "Case #" << (i+1) << ": " << time + x/e << endl;
	}	

	return 0;
}
