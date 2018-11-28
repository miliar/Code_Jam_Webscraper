#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

vector<int> b1;
vector<int> b2;


void read_rows(vector<int>& b){
	b = vector<int>(4,0);
	int r; cin >> r;
	int el;
	for(int i = 0; i < 4; ++i){
		for(int j = 0; j < 4; ++j){
			cin >> el;
			if(i+1 == r) b[j] = el;
		}
	}
	sort(b.begin(), b.end());
}



vector<int> intersec(){
	vector<int> inter(0,0);
	for(int i = 0; i< 4; ++i){
		for(int j = 0; j< 4;++j){
			if(b1[i] == b2[j]){
				inter.push_back(b1[i]);
				break;      	
			}
		}
	}
	return inter;
}


int main(){

	int T; cin >> T;
	for(int t = 1; t<= T; ++t){
		read_rows(b1);
		read_rows(b2);
		vector<int> inter = intersec();
		cout << "Case #" << t <<": ";
		if(inter.size() == 0){
			cout << "Volunteer cheated!" << endl;
		}
		else if(inter.size() > 1){
			cout << "Bad magician!" << endl;
		}
		else{
			cout << inter[0] << endl; 
		}
	}
  return 0;
}

