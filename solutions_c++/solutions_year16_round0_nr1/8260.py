#include <iostream>
#include <vector>
#include <set>
#include <fstream>

using namespace std;

ifstream fin("in.txt");
ofstream fout("out.txt");

int dp[1000100];

#define cin fin
#define cout fout

int main(){
	vector<int> vv;
	for(int i = 1 ; i < 1000019 ; ++i){
		set<int> ss;
		for(int j = 1 ; j < 150 ; ++j){
			int nn = i * j;
			while(nn > 0){
				ss.insert(nn % 10);
				nn /= 10;
			}
			if(ss.size() == 10){
				dp[i] = i * j;
				break;
			}
		}
	}

	int t;
	cin >> t;
	for(int o = 0 ; o < t ; ++o){
		int n;
		cin >> n;
		cout << "Case #" << o + 1 << ": ";
		if(n == 0) cout << "INSOMNIA" << endl;
		else{
			if(dp[n] == 0) cout << "INSOMNIA" << endl;
			else cout << dp[n] << endl; 
		}
	}

	return 0;
}