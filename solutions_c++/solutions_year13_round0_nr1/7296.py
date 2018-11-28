#include <string.h>
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <typeinfo>
#include <sstream>

using namespace std;

const string WinSeq[10] =
  {"XXXX","TXXX","XTXX","XXTX","XXXT",
   "OOOO","TOOO","OTOO","OOTO","OOOT"};

int main (int argc, char *argv[]) {

  int NGames = 0;
  int i,j;
  ifstream in_stream;
  ofstream out_stream;
  string line, temp, temp1;
  vector<string> list,list1;
  std::stringstream sstm;
      
  in_stream.open(argv[1]);
  in_stream >> line;
  NGames = atoi(line.c_str());
  std::cout << NGames << "\n";
    
  while(!in_stream.eof()){
    in_stream >> line;
    list.push_back(line);
  }
  
  for(i=0;i<NGames;i++)
    list1.push_back("");

  in_stream.close();

  for(i=0;i<list.size()-1;i++){
    
    for(j=0;j<5;j++){
      if(list[i] == WinSeq[j]){
	sstm.str("");
	sstm << "Case #" << (int)(i/4)+1 << ": X won";
	list1[i/4] = sstm.str();
      }
    }
        
    for(j=5;j<10;j++){
      if(list[i] == WinSeq[j]){
	sstm.str("");
	sstm << "Case #" << (int)(i/4)+1 << ": O won";
	list1[i/4] = sstm.str();
      }
    }    
  }

  for(i=0;i<list.size()-1;i+=4){
    
    sstm.str("");
    sstm << list[i][0] << list[i+1][0] << list[i+2][0] << list[i+3][0];
    temp1 = sstm.str();
    for(j=0;j<5;j++){
      if(temp1 == WinSeq[j]){
	sstm.str("");
	sstm << "Case #" << (int)(i/4)+1 << ": X won";
	list1[i/4] = sstm.str();
      }
    }
    
    for(j=5;j<10;j++){
      if(temp1 == WinSeq[j]){
	sstm.str("");
	sstm << "Case #" << (int)(i/4)+1 << ": O won";
	list1[i/4] = sstm.str();
      }
    }

    sstm.str("");
    sstm << list[i][1] << list[i+1][1] << list[i+2][1] << list[i+3][1];
    temp1 = sstm.str();
    for(j=0;j<5;j++){
      if(temp1 == WinSeq[j]){
	sstm.str("");
	sstm << "Case #" << (int)(i/4)+1 << ": X won";
	list1[i/4] = sstm.str();
      }
    }
    
    for(j=5;j<10;j++){
      if(temp1 == WinSeq[j]){
	sstm.str("");
	sstm << "Case #" << (int)(i/4)+1 << ": O won";
	list1[i/4] = sstm.str();
      }
    }

    sstm.str("");
    sstm << list[i][2] << list[i+1][2] << list[i+2][2] << list[i+3][2];
    temp1 = sstm.str();
    for(j=0;j<5;j++){
      if(temp1 == WinSeq[j]){
	sstm.str("");
	sstm << "Case #" << (int)(i/4)+1 << ": X won";
	list1[i/4] = sstm.str();
      }
    }

    for(j=5;j<10;j++){
      if(temp1 == WinSeq[j]){	
	sstm.str("");
	sstm << "Case #" << (int)(i/4)+1 << ": O won";
	list1[i/4] = sstm.str();
      }
    }

    sstm.str("");
    sstm << list[i][3] << list[i+1][3] << list[i+2][3] << list[i+3][3];
    temp1 = sstm.str();
    for(j=0;j<5;j++){
      if(temp1 == WinSeq[j]){
	sstm.str("");
	sstm << "Case #" << (int)(i/4)+1 << ": X won";
	list1[i/4] = sstm.str();
      }
    }

    for(j=5;j<10;j++){
      if(temp1 == WinSeq[j]){
	sstm.str("");
	sstm << "Case #" << (int)(i/4)+1 << ": O won";
	list1[i/4] = sstm.str();
      }
    }
  }

  for(i=0;i<list.size()-1;i+=4){

    sstm.str("");
    sstm << list[i][0] << list[i+1][1] << list[i+2][2] << list[i+3][3];
    temp1 = sstm.str();
    for(j=0;j<5;j++){
      if(temp1 == WinSeq[j]){
	sstm.str("");
	sstm << "Case #" << (int)(i/4)+1 << ": X won";
	list1[i/4] = sstm.str();
      }
    }
    
    for(j=5;j<10;j++){
      if(temp1 == WinSeq[j]){
	sstm.str("");
	sstm << "Case #" << (int)(i/4)+1 << ": O won";
	list1[i/4] = sstm.str();
      }
    }

    sstm.str("");
    sstm << list[i][3] << list[i+1][2] << list[i+2][1] << list[i+3][0];
    temp1 = sstm.str();
    for(j=0;j<5;j++){
      if(temp1 == WinSeq[j]){
	sstm.str("");
	sstm << "Case #" << (int)(i/4)+1 << ": X won";
	list1[i/4] = sstm.str();
      }
    }

    for(j=5;j<10;j++){
      if(temp1 == WinSeq[j]){
	sstm.str("");
	sstm << "Case #" << (int)(i/4)+1 << ": O won";
	list1[i/4] = sstm.str();
      }
    }
  }

  out_stream.open("Output.out");

  for (i=0;i<list1.size();i++){
    if (list1[i] == ""){
      for (j=0;j<16;j++){
  	if (list[i*4+j/4][j%4] == '.'){
  	  sstm.str("");
	  sstm << "Case #" << (int)(i)+1 << ": Game has not completed";
	  list1[i] = sstm.str();
	  break;
  	}
  	sstm.str("");
	sstm << "Case #" << (int)(i)+1 << ": Draw";
	list1[i] = sstm.str();
      }
    }
    out_stream << list1[i] << "\n";
  }

  

  out_stream.close();

  return 0;

}
