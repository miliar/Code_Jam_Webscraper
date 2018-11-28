#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main(){

	freopen("op.txt", "w", stdout);
	freopen("in.in", "r", stdin);
	
	float tmp;
	int T, N,
		y, z;

	cin >> T;

	vector<float> Naomi, Ken, v1, v2;
	
	for(int t=1 ; t<=T ; t++){
		Ken.clear();
		Naomi.clear();

		cin >> N;

		for(int i=0 ; i<N ; i++){ cin >> tmp; Naomi.push_back(tmp);}
		for(int i=0 ; i<N ; i++){ cin >> tmp; Ken.push_back(tmp);}

		sort(Naomi.begin(), Naomi.end());
		sort(Ken.begin(), Ken.end());
		v1 = Naomi;	v2 = Ken;


		int j = 0;
		for(int i=0 ; i<N ; i++){
			for(; j<Ken.size(); j++)
				if(Ken[j] > Naomi[i]){
					Ken.erase(Ken.begin()+j);
					break;
				}
		}
		z = Ken.size();

		Naomi = v1; Ken = v2;

		int n = N, lastidx;

		j=N-1;
		for(int i=N-1 ; i>=0 ; i--){
			lastidx  = -1;
			for(j=Naomi.size()-1 ; j>=0 ; j--){
				if(Ken[i] < Naomi[j]) lastidx = j;
				else break;
			}
			if(lastidx == -1)
				n--;
			else
				Naomi.erase(Naomi.begin()+lastidx);
		}

		y = n;


		printf("Case #%d: %d %d\n", t, y, z);
	}

	return 0;
}