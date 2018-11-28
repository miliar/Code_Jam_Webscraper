#include <iostream>
#include <string>

using namespace std;

int main (){
	int T;
	cin >>T;
	for (int cas = 1; cas <= T; cas++){
		int Smax;
		string S;
		cin >>Smax;
		int resp = 0;
		char c;
		cin >>c;
		int cont = int(c -'0');
		for (int it = 1; it <= Smax; it++){
			cin >>c;
			int n = int(c-'0');
			resp = max(resp, it-cont);
			cont+=n;
		}
		cout <<"Case #"<<cas<<": "<<resp<<endl;

	}
}