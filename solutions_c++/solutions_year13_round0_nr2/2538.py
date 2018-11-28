#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

#define D 128
/* Global variables */
int lawn[D][D];
int n;
int m;
/* prototypes */


void printMap(){
	for(int i=0; i<n; i++){
	for(int j=0; j<m; j++){
		cout << lawn[i][j] << " ";
	}
	cout << endl;
	}
	cout << endl;
	return;
}

/*
void printVector(){
	for(vector<vector<int> >::iterator it= largest.begin(); it != largest.end(); it++){
 		cout << "(" << (*it)[1] << "," << (*it)[2] << ")" << (*it)[0] << " ";
	}		
	cout << endl;
	return;
}
*/

bool rank(vector<int> v1, vector<int> v2){
	//if(v1[0] != v2[0]){
		return v1[0] < v2[0];
	//} 
	/*else{
		return (v1[1] > v2[1]) or !(v1[1] == 0 or v1[1] == (n-1) or v1[2] == 0 or v1[2] == (m-1) );
	}*/
}

bool canBeCut(vector<int> vec){
	int height = vec[0];
	//lawn[vec[1]][vec[2]] = 0;
	
	bool doable = true;
	// horizontal
	for(int j=0; j< m; j++){
		if(lawn[vec[1]][j] > height ){
		/*	cout << "j is " << j << endl;
			cout << "vec[1] is" << vec[1] << endl;
			cout << "vec[2] is" << vec[2] << endl;
			cout << "height is " << height << endl;
			cout << "height surrounding is " << lawn[vec[1]][j] << endl;
		*/	doable = false;
			break;
		}
	}
	if(doable){
		return true;
	}
	// if not doable yet, check vertical
	// vertical
	for(int i=0; i< n; i++){
		if(lawn[i][vec[2]] > height){
		//	cout << "i is " << i << endl;
			return false;
		}
	}

	return true;
}


int main(){
	int numCases;
	cin >> numCases;
	for(int caseN=1; caseN <= numCases; caseN++){
		cin >> n;
		cin >> m;
		for(int i=0; i<n; i++){
		for(int j=0; j<m; j++){
			cin >> lawn[i][j];
		}
		}	
		// lawn is stored
		//printMap();

		vector<vector<int> > largest(m*n, vector<int>(3) );
		int it=0;
		// find the largest number
		for(int i=0; i< n; i++){
		for(int j=0; j< m; j++){
			largest[it][0] = lawn[i][j];
			largest[it][1] = i;
			largest[it][2] = j;
			
			it++;
		}
		}
		//sort(largest.begin(), largest.end(), rank);		// sort by descending
		//printVector();

		bool doable = true;
		for( it = 0; it < n*m ; it++){
		//	cout << "Coordinates  are " << largest[it][1] << " ";
			if(!canBeCut(largest[it])){
				doable = false;
				break;
			}
		}
		


		cout << "Case #" << caseN << ": " << ( doable?"YES":"NO" ) << endl;
	}
}
