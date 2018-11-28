#include <iostream>
#include <stdio.h>
#include <vector>
#include <map>
#include <string>
#include <cstdlib>
#include <set>
#include <stdlib.h>
#include <cstring>
#include <algorithm>


using namespace std;

int f_list[4][4];
int s_list[4][4];

int main(){
	freopen( "out.out", "w", stdout );
	freopen( "in.in", "r", stdin );

	int n;
	cin >> n;

	for (int I=1 ; I<n+1 ; I++){
		int f_row,s_row;
		cin >> f_row;
		for(int i=0 ; i<16 ; i++){
			int tmp;
			cin >> tmp;
			f_list[i/4][i%4] = tmp;
		}
		cin >> s_row;
		for(int i=0 ; i<16 ; i++){
			int tmp;
			cin >> tmp;
			s_list[i/4][i%4] = tmp;
		}
		int times = 0;
		int ans;


		for(int i=0 ; i<4 ; i++){
			for(int j=0 ; j<4; j++){
				if(s_list[s_row-1][i]==f_list[f_row-1][j]){
					times++;
					ans = s_list[s_row-1][i];
				}
			}
		}

		if(times==1)
			cout << "Case #"  << I << ": " << ans << endl;
		else if(times==0)
			cout << "Case #"  << I << ": " << "Volunteer cheated!" << endl;
		else
			cout << "Case #"  << I << ": " << "Bad magician!" << endl;
	}


	return 0;
}