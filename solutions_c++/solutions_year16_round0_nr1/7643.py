#include <iostream>
#include <vector>

using namespace std;


void fill_vector(unsigned x, vector<bool> &V){
	while(x > 0){
		unsigned i = x%10;
		x /= 10;
		V[i] = true;
	}
}


bool check_full(const vector<bool> &V){
	for(unsigned i=0;i<10;i++)
		if(not V[i])
			return false;
	return true;
}


int main(){
	
	unsigned T, N;
	cin >> T;

	for(unsigned i=1;i<=T;i++){
		vector<bool> V(10, false);
		cin >> N;
		int j = 1;
		while(not check_full(V) and j > 0){
			if(j == 1024){
				j = -1;
			} else {
				fill_vector(N*j, V);
				j++;
			}
		}
		if(j < 0)
			cout << "Case #" << i << ": INSOMNIA" << endl;
		else
			cout << "Case #" << i << ": " << N*(j-1) << endl; 
	}

	cout << endl;

}