#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
char s[2100];
int no[10];

int count(char c){
	int co = 0;
	for (int i=0;i<strlen(s);i++){
		if  (s[i]==c) co ++;
	}
	return co;

}

int main() {
	freopen("small.in","r",stdin);
	freopen("small.out","w",stdout);

	int T,cases,N;

	scanf("%d ",&T);

	for (cases=1;cases<=T;cases++){
		scanf("%s ", s);
		
		int noZ = count('Z');
		no[0] = noZ;
		
		int noW = count('W');
		no[2] = noW;
		
		int noX = count('X');
		no[6] = noX;
		
		int noG = count('G');
		no[8] = noG;
		
		int noU = count('U');
		no[4] = noU;

		int noH = count('H');
		no[3] = noH - no[8];

		int noS = count('S');
		no[7] = noS - no[6];

		int noF = count('F');
		no[5] = noF - no[4];

		int noO = count('O');
		no[1] = noO - no[0] - no[2] - no[4];

		int noN = count('N');
		no[9] = (noN - no[1] - no[7]) / 2;

		printf( "Case #%d: ",cases);
		for (int i=0;i<10;i++){
			for (int j=0;j<no[i];j++){
				printf("%d",i);
			}
		}

		printf("\n");



	}
}
