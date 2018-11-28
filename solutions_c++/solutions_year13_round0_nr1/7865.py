#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>

using namespace std;

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)

typedef long long ll;
char result[128];
	
//char test[] = "1\nXXXT\n....\nOO..\n....";

char *calc(){
	char game[4][5];
	int count;
	bool finished = true;
	int idx1 = 0, idx2 = 0, tmp = 0;

	for(idx1 = 0; idx1 < 4; idx1++){
		cin.getline(game[idx1], 5);
	}
	
	for(idx1 = 0; idx1 < 4; idx1++){
		for(idx2 = 0; idx2 < 4; idx2++){
			if(game[idx1][idx2] == '.')	finished = false;
		}
	}

	//horizontal
	for(idx1 = 0; idx1< 4; idx1++){
		if(game[idx1][0] == '.'){	finished = false;	continue;	}
		if(game[idx1][0] == 'T')	tmp = 1;
		else						tmp = 0;
		for(idx2= 1+tmp; idx2< 4;idx2++){
			if(game[idx1][idx2] == '.'){	finished = false;	break;	}
			if(game[idx1][tmp] != game[idx1][idx2] && game[idx1][idx2] != 'T'){
				break;
			}
		}

		if(idx2== 4 && game[idx1][idx2-1] != '.'){
			sprintf(result, "%c won", game[idx1][tmp]);
			return result;
		}
	}

	//vertical
	for(idx1= 0; idx1< 4; idx1++){
		if(game[0][idx1] == '.'){	finished = false;	continue;	}
		if(game[0][idx1] == 'T')	tmp = 1;
		else						tmp = 0;

		for(idx2= 1+tmp; idx2< 4;idx2++){
			if(game[idx2][idx1] == '.'){	finished = false;	break;	}
			if(game[tmp][idx1] != game[idx2][idx1] && game[idx2][idx1] != 'T'){
				break;
			}
		}

		if(idx2== 4 && game[idx2-1][idx1] != '.'){
			sprintf(result, "%c won", game[tmp][idx1]);
			return result;
		}
	}

	//diag1
	if(game[0][0] == 'T')	tmp = 1;
	else					tmp = 0;

	bool outOfLoop = false;
	if(game[0][0] != '.'){
		for(idx1= 0+tmp; idx1< 4; ){
			for(idx2= 0+tmp; idx2< 4; ){
				if(game[idx1][idx2] == '.'){	finished = false;	outOfLoop = true; 	idx1++; idx2++; break;	}
				if(game[tmp][tmp] != game[idx1][idx2] && game[idx1][idx2] != 'T'){
					outOfLoop = true;
					break;
				}
				idx1= idx1+ 1;
				idx2= idx2+ 1;
			}
			if(outOfLoop)	break;

			if(idx2== 4 && idx1== 4){
				sprintf(result, "%c won", game[tmp][tmp]);
				return result;
			}
		}
	}

	//diag2
	if(game[0][3] == 'T')	tmp = 1;
	else					tmp = 0;
	outOfLoop = false;
	if(game[0][3] != '.'){
		for(idx1 = 0+tmp; idx1 < 4;){
			for(idx2= 3-tmp; idx2> -1;){
				if(game[idx1][idx2] == '.'){	finished = false;	outOfLoop = true; idx1++;idx2--;break;	}
				if(game[tmp][3-tmp] != game[idx1][idx2] && game[idx1][idx2] != 'T'){
					outOfLoop = true;
					break;
				}
				idx1= idx1 + 1;
				idx2= idx2 - 1;
			}

			if(outOfLoop)	break;
			if(idx2== -1 && idx1== 4){
				sprintf(result, "%c won", game[tmp][3-tmp]);
				return result;
			}
		}
	}

	if(finished)	sprintf(result, "%s", "Draw");
	else			sprintf(result, "%s", "Game has not completed");
	return result;
}

int main(void){
	int T, t = 1;
	char junk[128];
	scanf("%d", &T);
	
	REP(t, T){
		cin.getline(junk, 128);
		printf("Case #%d: %s\n", t+1, calc());
	}
}
