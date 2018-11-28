#include<fstream>
#include<iostream>
#include<iomanip>
#include<algorithm>
#include<vector>
#include<cmath>

using namespace std;

int main()
{
	ifstream fin("SmallA0.in");
	ofstream fout("SmallASol.out");
	int runs, strNum, goal, moves;
	float avg;
	bool valid;
	string temp;
	vector<string> input;
	vector<string> comp;
	vector<vector<int> > charNum;
	vector<int> tempIV;
	tempIV.push_back(0);
	charNum.clear();
	input.clear();
	comp.clear();
	fin >> runs;
  for(int i = 0; i < runs; i++){
		fin >> strNum;
		for(int j = 0; j < strNum; j++){
		  fin >> temp;
		  input.push_back(temp);
		  comp.push_back("");
		  comp[j] += input[j][0];
		  charNum.push_back(tempIV);
		}
		for(int j = 0; j < input.size(); j++){
		  for(int k = 0; k < input[j].size(); k++){
		    if(comp[j][comp[j].size()-1] != input[j][k]){
		      comp[j] += input[j][k];
		      charNum[j].push_back(1);
		    }
		    else{
		      charNum[j].back()++;
		    }
		  }
		}
		valid = true;
		for(int j = 0; j < strNum-1; j++){
		  for(int k = j+1; k < strNum; k++){
		    if(comp[j] != comp[k]){
		      valid = false;
		    }
      }
		}
		if(valid){
		  moves = 0;
  		for(int j = 0; j < comp[0].size(); j++){
  		  avg = 0;
  		  for(int k = 0; k < charNum.size(); k++){
  		    avg += charNum[k][j];
  		  }
  		  avg = avg/charNum.size();
  		  cout << "AVG: " << avg << endl;
  		  goal = avg;
  		  avg = avg - goal;
  		  if(avg >= 0.5) goal++;
  		  for(int k = 0; k < charNum.size(); k++){
  		    moves += abs(goal - charNum[k][j]);
  		    cout << moves;
  		  }
  		  cout << endl;
  		}
    }
		if(!valid){
		  fout << "Case #" << i+1 << ": Fegla Won" << endl;
		}
		else{
		  fout << "Case #" << i+1 << ": " << moves << endl;
		}
    input.clear();
		comp.clear();
		charNum.clear();
	}
	return 0;
}
