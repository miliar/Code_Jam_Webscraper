#include <cmath>
#include <vector>
#include <iostream>
#include <queue>
#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;
typedef long long Long;


int main() {
	freopen("in.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	cin >> T;
	for(int tc = 1; tc <= T; ++tc){
		int N;
		cin >> N;
		vector<int> V(10);
		int C = 0 , f = 0;
		cout << "Case #" << tc << ": ";
		for(int j = 1; j <= 200; ++j){
			int n = j * N;
			while(n){
				V[n%10]++;
				if(V[n%10] == 1)
					C++;
				n /= 10;
			}
			if(C == 10){
				f = 1;
				cout << j*N << endl;
				break;
			}
		}
		if(!f){
			cout << "INSOMNIA" << endl;
		}
	}
}


/*
 ######
 ######
 ######
 ######
*/
