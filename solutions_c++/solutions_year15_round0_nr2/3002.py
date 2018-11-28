#include<iostream>
#include<vector>
#include<cmath>
#include<utility>
using namespace std;
int cut_(vector<int> & V, int h){
	int step = 0;
	for(int i = 0 ; i < V.size() ; i ++){
		if(V[i] > h)
			step += V[i]/h - (V[i] % h == 0);
	}
	return step + h;
}
int main(){
	int T;
	int N;
	cin >> T;
	for(int t = 1 ;t <= T ; t++){
		cin >> N;
		vector<int> V(N);
		vector<int> V_(N);
		int MAX = -1;
		for(int i = 0 ; i < N ; i ++){
			cin >> V[i];
			if(V[i] > MAX)
				MAX = V[i];
		}
		int ans = MAX;
		for(int cut = MAX - 1 ; cut >= 1 ; cut--){
			int cur = cut_(V,cut);	
			if(cur < ans)
				ans = cur;
		}

		cout << "Case #"<<t<<": "<<ans << endl;
	}
	return 0;
}
