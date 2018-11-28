#include <iostream>
#include <fstream>

using namespace std;

ifstream fin("in.txt");
ofstream fout("out.txt");

#define cin fin
#define cout fout

int main(){
	int t;
	cin >> t;
	for(int o = 0 ; o < t ; ++o){
		int sm;
		cin >> sm;
		string s;
		cin >> s;
		int imax = sm + 1 , imin = -1;
		for(int i = 0 ; i < s.size() ; ++i){
			if(s[i] != '0'){
				imax = i;
			}
		}

		int ans = 0;
		int sum = 0;

		for(int i = 0 ; i < sm + 1 ; ++i){
			while(i > sum){
				++sum;
				++ans;
			}
			sum += (s[i] - '0');
		}

		cout << "Case #" << o + 1 << ": " << ans << endl;
	}
	return 0;
}
