#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <cfloat>
#include <iomanip>
#include <climits>
#include <algorithm>
#include <map>

using namespace std;


int main(int argc, char *argv[]){
	int T;
	
	ifstream ifs(argv[1]);
	ofstream ofs("output.txt");

	ifs >> T;
	
	for(int t=0; t<T; t++){
		int N;
		ifs >> N ;
		vector< string > S(N);
		for(int i=0; i<N; i++){
			ifs >> S[i];
		}
		vector<vector<int> > V(N, vector<int>(1,0) );
		vector<string> mys(N);
		
		
		for(int i=0; i<N; i++){
			int l=S[i].size();
			char tmp=S[i][0];
			mys[i] += tmp;
			
			vector<int>::iterator itr = V[i].end() -1 ;
			
			for(int j=0; j<l; j++){
				if(tmp==S[i][j]){
					*itr += 1;
				}else{
					tmp=S[i][j];
					V[i].push_back(1);
					itr = V[i].end() -1;
					mys[i]+=tmp;
				}
			}
		}

		int ans=0;
		for(int i=0; i<N-1; i++){
			if( mys[i].compare(mys[i+1]) ) ans=-1;
		}

		if(ans>=0){
			int l=mys[0].size();
			vector<vector<int> > myV(l, vector<int>(N,0) );
			for(int i=0; i<l; i++){
				for(int j=0; j<N; j++){
					myV[i][j] = V[j][i];
				}
			}
			for(int j=0; j<N; j++){
				sort(myV[j].begin(), myV[j].end());
			}
			for(int i=0; i<l; i++){
				int mean=myV[i][N/2];
				for(int j=0; j<N; j++){
					ans += abs(myV[i][j] - mean);
				}
			}
			cout << "Case #" << t+1 << ": " << ans << endl;
			ofs << "Case #" << t+1 << ": "  << ans << endl;
		}else{
			cout << "Case #" << t+1 << ": " << "Fegla Won" << endl;
			ofs << "Case #" << t+1 << ": "  << "Fegla Won" << endl;
		}
		
	}
	return 0;
}