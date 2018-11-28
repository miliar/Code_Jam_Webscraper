#include <string.h>
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <typeinfo>
#include <sstream>

using namespace std;

int sizes[100][3];

int Next(int n, int a, int b){
  if (n > 1)
    return Next(n-1,sizes[n-2][0],sizes[n-2][1]) + a*b + 2;
  else
    return a*b + 2;
}

int main (int argc, char *argv[]) {

  int NPatterns = 0;
  int i,j,k;
  bool flag;
  ifstream in_stream;
  ofstream out_stream;
  string line, temp, temp1;
  vector<string> list,list1;
  std::stringstream sstm;
      
  in_stream.open(argv[1]);
  in_stream >> line;
  NPatterns = atoi(line.c_str());
 
  
  while(!in_stream.eof()){
    in_stream >> line;
    list.push_back(line);
  }

 for(i=0;i<=NPatterns;i++)
    list1.push_back("");
  
 in_stream.close();
  
  sstm.str("");
  sstm << list[0];
  sizes[0][0] = atoi(sstm.str().c_str());
  sstm.str("");
  sstm << list[1];
  sizes[0][1] = atoi(sstm.str().c_str());
  sizes[0][2] = 2;

  for(i=1;i<NPatterns;i++){
    int position = Next(i,sizes[i-1][0],sizes[i-1][1]);
    sstm.str("");
    sstm << list[position];
    sizes[i][0] = atoi(sstm.str().c_str());
    sstm.str("");
    sstm << list[position + 1];
    sizes[i][1] = atoi(sstm.str().c_str());
    sizes[i][2] = position + 2;
  }
  
  for(i=0;i<NPatterns;i++){
    std::cout << "sizes" << sizes[i][0] << "\n";
    std::cout << sizes[i][1] << "\n";
    std::cout << sizes[i][2] << "\n";
  }

  std::cout << "NPatterns=" << NPatterns << "\n";
  
  for(i=0;i<NPatterns;i++){
    
    std::cout << "start \n";
    std::cout << "i=" << i << "\n";
    flag = true;
    for(j=sizes[i][2];j<sizes[i][2]+sizes[i][0]*sizes[i][1];j++){
      
      int x = (j - sizes[i][2]) % sizes[i][1];
      int y = (j - sizes[i][2]) / sizes[i][1];

      std::cout << "i=" << i << "\n";
      std::cout << "j=" << j << "\n";
      std::cout << "x=" << x << "\n";
      std::cout << "y=" << y << "\n";
      
      std::cout << "Horizontal check \n";
      for(k=j-x;k < j-x+sizes[i][1];k++){
	std::cout << "k=" << k << "\n";
	if(list[k] > list[j]){
	  flag = false;
	  break;
	}
	std::cout << "good \n";
      }
      
      std::cout << "Vertical check \n";
      if(flag == false){
	flag = true;
	for(k=j-y*sizes[i][1];k<=j+(sizes[i][0]-y-1)*sizes[i][1];k+=sizes[i][1]){
	  std::cout << "k=" << k << "\n";
	  if(list[k] > list[j]){
	    flag = false;
	    break;
	  }
	  std::cout << "good \n";
	}
      }
      
      if(flag == false){
	sstm.str("");
	sstm << "Case #" << i+1 << ": NO";
	list1[i] = sstm.str();
	std::cout << "Failed Both \n";
	break;
      }
    }
    if(flag == true){
      sstm.str("");
      sstm << "Case #" << i+1 << ": YES";
      list1[i] = sstm.str();
    }
  }



  out_stream.open("Output1.out");
  
  for(i=0;i<list1.size();i++)    
    out_stream << list1[i] << "\n";
  

  out_stream.close();


  for(i=0;i<list1.size()-1;i++)
    std::cout << list1[i] << "\n"; 

  return 0;

}
