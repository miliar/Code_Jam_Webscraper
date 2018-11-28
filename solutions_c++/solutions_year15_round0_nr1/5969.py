#include <iostream>
#include <string>
#include <cstdio>
using namespace std;


int main(){

	freopen("out.txt", "w", stdout);
	freopen("in.in", "r", stdin);

	int T;
	cin >> T;

	int count = 0;
	int Smax;
	string S;
	while (T--){
		count++;
		cin >> Smax;
		cin >> S;

		int pcount = S[0] - '0';
		int addedP = 0;
		for (int ind = 1; ind < S.size(); ind++){
			if (ind > pcount){
				addedP++;
				pcount++;
			}
			pcount += S[ind] - '0';
		}

		cout <<"Case #"<<count<<": "<< addedP << endl;

	}
	return 0;
}