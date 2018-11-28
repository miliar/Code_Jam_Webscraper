#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    int T, cards[4][4], first, second;
    vector<int> suspects1,suspects2;
    cin >> T;
    for(int i=0; i<T; ++i){
	cin >> first;
	first = first - 1;
	for(int row=0; row<4; ++row){
	    for(int col=0; col<4; ++col){
		cin >> cards[row][col];
	    }
	}
	for(int j=0; j<4; ++j){
	    //cerr << "suspects: " << cards[first][j] << endl;
	    suspects1.push_back(cards[first][j]);
	}

	cin >> second;
	second = second - 1;
	for(int row=0; row<4; ++row){
	    for(int col=0; col<4; ++col){
		cin >> cards[row][col];
	    }
	}
	for(int j=0; j<4; ++j){
	    if(count(suspects1.begin(),suspects1.end(),cards[second][j])){
		suspects2.push_back(cards[second][j]);
		//cerr << cards[second][j] << endl;
	    }	    
	}
	cout << "Case #" << i+1 << ": ";
	if(suspects2.size()==1){
	    cout << suspects2[0] << endl;	
	}
	else if(suspects2.size()>1){
	    cout << "Bad magician!" << endl;
	}
	else if(suspects2.size()==0){
	    cout << "Volunteer cheated!" << endl;
	}
	suspects1.clear();
	suspects2.clear();
    }
}
