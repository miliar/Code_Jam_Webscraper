#import <iostream>
#import <fstream>
#import <sstream>

using namespace std;


int main(){
	int cases=0, guess1=0, guess2=0, answer=0, nanswers=0;
	int arrangem1[4][4];
	int arrangem2[4][4];
	string line;
	stringstream sline;
	ifstream inputf;
	inputf.open("in.txt");
	if(!inputf.good()){
		cout<< "file error" << endl;
		exit(0);
	}
	if(!inputf.eof()){
		getline(inputf, line);
		sline.clear(); sline.str("");
		sline << line;
		sline >> cases;
		
	
		for(int c = 1; c< cases+1; ++c){
			
			getline(inputf, line);
			
			sline.clear(); sline.str("");
			sline << line;
			
			sline >> guess1;
			
			
			for(int i = 0; i < 4; ++i){
				getline(inputf, line);
				
				sline.clear(); sline.str("");
				sline << line;
				sline >> arrangem1[i][0] >> arrangem1[i][1] >> arrangem1[i][2] >> arrangem1[i][3];
				
			}
			getline(inputf, line);
			
			sline.clear(); sline.str("");
			sline << line;
			sline >> guess2;
			for(int i = 0; i < 4; ++i){
				getline(inputf, line);
				
				sline.clear(); sline.str("");
				sline << line;
				sline >> arrangem2[i][0] >> arrangem2[i][1] >> arrangem2[i][2] >> arrangem2[i][3];
				
			}
			
			nanswers = 0;
			for(int i = 0; i<4; ++i){
				
				for(int j = 0; j<4; ++j){
					
					if( arrangem1[guess1-1][i] == arrangem2[guess2-1][j]){
						answer = arrangem1[guess1-1][i];
						++nanswers;
					}
				}
			}
			cout << "Case #" << c << ": ";
			if(nanswers == 0){
				cout<< "Volunteer cheated!" << endl;
			}
			else if(nanswers == 1){
				cout << answer << endl;
			}
			else {
				cout << "Bad magician!" << endl;
			}
			
		}
	}
}
