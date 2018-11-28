
#include <string>
#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {

	  string line;
	  ifstream input("A-large.in");
	  ofstream output("A-large.out");
      string firstLine;
      int lineNumber = 1;
	  vector<int> allDigits;
	  vector<int>::iterator idx;


	  if (input.is_open())
	  {
		  istringstream iss(line);
		  if (input.good())
		  {
			  // jump over first line
			  getline(input,line);
			  while(!input.eof()) {
				  getline(input,line);
				  istringstream buffer(line);
				  if(line == "") break;

				  // collect zeros
				  while(1) {
					  int posZ = line.find('Z');
					  if(posZ >= 0) {
						  line.erase(line.begin()+posZ);
						  //find rest
						  int posE = line.find('E');
						  line.erase(line.begin()+posE);
						  int posR = line.find('R');
						  line.erase(line.begin()+posR);
						  int posO = line.find('O');
						  line.erase(line.begin()+posO);
						  allDigits.push_back(0);
					  }
					  else break;
				  }

				  // collect twos
				  while(1) {
					  int posW = line.find('W');
					  if(posW >= 0) {
						  line.erase(line.begin()+posW);
						  //find rest
						  int posT = line.find('T');
						  line.erase(line.begin()+posT);
						  int posO = line.find('O');
						  line.erase(line.begin()+posO);
						  allDigits.push_back(2);
					  }
					  else break;
				  }

				  // collect sixes
				  while(1) {
					  int posX = line.find('X');
					  if(posX >= 0) {
						  line.erase(line.begin()+posX);
						  //find rest
						  int posS = line.find('S');
						  line.erase(line.begin()+posS);
						  int posI = line.find('I');
						  line.erase(line.begin()+posI);
						  allDigits.push_back(6);
					  }
					  else break;
				  }

				  // collect eights
				  while(1) {
					  int posG = line.find('G');
					  if(posG >= 0) {
						  line.erase(line.begin()+posG);
						  //find rest
						  int posE = line.find('E');
						  line.erase(line.begin()+posE);
						  int posI = line.find('I');
						  line.erase(line.begin()+posI);
						  int posH = line.find('H');
						  line.erase(line.begin()+posH);
						  int posT = line.find('T');
						  line.erase(line.begin()+posT);
						  allDigits.push_back(8);
					  }
					  else break;
				  }

				  // when eight is removed, only three has H
				  while(1) {
					  int posH = line.find('H');
					  if(posH >= 0) {
						  line.erase(line.begin()+posH);
						  //find rest
						  int posT = line.find('T');
						  line.erase(line.begin()+posT);
						  int posR = line.find('R');
						  line.erase(line.begin()+posR);
						  int posE = line.find('E');
						  line.erase(line.begin()+posE);
						  posE = line.find('E');
						  line.erase(line.begin()+posE);
						  allDigits.push_back(3);
					  }
					  else break;
				  }

				  // find U
				  while(1) {
					  int posU = line.find('U');
					  if(posU >= 0) {
						  line.erase(line.begin()+posU);
						  //find rest
						  int posF = line.find('F');
						  line.erase(line.begin()+posF);
						  int posO = line.find('O');
						  line.erase(line.begin()+posO);
						  int posR = line.find('R');
						  line.erase(line.begin()+posR);
						  allDigits.push_back(4);
					  }
					  else break;
				  }

				  // after four only five has f
				  while(1) {
					  int posF = line.find('F');
					  if(posF >= 0) {
						  line.erase(line.begin()+posF);
						  //find rest
						  int posI = line.find('I');
						  line.erase(line.begin()+posI);
						  int posV = line.find('V');
						  line.erase(line.begin()+posV);
						  int posE = line.find('E');
						  line.erase(line.begin()+posE);
						  allDigits.push_back(5);
					  }
					  else break;
				  }

				  // seven
				  while(1) {
					  int posV = line.find('V');
					  if(posV >= 0) {
						  line.erase(line.begin()+posV);
						  //find rest
						  int posS = line.find('S');
						  line.erase(line.begin()+posS);
						  int posE = line.find('E');
						  line.erase(line.begin()+posE);
						  posE = line.find('E');
						  line.erase(line.begin()+posE);
						  int posN = line.find('N');
						  line.erase(line.begin()+posN);
						  allDigits.push_back(7);
					  }
					  else break;
				  }

				  // nine I
				  while(1) {
					  int posI = line.find('I');
					  if(posI >= 0) {
						  line.erase(line.begin()+posI);
						  //find rest
						  int posN = line.find('N');
						  line.erase(line.begin()+posN);
						  posN = line.find('N');
						  line.erase(line.begin()+posN);
						  int posE = line.find('E');
						  line.erase(line.begin()+posE);
						  allDigits.push_back(9);
					  }
					  else break;
				  }

				  // one O
				  while(1) {
					  int posO = line.find('O');
					  if(posO >= 0) {
						  line.erase(line.begin()+posO);
						  //find rest
						  int posN = line.find('N');
						  line.erase(line.begin()+posN);
						  int posE = line.find('E');
						  line.erase(line.begin()+posE);
						  allDigits.push_back(1);
					  }
					  else break;
				  }

				  //if(lineNumber == 5) break;
				  sort(allDigits.begin(), allDigits.end());
				  cout << "Case #" << lineNumber << ": ";
				  output << "Case #" << lineNumber << ": ";
				  for(idx = allDigits.begin(); idx != allDigits.end(); ++idx) {
					  cout << *idx;
					  output << *idx;
				  }
				  allDigits.clear();
				  lineNumber++;
				  cout << endl;
				  output << endl;
			  }
		  }
	  }

}
