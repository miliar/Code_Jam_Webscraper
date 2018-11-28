#include <iostream>
#include <vector>
#include <cstdio>
#include <fstream>
#include <math.h>
#include <algorithm>
#include <set>
#include <map>
#include <sstream>


using namespace std;



//  Google codejam small -  C


int  sec_strategy (vector<double> x , vector<double>  y){

	sort(x.begin() , x.end()) ;
	sort(y.begin() , y.end()) ;


	int   counter  = 0 ;

	for ( int i = 0   ; i < y.size() ; i ++){
		if (y[i] > x[y.size() -1])
			return counter ;
		for ( int j = 0 ; j < y.size() ; j ++){
			if (x[j] == -1)
				continue ;
			if (x[j] > y[i]){
				x[j] = -1 ;
				counter ++  ;
				break ;
			}
		}
	}


	return  counter  ;
}



int  first_strategy (vector<double> x , vector<double>  y){
	sort(x.begin() , x.end()) ;
	sort(y.begin() , y.end()) ;
	int   counter  = 0 ;
	for ( int i = 0; i < x.size() ; i ++){
		bool flag = 0 ;
		bool bigger = 0;
		if (x[i]  > y[y.size() - 1])
			bigger = 1;

		for ( int j = 0; j < y.size() ; j ++ ){
			if (y[j]  == -1)
				continue ;
			if (bigger ){
				y[j] = -1 ;
				break ;
			}
			if (y[j] > x[i]){
				flag  = 1;
				y[j] = -1 ;
				break  ;
			}
		}

		if (!flag)  counter  ++ ;
	}

	return  counter  ;
}




int main() {

	int t ;
	cin >> t;

	for ( int    l = 0; l < t; l ++ ){

		int   n ;
		cin >> n;
		vector <double>  x(n) ;
		vector <double> y(n) ;
		for ( int i = 0; i < n; i ++)
			cin >> x[i]  ;
		for ( int i = 0; i < n; i ++)
			cin >> y[i]  ;


		cout << "Case #"<<l + 1 << ": "<<sec_strategy(x,y) << " " << first_strategy(x,y)<< endl;

	}
	return 0;
}
