# include <iostream>
# include <math.h>
# include <stdio.h>
# include <string.h>
# include <algorithm>
# include <vector>
# include <fstream>
# include <limits.h>

using namespace std;

//ifstream INPUT_FORMAT ("");
ofstream fout ("file.txt");

int T;
double C,F,X,income=2.0,cookie_NUM=0.0,time=0.0;

int main(){
	
	cin >> T;
	for ( int i=0; i<T; i++ ){
		cin >> C >> F >> X;
		
		double mn=(double)X/income;
		for ( int j=1; j<(int)(X); j++ ){
			time+=( C/income );
			income+=F;
			
			mn=min( mn , time+(X/income) );
		}
		
		income=2.0 , time=0.0;
		
		fout.precision(7);
		fout << "Case #" << i+1 << ": " << fixed << mn << endl;
	}
	
	return 0;
}
