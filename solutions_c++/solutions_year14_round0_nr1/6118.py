
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <sstream>


using namespace std;

int toInt(std::string& str){
	int out;
	istringstream stream(str);
	stream >> out;
	return out;	
}

class CardTrick{
public:
	int grid1Row;
	int grid2Row;
	vector<int> grid1;
	vector<int> grid2;
	
	int findCard(){
		//use iterator to get the sub array iterators
		// selected row in the first grid
		vector<int>::iterator gr1_begin = grid1.begin() + (grid1Row-1)*4;
		vector<int>::iterator gr1_end = gr1_begin + 3;
		//selected rw in the second grid
		vector<int>::iterator gr2_begin = grid2.begin() + (grid2Row-1)*4;
		vector<int>::iterator gr2_end = gr2_begin + 3;
		//look for similar items
		//if there are more than two similar items the player cheated
		bool cheated = false;
		//for each element in the frist row try to find it in the second row
		int count = 0;
		int val = 0;
		for( auto it = gr1_begin ; it != gr1_end+1 ; ++it){
			if(std::find(gr2_begin, gr2_end+1, *it) != gr2_end+1){
				count++;
				val = *it;
			}
		}
		if (count == 0) return -1;
		else if (count > 1) return -2;
		else return val;
	}
};

bool readOneTestCase(CardTrick &cd){
	//read row number
	string in;
	std::getline(cin,in);
	cd.grid1Row = toInt(in);
	//read first grid
	for(int j = 0 ; j < 4 ; ++j){
		std::getline(cin,in);
		int temp[4] = {0};
		sscanf(in.c_str(), "%d %d %d %d", temp, temp+1, temp+2, temp+3);
		cd.grid1.push_back(temp[0]);
		cd.grid1.push_back(temp[1]);
		cd.grid1.push_back(temp[2]);
		cd.grid1.push_back(temp[3]);
	}
	//read second row number
	std::getline(cin,in);
	cd.grid2Row = toInt(in);
	//read second grid
	for(int j = 0 ; j < 4 ; ++j){
		std::getline(cin,in);
		int temp[4] = {0};
		sscanf(in.c_str(), "%d %d %d %d", temp, temp+1, temp+2, temp+3);
		cd.grid2.push_back(temp[0]);
		cd.grid2.push_back(temp[1]);
		cd.grid2.push_back(temp[2]);
		cd.grid2.push_back(temp[3]);
	}	
	return true;
}




int main(){
	//readfilefrom

	string in;
	std::getline(cin,in);
	int numTestCases = toInt(in);
	
	freopen("magikTricksmall.txt", "w", stdout);
	for (int i = 1 ; i <= numTestCases ; ++i){
		CardTrick cd;
		readOneTestCase(cd);
		int result = cd.findCard();
		cout << "Case #" << i ;
		if(result == -2){
			cout << ": Bad magician!";
		}
		else if(result == -1){
			cout << ": Volunteer cheated!" ; 
		}
		else{
			cout << ": " << result;
		}
		cout << endl;

	}
	
	int hi;
	
}