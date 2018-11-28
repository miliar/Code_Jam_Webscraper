 
#include <iostream>

using namespace std;


int main(){
	int itr;
	cin >> itr;
	++itr;
	for(int i = 1; i < itr; ++i){
		int r, c;
		cin >> r;
		cin >> c;

		int **lawn = new int*[r];
		for(int s = 0; s < r; ++s)
			lawn[s] = new int[c];
			
		for(int row = 0; row < r; ++row)
			for(int col = 0; col < c; ++col){
				cin >> lawn[row][col];
			}
			
		bool canDo = true;	
		for(int j = 0; j < r && canDo; ++j)
			for(int k = 0; k < c && canDo; ++k){
				int cur = lawn[j][k];
				int max = cur;
				for(int q = 0; q < c; ++q){
					if(max < lawn[j][q]){
						max = lawn[j][q];
						break;
					}
				}
				if(max != cur){
					max = cur;
					for(int q = 0; q < r && canDo; ++q){
						if(max < lawn[q][k]){
							canDo = false;
							break;
						}
					}
					
				}
			}
				
		cout << "Case #" << i << ": " << ( (canDo)? "YES" : "NO") << endl;
		for(int j = 0; j < r; ++j)
				delete[] lawn[j];
		delete lawn;		
	}


}