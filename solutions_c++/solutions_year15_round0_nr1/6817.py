#include <iostream>
#include <fstream>

using namespace std;


int main(int argc, char *argv[]){
	ifstream fin(argv[1], ios::in);
	ofstream fout(argv[2], ios::out);

	int T;

	fin>>T;
	int Tcase = 1;
	// cout << fixed; 
	// cout.precision(7);
	// fout << fixed; 
	// fout.precision(7);
	while(T--) {
		int sm;
		string aud;
		long long int clapps = 0;
		long long int res = 0;

		fin>>sm;
		fin>> aud;
		for (int i = 0; i < sm; ++i)
		{
			clapps += (int)aud[i]-'0';
			if (i+1 > clapps) {
				int diff= (i+1 -clapps);
				res += diff;
				clapps += diff;
			}
		}
		// cout <<sm<<' '<<aud<<endl;
		cout<<"Case #"<<Tcase<<": "<<res<<endl;
		fout<<"Case #"<<Tcase++<<": "<<res<<endl;
	}

	fin.close();
	fout.close();
	
	return 0;	
}
