#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<fstream>
#include<map>

using namespace std;


#define MAX(a,b) ((a>b)? a:b)
#define MIN(a,b) ((a<b)? a:b)
#define MAX3(a, b, c) MAX(a, MAX(b,c))

int main(){
	int T, A, B, K;
	ifstream cin("code_jam.in");
	ofstream cout("code_jam.out");
	cin >> T;
	for (int t = 1; t <= T; t++){
		cout << "Case #" << t << ": ";
		cin >> A >> B >> K;
		unsigned long long ret = 0;
		for (int i = 0; i < A; i++){
			for (int j = 0; j < B; j++){
				if ((i & j) < K)
					ret++;
			}
		}
		cout << ret << "\n";
	}
}