//============================================================================
// Name        : Contest.cpp
// Author      : Tarango Khan
// Team        : Byteheads
//============================================================================

#include <bits/stdc++.h>
using namespace std;

int main() {
	int nCase,sMax;
	string Line;
	cin>>nCase;
	for(int cs = 1;cs<=nCase;cs++){
		cin>>sMax>>Line;
		int cnt = Line[0]-'0';
		int frnd = 0;
		for(int i = 1;i<=sMax;i++){
			int cur = Line[i]-'0';
			//printf("Cur: %d , cnt: %d\n",cur,cnt);
			if(cur == 0) continue;
			if(cnt<i){
				frnd = frnd + (i-cnt);
				cnt = cnt + (i-cnt);
				//printf("For frnd i: %d, frnd: %d\n",i,frnd);
			}
			cnt = cnt + cur;
		}
		printf("Case #%d: %d\n",cs,frnd);
	}
}
