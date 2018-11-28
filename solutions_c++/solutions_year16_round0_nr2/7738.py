#include <iostream>
#include <vector>

using namespace std;


int moves(vector<bool> &V, int i){
	if(i < 0){
		return 0;
	} else if(V[i]) {
		return moves(V, i-1);
	} else {
		for(int j=0;j<=i;j++)
			V[j] = !V[j];
		return 1 + moves(V, i-1);
	}
}


int moves(vector<bool> &V){
	return moves(V, V.size()-1);
}


int main(){

	int T;
	cin >> T;

	for(int i=1;i<=T;i++){
		string pnk;
		cin >> pnk;
		vector<bool> V(pnk.size());
		for(int j=0;j<pnk.size();j++){
			if(pnk[j] == '+')
				V[j] = true;
			else
				V[j] = false;
		}
		cout << "Case #" << i << ": " << moves(V) << endl;
	}

}