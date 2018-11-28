#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

struct Cards{
	int row;
	int card[4][4];
	Cards(){
		cin >> row;
		for( int iy=0; iy<4; iy++ )
			for( int ix=0; ix<4; ix++ )
				cin >> card[ix][iy];
	}
	vector<int> getRow(){
		vector<int> values;
		for( int i=0; i<4; i++ )
			values.push_back( card[i][row-1] );
		return values;
	}
};

struct Magic{
	Cards first;
	Cards second;
	
	string result(){
		vector<int> out(8);
		auto row1 = first.getRow();
		auto row2 = second.getRow();
		sort( row1.begin(), row1.end() );
		sort( row2.begin(), row2.end() );
		auto it = set_intersection( row1.begin(), row1.end(), row2.begin(), row2.end(), out.begin() );
		int amount = it - out.begin();
		switch( amount ){
			case 0: return "Volunteer cheated!";
			case 1: return to_string( out[0] );
			default: return "Bad magician!";
		}
	}
};

int main( int, char** ){
	int amount;
	cin >> amount;
	for( int i=1; i<=amount; i++ )
		cout << "Case #" << i << ": " << Magic().result() << endl;
	
	return 0;
}