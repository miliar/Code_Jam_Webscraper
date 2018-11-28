
#include <iostream>
#include <vector>


using namespace std;


int main(int argc, char** argv){

	int T, af, as;
	int field_one[4][4], field_two[4][4];
	vector< int > selected;

	cin >> T;

	for( int i=1; i <= T; i++ ){

		cin >> af;

		for( int j=0; j < 4; j++ ){
			for( int k=0; k < 4; k++ ){
				cin >> field_one[j][k];
			}
		}
		
		cin >> as;

		for( int j=0; j < 4; j++ ){
			for( int k=0; k < 4; k++ ){
				cin >> field_two[j][k];
			}
		}

		for( int j=0; j < 4; j++ ){
			for( int k=0; k < 4; k++ ){
				if( field_one[af-1][j] == field_two[as-1][k] ){
					selected.push_back( field_one[af-1][j] );
				}
			}
		}

		/*for( int j=0; j < selected.size(); j++ ){
			cout << selected[j] << endl;
		}*/

		if( selected.size() == 0 ){
			cout << "Case #" << i << ": Volunteer cheated!\n";
		}
		else{
			if( selected.size() == 1 ){
				cout << "Case #" << i << ": " << selected[0] << "\n";
			}
			else{
				cout << "Case #" << i << ": Bad magician!\n";
			}
		}

		//Next test
		selected.resize(0);

	}


		

	return 0;
}






