#include <iostream>
#include <algorithm>
#include <cstring>
#include <map>
#include <set>
#include <vector>
#include <stack>
#include <queue>
#include <utility>
#include <sstream>
#include <bitset>
#include <stdio.h>
#include <string.h>
#include <math.h>

using namespace std;

int i , j , k;

int main ()
{
	int ncases;
	int row;
	int val;
	int resp[4];
	int matrix[4][4];
	int cont;
	
	cin >>ncases;
	for ( i=1; i <= ncases;i++){
		cin >>row;
		row--;
		for ( j =0; j < 4;j++){
			for ( k =0; k < 4;k++){
				cin >>matrix[j][k];
			}
		}
		
		//get all the answers
		for ( j =0; j < 4;j++){
			resp[j] = matrix[row][j];
		}
		cin >>row;
		row--;
		//prublic again
		for ( j =0; j < 4;j++){
			for ( k =0; k < 4;k++){
				cin >>matrix[j][k];
			}
		}
		for ( j =0; j < 4;j++){
			cout <<	resp[j]<<" ";
		}
		cout <<endl;
		//see if just one is right
		cont =0;
		for ( j =0; j < 4;j++){
			
			for ( k =0; k < 4;k++){//los que tengo ua almacenados
				if ( resp[k] == matrix[row][j]){
					cont++;
					val = resp[k];
				}
			}
		}
		
		if ( cont == 1 )
			cout <<"Case #"<<i<<": "<<val<<endl;
		else if ( cont > 1)
			cout <<"Case #"<<i<<": Bad magician!"<<endl;
		else
			cout <<"Case #"<<i<<": Volunteer cheated!"<<endl;
		
		
	}
	
		
	return 0;
	

}




