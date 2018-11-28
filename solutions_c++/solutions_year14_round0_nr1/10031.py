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
	int choice;
	int game[4][4];
	int game1[4], game2[4];
	char line[128];
	char *pLine;

	cin.getline(line, 128);
	choice = atoi(line);
	for (int idx = 0; idx < 4; idx++){
		cin.getline(line, 128);
		pLine = strtok(line, " ");	game[idx][0] = atoi(pLine);
		pLine = strtok(NULL, " ");	game[idx][1] = atoi(pLine);
		pLine = strtok(NULL, " ");	game[idx][2] = atoi(pLine);
		pLine = strtok(NULL, " ");	game[idx][3] = atoi(pLine);
	}

	for (int i = 0; i < 4; i++) game1[i] = game[choice - 1][i];
	cin.getline(line, 128);
	choice = atoi(line);
	for (int idx = 0; idx < 4; idx++){
		cin.getline(line, 128);
		pLine = strtok(line, " ");	game[idx][0] = atoi(pLine);
		pLine = strtok(NULL, " ");	game[idx][1] = atoi(pLine);
		pLine = strtok(NULL, " ");	game[idx][2] = atoi(pLine);
		pLine = strtok(NULL, " ");	game[idx][3] = atoi(pLine);
	}
	for (int i = 0; i < 4; i++) game2[i] = game[choice - 1][i];

	int res = 0;
	int count = 0;
	for (int i = 0; i < 4; i++){
		for (int j = 0; j < 4; j++){
			if (game1[i] == game2[j]){
				res = game1[i];
				count++;
			}
		}
	}

	if(count > 1)		sprintf(result, "%s", "Bad magician!");
	else if(count == 0)	sprintf(result, "%s", "Volunteer cheated!");
	else				sprintf(result, "%d", res);
	return result;
}

int main(void){
	int T, t = 0;
	char junk[128];
	cin.getline(junk, 128);
	T = atoi(junk);

	REP(t, T){
		//cin.getline(junk, 128);
		printf("Case #%d: %s\n", t + 1, calc());
	}
}
