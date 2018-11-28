#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <sstream>
#include <functional>
#include <map>
#include <string>
#include <string.h>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <list>
using namespace std;
const double PI = 3.14159265358979323846;

int main(){
	int T;
	cin>>T;
	for(int Case = 1; Case <= T; Case++){
		string s[4];
		int winFlag = 0;
		for(int i = 0; i < 4; i++)cin>>s[i];
		
		for(int i = 0; i < 4; i++){
			int X = 0,O = 0;
			for(int j = 0; j < 4; j++){
				if(s[i][j]=='X' || s[i][j] == 'T')X++;
				if(s[i][j]=='O' || s[i][j] == 'T')O++;
			}
			if(X==4)winFlag++;
			if(O==4)winFlag--;
		}
		
		for(int j = 0; j < 4; j++){
			int X = 0,O = 0;
			for(int i = 0; i < 4; i++){
				if(s[i][j]=='X' || s[i][j] == 'T')X++;
				if(s[i][j]=='O' || s[i][j] == 'T')O++;
			}
			if(X==4)winFlag++;
			if(O==4)winFlag--;
		}
		
		int X = 0, O = 0;
		for(int i = 0; i < 4; i++){
			if(s[i][i]=='X' || s[i][i] == 'T')X++;
			if(s[i][i]=='O' || s[i][i] == 'T')O++;
		}
		if(X==4)winFlag++;
		if(O==4)winFlag--;
		
		X = O = 0;
		
		for(int i = 0; i < 4; i++){
			if(s[i][3-i]=='X' || s[i][3-i] == 'T')X++;
			if(s[i][3-i]=='O' || s[i][3-i] == 'T')O++;
		}
		if(X==4)winFlag++;
		if(O==4)winFlag--;
		
		printf("Case #%d: ",Case);
		if(winFlag>0){
			printf("X won\n");
		}
		if(winFlag<0){
			printf("O won\n");
		}
		if(winFlag==0){
			bool drawFlag = true;
			for(int i = 0; i < 4; i++){
				for(int j = 0; j < 4; j++){
					if(s[i][j] == '.')drawFlag = false;
				}
			}
			
			if(drawFlag){
				printf("Draw\n");
			}else {
				printf("Game has not completed\n");
				
			}
		}
	}
	return 0;
}
