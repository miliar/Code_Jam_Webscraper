//============================================================================
// Name        : test.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================
#include <iostream>
#include <fstream>     // std::cout, std::ios
#include <sstream>      // std::stringstream

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <set>
using namespace std;

void stringToIntArray( std::string line,int* intArray, const int& intArraySize ) {
    int num, i = 0, len;
    char a[line.size()+1];
    a[line.size()]=0;
    memcpy(&a[0],line.c_str(),line.size());
    char* ap=&a[0];
    while ( sscanf( ap, "%d%n", &num, &len) == 1 && i<intArraySize) {
        intArray[i]= num;
        ap =ap+ len;    // step past the number we found
        i++;            // increment our count of the number of values found
    }
}

int test(const int& num1,const int& num2){
    int fp[5];
    int count(0);
    fp[0]=1;
    fp[1]=4;
    fp[2]=9;
    fp[3]=121;
    fp[4]=484;
    for(int i=0;i<5;i++){
      if(num1<=fp[i] && fp[i]<=num2){
        count++;
      }  
    }

    return count;

}

int main(int argc, char *argv[]) {
string line;
  ifstream myfile(argv[1]);
  int number(0);
  int caseNum(0);
  std::set<int> setOfNum;
  setOfNum.insert(1);
  setOfNum.insert(4);
  setOfNum.insert(9);
  setOfNum.insert(121);
  setOfNum.insert(484);
  
  if (myfile.is_open())
  {
      getline (myfile,line);
      
      if(number==0)  
        number=atoi(line.c_str());

      while ( caseNum<number)
      {
        getline (myfile,line);
        int matrixSize[2];
        stringToIntArray(line,&matrixSize[0],2);
        std::cout << "Case #" << caseNum+1<<": "<<test(matrixSize[0],matrixSize[1]);  
        std::cout <<std::endl;
        //std::string s
        caseNum++;
      }  
    myfile.close();
  }

  return 0;
}


/*
  for(int i=89;i<99;i++){  
    const char* temp("/home/thuha/workspace/test/src/image/img-%03d.jpg");
    char fileName[255],fileName2[255],fileName3[255];

    sprintf(fileName,temp,i);
    sprintf(fileName2,temp,i+1);    
    sprintf(fileName3,"/home/thuha/workspace/test/src/diff/img-%05d.jpg",i);    
    CImg<unsigned char> image(fileName);
    CImg<unsigned char> image2(fileName2);
    CImg<unsigned char> image3(image-image2);
    image3.save(fileName3);
    std::cout << fileName3 << std::endl;
//    CImg<unsigned char> imageDiffGrey(image.width(),image.height());
  }
  */
