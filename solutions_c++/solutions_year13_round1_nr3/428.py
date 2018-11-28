#include <iostream>
#include <cmath>
#include <vector>
#include <list>
#include <ctime>
#include <cstdlib>

using namespace std;

int T, R, N, M, K;

list<vector<int> > tuples;
list<vector<int> > valid;

int power(int a, int b){
	int ans = 1;
	while(b--){
		ans *= a;
	}
	return ans;
}

void generate(){
	int limit = power(M-1, N);
	
	for(int i = 0; i < limit; i++){
		int val = i;
		vector<int> v;
		for(int j = 0; j < N; j++){
			v.push_back(val % (M-1) + 2);
			val /= (M-1);
		}
		
		tuples.push_back(v);
	}
}

bool can_generate(vector<int>& v, int pos, int val, int x){
	if(val == x)
		return true;
	
	if(pos == v.size())
		return false;
		
	if(can_generate(v, pos+1, val, x) || can_generate(v, pos+1, val * v[pos], x))
		return true;
	
	return false;
}

int main(){
	srand(time(NULL));
	cin >> T;
	cin >> R >> N >> M >> K;
		
	generate();
	
	cout << "Case #1:\n";
	
	for(int i = 0; i < R; i++){
		valid = tuples;
		for(int j = 0; j < K; j++){
			int x;
			cin >> x; 
			list<vector<int> >::iterator it = valid.begin();
			
			while(it != valid.end()){
				if(can_generate(*it, 0, 1, x)){
					it++;
				}
				else{
					it = valid.erase(it);
				}
			}
		}
		
		if(!valid.empty()){
			list<vector<int> >::iterator it = valid.begin();
			for(int i = 0; i < N; i++){
				cout << (*it)[i];
			}	
			cout << "\n";
		}			
		else{
			for(int i = 0; i < N; i++){
				cout << (rand() % (M-1) + 2);
			}
			cout << "\n"
		}
	}
}

