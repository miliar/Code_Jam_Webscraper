#include <iostream>
#include <cmath>
#include <string>
#include <cstdlib>
#include <climits>
using namespace std;

int mingap,minc,minj;
string cmin,jmin;
string cold,jold;

void backtrack(int n, string c,string j){
	while(n < (int)cold.length() && cold[n] != '?' && jold[n] != '?') ++n;
	if(n == (int)cold.length()){
		//compare
		int cval,jval;
		cval = atoi(c.c_str());
		jval = atoi(j.c_str());
		if(abs(jval-cval) < mingap){
			mingap = abs(jval-cval);
			cmin = c;
			jmin = j;
			minc = cval;
			minj = jval;
		}else if(abs(jval-cval) == mingap){
			if(cval < minc){
				minc = cval;
				cmin = c;
				jmin = j;
			}else if(cval == minc && jval < minj){
				minj = jval;
				cmin = c;
				jmin = j;
			}
		}
//		if(c == "023") cout << n << " " << c << " " << j << " " << cmin << " " << minc << endl;
	} else if(cold[n] == '?' && jold[n] == '?'){
		for(int i = 0; i < 10; i++){
			for(int k = 0; k < 10; k++){
				c[n] = '0'+i;
				j[n] = '0'+k;
				backtrack(n+1,c,j);
			}
		}
	}else if(cold[n] == '?'){
		for(int i = 0; i < 10; i++){
			c[n] = '0'+i;
			backtrack(n+1,c,j);
		}
	}else if(jold[n] == '?'){
		for(int i = 0; i < 10; i++){
			j[n] = '0'+i;
			backtrack(n+1,c,j);
		}
	}
}



int main (){
	int ncases;
	cin >> ncases;
	for(int i = 1; i <= ncases; i++){
		mingap = INT_MAX;
		minc = INT_MAX;
		minj = INT_MAX;
		cin >> cold >> jold;
		backtrack(0,cold,jold);
		cout << "Case #" << i << ": " << cmin << " " << jmin << endl;
	}
  
	return 0;
}


