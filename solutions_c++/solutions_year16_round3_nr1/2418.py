#include <iostream>
#include <vector>
#include <string>

using namespace std;


bool ok(vector<int> &vec){
	int idx, v=0, S=0;
	for(int i=0; i<vec.size(); ++i){
		S += vec[i];
		if(v < vec[i]){
			v = vec[i];
			idx = i;
		}
	}
	return v*2 <= S;
}

int main(){
	int T;
	cin >> T;
	for(int tc=1; tc <= T; ++tc){
		int N;
		cin >> N;
		vector<int> vec;
		int S = 0;
		for(int i=0; i<N; ++i){
			int tmp;
			cin >> tmp;
			vec.push_back(tmp);
			S += tmp;
		}
		cout << "Case #" << tc << ":";
		while(S > 0){
			if(S > 2){
				int idx, v=0;
				for(int i=0; i<vec.size(); ++i){
					if(v < vec[i]){
						v = vec[i];
						idx = i;
					}
				}
				cout << " " << (char)('A' + idx);
				--S;
				--vec[idx];

				if(!ok(vec)){
					v = 0;
					for(int i=0; i<vec.size(); ++i){
						if(v < vec[i]){
							v = vec[i];
							idx = i;
						}
					}
					cout << (char)('A' + idx);
					--S;
					--vec[idx];
				}
			}else{
				cout << " ";
				for(int i=0; i<vec.size(); ++i){
					if(vec[i] > 0){
						cout << (char)('A' + i);
					}
				}
				S -= 2;
				cout << endl;
			}
		}

	}
}