#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;

char* lawnmower(){
	int N,M;
	cin >> N >> M;

	int** a = new int*[N];
	for(int i=0; i<N; i++){
		a[i] = new int[M];
	}

	for(int i=0; i<N; i++){
		for(int j=0; j<M; j++){
			cin >> a[i][j];
		}
	}

	int* maxi = new int[N];
	int* maxj = new int[M];
	
	for(int i=0; i<N; i++){
		maxi[i] = 0;
		for(int j=0; j<M; j++){
			if(a[i][j]>maxi[i]){
				maxi[i] = a[i][j];
			}
		}
	}
	for(int j=0; j<M; j++){
		maxj[j] = 0;
		for(int i=0; i<N; i++){
			if(a[i][j]>maxj[j]){
				maxj[j] = a[i][j];
			}
		}
	}

	for(int i=0; i<N; i++){
		for(int j=0; j<M; j++){
			if(a[i][j] < maxi[i] && a[i][j] < maxj[j]){
				return "NO";
			}
		}
	}

	return "YES";
}


int main(){
	ifstream input("B-large.in");
	cin.rdbuf(input.rdbuf());

	ofstream output("large.txt");
	cout.rdbuf(output.rdbuf());
	
	int T;
	cin >> T;

	for(int i=0; i<T; i++){
		cout << "Case #" << i+1 << ": " << lawnmower() << endl;
	}
	
	return 0;
}