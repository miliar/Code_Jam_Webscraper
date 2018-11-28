#include <bits/stdc++.h>

using namespace std;

const int N = 16;
const int J = 500;

string s;
vector<string> vs;

void rec(int curr) {
	if(curr == N-1) {
		s = s + '1';
		vs.push_back(s);
		s.pop_back();
		return;
	}
	s = s + '0';
	rec(curr+1);
	s.pop_back();

	s = s + '1';
	rec(curr+1);
	s.pop_back();
}

long long powTable[11][18];

void preprocess() {
	for(int b=2; b<11; b++) {
		powTable[b][0] = 1;
		for(int i=1; i<=N+1; i++) {
			powTable[b][i] = 1LL * b * powTable[b][i-1];
		}
	}
}

int main(int argc, char const *argv[]){
	freopen("C:\\Users\\Paramdeep Singh\\Desktop\\C-small-attempt1.in","r",stdin);
	freopen("C:\\Users\\Paramdeep Singh\\Desktop\\output.txt","w",stdout);
	int c, nn, jj; scanf("%d%d%d", &c, &nn, &jj); 
	s = "1";
	rec(1);
	preprocess();
	int cntr = 0;
	printf("Case #1:\n");
	for(int i=0; i<vs.size(); i++) {
		bool good = true;
		long long p[11];
		for(int b=2; b<11; b++) {
			long long val = 0;
			for(int j=0; j<vs[i].size(); j++) {
				if(vs[i][j] == '1') {
					val += powTable[b][j];
				}
			}
			long long proof = -1;
			for(long long j=2; 1LL*j*j <= val; j++) {
				if(val % j == 0) {
					proof = j;
					break;
				}
			}
			if(proof == -1) {
				good = false;
				break;
			}
			else p[b] = proof;
		}
		if(good) {
			reverse(vs[i].begin(), vs[i].end());
			cout << vs[i] << vs[i] << " ";
			for(int b=2; b<11; b++) 
				printf("%d ", p[b]);
			printf("\n");
			cntr++;
			if(cntr == J) break;
		}
	}
	return 0;
}