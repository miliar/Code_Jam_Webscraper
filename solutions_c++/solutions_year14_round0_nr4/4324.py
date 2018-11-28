#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
int N;
int real_war(int * naomi, int * ken){
	int cnaomi[N], cken[N];
	for (int i = 0; i < N; i++){
		cnaomi[i] = naomi[i];
		cken[i] = ken[i];
	}
	sort(cnaomi, cnaomi + N);
	sort(cken, cken + N);
	//cout << "realwar" << endl;
	//for (int i = 0; i < N; i++) cout << cnaomi[i] << " "; cout << endl;
	//for (int j = 0; j < N; j++) cout << cken[j] << " "; cout << endl;
	int npoints = 0;
	int last_j = N-1;
	for (int i = N-1; i >=0; i--){
		for (int j = last_j; j >= 0; j--){
			if (cken[i] > cnaomi[j]){
				//cout << "a " << cken[i] << endl;
				//cout << "b " << cnaomi[j] << endl;
				npoints++;
				last_j = j-1;
				break;
			}
		}
	}
	return N - npoints;
}

int deceit_war(int * naomi, int * ken){
	int cnaomi[N], cken[N];
	for (int i = 0; i < N; i++){
		cnaomi[i] = naomi[i];
		cken[i] = ken[i];
	}
	sort(cnaomi, cnaomi + N);
	sort(cken, cken + N);
	//cout << "deceit" << endl;
	//for (int i = 0; i < N; i++) cout << cnaomi[i] << " "; cout << endl;
	//for (int j = 0; j < N; j++) cout << cken[j] << " "; cout << endl;
	int npoints = 0;
	int last_j = N-1;
	for (int i = N-1; i >=0; i--){
		for (int j = last_j; j >= 0; j--){
			if (cnaomi[i] > cken[j]){
				npoints++;
				last_j = j-1;
				break;
			}
		}
	}
	return npoints;
}

int main(){
	int T; cin >> T;
	for (int test = 1; test <= T; test++){
		cin >> N;
		int naomi[N], ken[N];
		for (int i = 0; i < N; i++){
			double a; cin >> a;
			naomi[i] = 100000*a;
		}
		for (int i = 0 ; i < N; i++){
			double b; cin >> b;
			ken[i] = 100000 * b;
		}
	//		for (int i = 0; i < N; i++) cout << naomi[i] <<" "; cout << endl;
	//for (int j = 0; j < N; j++) cout << ken[j] << " "; cout << endl;
		int y, z;
		z = real_war(naomi, ken);
		y = deceit_war(naomi, ken);

		printf("Case #%d: %d %d\n", test, y, z);
	}

	return 0;
}