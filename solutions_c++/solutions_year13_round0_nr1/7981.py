#include <iostream>
#include <string>
#include <vector>
#include <fstream>

using namespace std;

int N;
vector<string> data;
string str;
bool kosong = false;
int t;

int searchH(){
	bool found = true;
	int countO = 0, countX = 0, countT = 0;
	char last = 'T';
	for(int i=0; i<4; i++){
		countO = 0, countX = 0, countT = 0;
		for(int j=0; j<4; j++){
			if(data[i][j] == 'T'){
				countT++;
			}
			else if(data[i][j] == 'O'){
				countO++;
			}
			else if(data[i][j] == 'X'){
				countX++;
			}
			if(data[i][j] == '.'){
				kosong = true;
			}
		}
		if(countO > 3 || (countO == 3 && countT == 1)){
			return 1;
		}
		else if(countX > 3 || (countX == 3 && countT == 1)){
			return 2;
		}
		else
			found = false;
	}
	if(!found) return 0;
}

int searchV(){
	bool found = true;
	int countO = 0, countX = 0, countT = 0;
	char last = 'T';
	for(int i=0; i<4; i++){
		countO = 0, countX = 0, countT = 0;
		for(int j=0; j<4; j++){
			if(data[j][i] == 'T'){
				countT++;
			}
			else if(data[j][i] == 'O'){
				countO++;
			}
			else if(data[j][i] == 'X'){
				countX++;
			}
		}
		if(countO > 3 || (countO == 3 && countT == 1)){
			return 1;
		}
		else if(countX > 3 || (countX == 3 && countT == 1)){
			return 2;
		}
		else
			found = false;
	}
	if(!found) return 0;
}

int searchD1(){
	bool found;
	int countO = 0, countX = 0, countT = 0;
	char last = 'T';
	int i=0, j=0;
	while(i<=3 && j<=3){
		if(data[i][j] == 'T'){
			countT++;
		}
		else if(data[i][j] == 'O'){
			countO++;
		}
		else if(data[i][j] == 'X'){
			countX++;
		}
		i++; j++;
	}
	if(countO > 3 || (countO == 3 && countT == 1)){
		return 1;
	}
	else if(countX > 3 || (countX == 3 && countT == 1)){
		return 2;
	}
	else
		return 0;
}

int searchD2(){
	bool found;
	int countO = 0, countX = 0, countT = 0;
	char last = 'T';
	int i=0, j=3;
	while(i<=3 && j<=3){
		if(data[i][j] == 'T'){
			countT++;
		}
		else if(data[i][j] == 'O'){
			countO++;
		}
		else if(data[i][j] == 'X'){
			countX++;
		}
		i++; j--;
	}
	if(countO > 3 || (countO == 3 && countT == 1)){
		return 1;
	}
	else if(countX > 3 || (countX == 3 && countT == 1)){
		return 2;
	}
	else
		return 0;
}

int main(){
	ifstream fin ("A-small-attempt1.in");
	fin>>N;
	
	ofstream fout ("output.out");
	for(t=1; t<=N; t++){
		data.clear();
		for(int i=0; i<4; i++){
			fin>>str;
			data.push_back(str);
		}
		/*for(int i=0; i<4; i++){
			fout<<data[i]<<endl;
		}*/
		fout<<"Case #"<<t<<": ";
		if(searchH() == 1 || searchV() == 1 || searchD1() == 1 || searchD2() == 1){
			fout<<"O won";
		}
		else if(searchH() == 2 || searchV() == 2 || searchD1() == 2 || searchD2() == 2){
			fout<<"X won";
		}
		else{
			if(kosong){
				fout<<"Game has not completed";
			}
			else fout<<"Draw";
		}
		fout<<endl;
	}
	return 0;
}