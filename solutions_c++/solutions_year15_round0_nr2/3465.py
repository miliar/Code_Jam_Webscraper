#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

#define pB push_back

ifstream fin("in.txt");
ofstream fout("out.txt");

#define cin fin
#define cout fout


int main(){
	int t;
	cin >> t;
	for(int o = 0 ; o < t ; ++o){
		int d;
		cin >> d;
		vector<int> p;
		int mm = -1;
		for(int i = 0 ; i < d ; ++i){
			int x;
			cin >> x;
			if(x > mm) mm = x;
			p.pB(x);
		}

		int ans = 100000000;
		for(int i = 1 ; i <= mm ; ++i){
			vector<int> pp;
			for(int j = 0 ; j < d ; ++j) pp.pB(p[j]);
			int mmax = -1;
			int t = 0;
			for(int j = 0 ; j < pp.size() ; ++j){
				if(pp[j] > i){
					pp.pB(pp[j] - i);
					pp[j] = i;
					++t;
				}
				mmax = max(mmax , pp[j]);
			}
			ans = min(ans , mmax + t);
		}
		cout << "Case #" << o + 1 << ": " << ans << endl;
	}

	return 0;
}
