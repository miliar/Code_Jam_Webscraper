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



//  Google codejam small -  A



int main() {

	int t ;
	cin >> t;

	for ( int    l = 0; l < t; l ++ ){

		int first , second ;
		int arr1 [4][4] ;
		int arr2 [4][4] ;

		cin >> first ;

		for ( int i = 0; i <  4 ; i ++)
			for ( int j = 0 ; j < 4 ; j ++)
				cin >> arr1[i][j] ;


		cin >> second ;
		for ( int i = 0; i <  4 ; i ++)
			for ( int j = 0 ; j < 4 ; j ++)
				cin >> arr2[i][j] ;

		int   count = 0 ;
		int num ;
		for ( int i = 0; i <  4 ; i ++)
			for ( int j = 0 ; j < 4 ; j ++){
				if (arr1[first - 1][i]  == arr2[second - 1][j]){
					count ++ ;
					num  = arr1[first - 1 ][i] ;
				}
			}


		if (count ==  1)
			cout << "Case #"<<l + 1 << ": " <<num << endl;
		else if (count > 1)
			cout << "Case #"<<l + 1 << ": " <<"Bad magician!"<< endl;
		else
			cout << "Case #"<<l + 1 << ": " <<"Volunteer cheated!"<< endl;

	}

	return 0;
}
