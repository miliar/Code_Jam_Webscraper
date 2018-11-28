//============================================================================
// Name        : CodeJam.cpp
// Author      : 
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
using namespace std;

int main() {
	int cunt,i,j,k,l;
	bool draw_r=true, draw_c=true;
	char in;
	cin >> cunt;
	vector<vector<int> > field;
	for (k=1; k<=cunt; ++k){
		draw_r=true;
		draw_c=true;

		cin >> i;
		cin >> j;
		field = vector<vector<int> >(i,vector<int>(j,101));
		for (i=0; i<field.size(); ++i){
			for (j=0; j<field[i].size(); j++){
				cin >> field[i][j];
			}
		}
		for (i=0; i<field.size(); ++i){
					for (j=0; j<field[i].size(); j++){


						for(l=0; l<field[i].size(); ++l){
							if (field[i][l] > field [i][j]){draw_r = false; break;}
						}
						for(l=0; l<field.size(); ++l){
							if (field[l][j] > field [i][j]){draw_c = false; break;}
						}
						if (!draw_r && !draw_c) break;
						draw_r= true; draw_c =true;
					}
					if (!draw_r && !draw_c) break;
		}
		if (draw_r || draw_c)
			cout << "Case #" << k << ": YES" << endl;
		else
			cout << "Case #" << k << ": NO" << endl;

	}
	return 0;
}
