#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <sstream>
using namespace std;


int fq, sq;

ifstream fin ("A-small-attempt1.in");
ofstream fout ("A-small-attempt1.out");

//ifstream fin ("test2.in");
//ofstream fout ("test2.out");

	
int cards1[4][4];
int cards2[4][4];

vector<int> possible;

string IntToString (int a)
{
    ostringstream temp;
    temp<<a;
    return temp.str();
}
	
void getCards(int cards[][4]){
	for(int i = 0; i < 4; i++){
		for(int j = 0; j < 4; j++){
			fin >> cards[i][j];
			//cout << cards[i][j] << " ";
		}
		//cout << endl;
	}
	//cout << " ---" << endl;
}

string make(){
	string str;
	possible.clear();
	for(int i = 0; i < 4; i++){
		possible.push_back(cards1[fq-1][i]);
		//cout << possible[i] << " ";
	}
	//cout << endl;
	
	
	bool found = false;
	for(int i = 0; i < possible.size(); i++){
		for(int j = 0; j < 4; j++){
			////cout << "checking last " << possible[i] << " with new " << cards2[sq-1][j] << endl;
			if(possible[i] == cards2[sq-1][j]){
				found = true;
				break;
			}
		}
		
		////cout << "found? " << found << " and checking " << possible[i] << endl;
		if(!found){
			possible.erase(possible.begin() + i);
			i--;
		}
		found = false;
	}
	
	if ( possible.size() == 1){
		str = IntToString(possible[0]);
		return str;
		
	}
		
	if ( possible.size() > 1)
		return "Bad magician!";
	
	return "Volunteer cheated!";
}
int main() { 
	int t;
	
	fin >> t;
	
	
	for (int i = 0; i < t; i++){
		//cout << "new test" << endl;
		fin >> fq;
		getCards(cards1);
		fin >> sq;
		getCards(cards2);
		fout<<"Case #"<<i+1<<": "<<make()<<endl;
	}
  
    return 0;
}
