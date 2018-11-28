#include <iostream>
using namespace std;


int main(){
	int n, caso=1;
	cin >> n;
	while(n--){
		int size, row, col;
		
		cin >> size >> row >> col;

		if(row > col){
			int aux = row;
			row=col;
			col = aux;
		}

		bool fit = true;
		if(size ==4 && row ==2 && col ==4){
			fit = false;
		}else if(size > col){
			fit = false;
		}else if( row*col % size != 0){
			fit = false;
		}else if ( (size%2==0) && size/2 > row){
			fit	= false;
		}else if((size%2!=0) && size/2+1 > row ){
			fit = false;
		}				

		cout << "Case #"<< caso++ << ": " 
				<< (fit ? "GABRIEL":"RICHARD") << endl;

	} 
	return 0;
}
