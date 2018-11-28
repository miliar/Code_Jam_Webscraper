#include <cstdio>
#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
#include <fstream>


using namespace std;

int T, A, N;

vector<int> MS;
int GV[1000001];




int main(){


	cin >> T;	
	for(int cas=1;cas<=T;cas++){
		cin >> A >> N;
		MS.clear();

		MS.push_back(0);
		int x;
		for(int i=1;i<=N;i++){
			cin >> x;
			MS.push_back(x);
		}

		sort(MS.begin(), MS.end());

		GV[0]=0;

		int sol = N;

		if(A==1) sol = N;
		else{

			for(int i=1;i<=N;i++){
				int add = 0;

				while(A<=MS[i]){
					A+=A-1;
					add+=1;
				}

				A+=MS[i];

				GV[i]=GV[i-1]+add;	

			}

			for(int i=1;i<=N;i++){
				int val = N-i+GV[i];
				if(val < sol) sol = val;
			}

		}
			
		cout << "Case #" << cas << ": " << sol << endl; 
	}
	return 0;
}
