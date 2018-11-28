#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<string>
#include<vector>
#include<iostream>
#include<fstream>
#include<map>
using namespace std;
#define MP make_pair
#define REP(i, N) for(int i = 0; i<(N); i++)
#define CLR(ary) memset((ary), 0, sizeof(ary))

const int INF = 987654321;
int numC;
int sMax;
char ary[2000];
int main(){
	freopen("A-large.in", "r", stdin);
	ofstream ofs("A-large.out");
	scanf("%d", &numC);
	for(int cases = 1; cases <= numC; cases++){
		scanf("%d %s", &sMax, ary);
		int S = ary[0] - '0', ans = 0;
		for(int i = 1; i<=sMax; i++){
			if(S < i){
				ans += i-S;
				S = i;
			}
			S += ary[i] - '0';
		}
		ofs<<"Case #"<<cases<<": "<<ans<<endl;
	}
	return 0;
}

