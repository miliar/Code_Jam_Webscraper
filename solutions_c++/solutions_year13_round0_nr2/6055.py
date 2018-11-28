#include <iostream>
#include <fstream>
#include <map>
#include <stdlib.h>
using namespace std;
struct POINT{
  int row;
  int col;

};

int toCheck = 0;
bool testPlan(multimap<int,POINT> testMap, int * data, int row, int col);

void showLown(int * data, int row, int col);
int main(int argc, char ** argv){
  ifstream inputFile;
  ofstream outputFile("output");
  int showYN = 0;
  
  if(argc < 2){
    cout << "Usage : " << argv[0] << " s/l" << endl;
    return 0;
  }
  
  if(argv[1][0] == 's'){
    inputFile.open("small");
  }else{
    inputFile.open("large");
  }
  if(argc >= 3)
    toCheck = atoi(argv[2]);
  if(argc >= 4)
    showYN = atoi(argv[3]);
  
  if(inputFile.is_open() && outputFile.is_open()){
    int gameCount;
    string line;
    inputFile >> gameCount; 
    getline(inputFile, line);

    for(int i = 1; i <= gameCount; i++){
      string result;
      int m,n;
      inputFile >> m;
      inputFile >> n;
      getline(inputFile, line);
      int * data = new int[m*n];
      int curData; 
      multimap<int, POINT > testMap;

      // store data 
      for(int row = 0; row < m; row++){
	for(int col = 0; col < n; col++){
	  // use an array to store the info
	  int index = row * n + col; 
	  inputFile >> curData; 
	  data[index] = curData;
	  // also use a sorted map to store the position information
	  POINT position = {row, col};
	  testMap.insert(pair<int,POINT>(curData, position));
	}
	getline(inputFile, line);
      }
      
      // test 
      if(i == toCheck)
	showLown(data, m, n);
      if(testPlan(testMap, data, m, n)){
	result = "YES";
	if(showYN == 1)
	  {
	    
	    cout << "Case #" << i << ": " << result << endl;
	    
	    showLown(data, m, n);
	  }
	
      }else{
	result = "NO";
	if(showYN > 1)
	  {
	    
	    cout << "Case #" << i << ": " << result << endl;
	    showLown(data, m, n);
	  }
	
      }
      if(i == toCheck){
	cout << "Case #" << i << ": " << result << endl;
      }
      outputFile << "Case #" << i << ": " << result << endl;
      delete data;
    }

    
  }else{
    cout << "Can't open file" << endl;
  }
  return 0;
}
void showLown(int * data, int row, int col){
  for(int i = 0; i < row; i++){
    for(int j = 0; j < col; j++){
      int index = i * col + j;
      cout << data[index] << " ";
    }
    cout << endl;
  }
  cout << "---------------------------------------" << endl;

}


bool testPlan(multimap<int,POINT> testMap, int * odata, int row, int col){

  //cout << "begin testing " << endl;
  //cout << endl;
  
  // iterate through the test map
  // showLown(data, row, col);
  int * data= new int[row * col];
  for(int i = 0; i < row * col; i++){
    data[i] =odata[i];
    //cout << data[i] << "    ";
  }
  multimap<int, POINT>::iterator iter;
  for(iter = testMap.begin(); iter != testMap.end(); ++iter){
    //cout << (*iter).first << " : " << (*iter).second.x << " " << (*iter).second.y <<  endl;
    int lcol, rcol, urow, drow;
    POINT pos = (*iter).second;
    int curHeight = (*iter).first;
    bool valid = false;
  
    int curIndex = pos.row * col + pos.col;
    // test row
    
    // row left
    lcol = pos.col - 1;
    while(true){
      if(lcol < 0){
	
	valid = true;
	break;
      }
      
      int lindex = pos.row * col + lcol;
      if(data[lindex] == 0 || data[lindex] == curHeight)
	lcol--;
      else{
	//cout << "Position : " << pos.row << " " << pos.col << endl;

	//cout << "fail left col" << endl;
	valid = false;
	break;
      }
    }

    // row right
    if(valid){
      rcol = pos.col + 1;
      while(true){
	if(rcol == col){
	  valid = true;
	  data[curIndex] = 0;
	  break;
	}
	int rindex = pos.row * col + rcol;
	if(data[rindex] == 0 || data[rindex] == curHeight)
	  rcol ++;
	else{
	  //cout << "Position : " << pos.row << " " << pos.col << endl;

	  //cout << "fail right col" << endl;
	  valid = false;
	  break;
	}
      }
    }
    
    if(valid) continue;

    // test col
    urow = pos.row -1;
    
    while(true){
      if(urow < 0){
	break;
      }
      int uindex = urow * col + pos.col;
      if(data[uindex] == 0 || data[uindex] == curHeight){
	urow--;
      }
      else{
	// col also fail;
	//cout << "Position : " << pos.row << " " << pos.col << endl;
	return false;
      }
    }
    drow = pos.row + 1;
    while(true){
      if(drow == row){
	break;
      }
      int dindex = drow * col + pos.col;
      //cout << "Cur : " << curHeight << "  and down row:  " << data[dindex] << endl;
      
      if(data[dindex] == 0 || data[dindex] == curHeight){
	drow++;
      }else{
	//cout << "Position : " << pos.row << " " << pos.col << endl;
	return false;
      }
    }
  }
  delete data;
  //showLown(odata, row, col);
  return true;
  
}
