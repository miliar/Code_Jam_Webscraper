#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <cmath>
#include <sstream>
#include <map>
#include <set>
#include <cstdlib>
#include <algorithm>

using namespace std;

#define INF 1e9
#define MAX 51

typedef pair<int,int> ii;

int matrix[9][9];
map<char, int> ch;

void pre_process(){
	ch['1'] = 1;
	ch['i'] = 2;
	ch['j'] = 3;
	ch['k'] = 4;

	matrix[1][1] = 1;
	matrix[1][2] = 2;
	matrix[1][3] = 3;
	matrix[1][4] = 4;

	matrix[2][1] = 2;
	matrix[2][2] = 5;
	matrix[2][3] = 4;
	matrix[2][4] = 7;

	matrix[3][1] = 3;
	matrix[3][2] = 8;
	matrix[3][3] = 5;
	matrix[3][4] = 2;

	matrix[4][1] = 4;
	matrix[4][2] = 3;
	matrix[4][3] = 6;
	matrix[4][4] = 5;

	for(int i=1; i<=4; i++){
		for(int j=5; j<=8; j++){
			if(i <= 4){
				if(matrix[i][j-4] > 4){
					matrix[i][j] = matrix[i][j-4]-4;
				} else {
					matrix[i][j] = matrix[i][j-4]+4;
				}
			} else {
				matrix[i][j] = matrix[i-4][j-4];
			}
		}
	}

	for(int i=5; i<=8; i++){
		for(int j=1; j<=8; j++){
			if(j <= 4){
				if(matrix[i-4][j] > 4){
					matrix[i][j] = matrix[i-4][j]-4;
				} else {
					matrix[i][j] = matrix[i-4][j]+4;
				}
			} else {
				matrix[i][j] = matrix[i-4][j-4];
			}
		}
	}
}

int main(){
	freopen("C-small-attempt1.in", "r", stdin);
	//freopen("in", "r", stdin);
	freopen("output.out", "w", stdout);
	pre_process();
	int tcase = 0;

	int T;
	scanf("%d", &T);

	while(T--){
		int L, X;
		scanf("%d%d", &L, &X);
		long long N = L*X;
		
		string str;
		cin >> str;

		vector<long long> endFirst;
		set<long long> startLast;

		set<ii> unique;
		int current = ch[str[0]];
		unique.insert(ii(current, 0));

		if(current == 2){
			endFirst.push_back(0);
		}

		long long x = 1;
		while(x < N){
			current = matrix[current][ch[str[x%L]]];

			if(current == 2){
				endFirst.push_back(x);
			}

			if(unique.count(ii(current, x%L))){
				break;
			}

			unique.insert(ii(current, x%L));
			x++;
		}

		unique.clear();
		current = ch[str[L-1]];
		unique.insert(ii(current, L-1));

		if(current == 4){
			startLast.insert(N-1);
		}

		long long y = N-2;
		while(y >= 0){
			current = matrix[ch[str[y%L]]][current];

			if(current == 4){
				startLast.insert(y);
			}

			if(unique.count(ii(current, y%L))){
				break;
			}

			unique.insert(ii(current, y%L));
			y--;
		}

		bool test = false;

		for(int i=0; i<endFirst.size() and !test; i++){
			long long z = endFirst[i]+1;
			current = ch[str[z%L]];

			if(current == 3){
				long long temp = z;

				while(temp+1 < N and !startLast.count(temp+1)){
					temp += x;
				}

				if(startLast.count(temp+1)){
					test = true;
				}
			}

			z++;
			while(z < N and !test){
				current = matrix[current][ch[str[z%L]]];

				if(current == 3){
					long long temp = z;

					while(temp+1 < N and !startLast.count(temp+1)){
						temp += x;
					}

					if(startLast.count(temp+1)){
						test = true;
					}
				}

				z++;
			}
		}

		printf("Case #%d: %s\n", ++tcase, test ? "YES" : "NO");
	}
}