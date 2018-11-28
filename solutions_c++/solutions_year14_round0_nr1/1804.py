// Q1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    freopen("D://Practice//A-small-attempt1.in", "r", stdin);
    freopen("D://Practice//A-small-attempt0.out", "w", stdout);

	int numCase;
	cin >> numCase;

	for(int i=0; i<numCase; i++) {
		int flag[16], ans[4], counter=0, tmp, r1, r2;
		for(tmp=0; tmp<16; tmp++) flag[tmp]=0;
		cin >> r1;
		for(int ra=0; ra<4; ra++){
			for(int ca=0; ca<4; ca++){
				cin >> tmp;
				if(ra == r1-1) flag[tmp-1] =1;
			}
		}
		cin >> r2;
		for(int ra=0; ra<4; ra++){
			for(int ca=0; ca<4; ca++){
				cin >>tmp;
				if(ra == r2-1){
					if(flag[tmp-1]==1) ans[counter++] = tmp;
					else flag[tmp-1]=0;
				}
			}
		}
		if(counter==1) cout << "Case #" << (i+1) << ": " << ans[0] << endl;
		else{ 
			if(counter==0) cout << "Case #" << (i+1) << ": " << "Volunteer cheated!" << endl;
			else cout << "Case #" << (i+1) << ": " << "Bad magician!" << endl;
		}
	}
	return 0;
}