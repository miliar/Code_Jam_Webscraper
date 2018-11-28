/*
 * A.cpp
 *
 *  Created on: ??þ/??þ/????
 *      Author: AhmedKamal
 */

#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>
using namespace std;
#define REP(i,n) for(int(i)=0;(i)<(int)(n);(i)++)
int main(){
vector<string> values (4);
freopen("A-small-attempt0.in","rt",stdin);
freopen ("A.out","w",stdout);
int count =1;
int tcases;
cin >> tcases;
while(count <= tcases){
	bool Xwins = false;
	bool Owins = false;
	int xnum =0;
	int onum =0;
	values.clear();
	REP(i , 4)
		cin >> values[i];


	for(int j=0; j<4 && !Xwins && !Owins; j++){
		xnum =0;
		onum =0;
		for(int i=0; i<4; i++){
		if(values[j][i] == 'X' || values[j][i] == 'T')
			xnum ++;
		else if(values[j][i] == 'O' || values[j][i] == 'T')
			onum ++;
		}
		if(xnum == 4) Xwins = true;
		else if(onum == 4) Owins = true;

		}


for(int j=0; j<4 && !Xwins && !Owins; j++){
	xnum =0;
	onum =0;
	for(int i=0; i<4; i++){
		if(values[i][j] == 'X' || values[i][j] == 'T')
			xnum ++;
		else if(values[i][j] == 'O' || values[i][j] == 'T')
			onum ++;
		}
	if(xnum == 4) Xwins = true;
	else if(onum == 4) Owins = true;

	}

if(!Xwins && !Owins){
	xnum =0;
	onum =0;
	for(int i=0; i<4; i++){
		if(values[i][i] == 'X' || values[i][i] == 'T')
			xnum++;
		if(values[i][i] == 'O' || values[i][i] == 'T')
			onum++;
	}
	if(xnum == 4) Xwins = true;
	else if(onum == 4) Owins = true;

	xnum =0;
	onum =0;
	for(int i=0; i<4; i++){
		if(values[i][3-i] == 'X' || values[i][3-i] == 'T')
			xnum++;
		if(values[i][3-i] == 'O' || values[i][3-i] == 'T')
			onum++;
}
	if(xnum == 4) Xwins = true;
	else if(onum == 4) Owins = true;


	}
if(Xwins || Owins){
	if(Xwins) {cout <<"Case #"<<count<<": X won"<<endl; }
	else {cout <<"Case #"<<count<<": O won"<<endl;}

}

else {
	REP(j , 4)
			REP(i , 4)
				if(values[j][i] == '.' ) {cout<<"Case #"<<count<<": Game has not completed"<<endl; goto a;}

	 cout <<"Case #"<<count<<": Draw"<<endl;

}
a: count++;

	}
return 0;

}
