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
#include <dirent.h>
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

void test(int* elements,const int& height,const int& width){
    int maxRows[height];
    int maxCols[width];
    for(int i=0;i<height;i++)
        maxRows[i]=0;

    for(int i=0;i<width;i++)
        maxCols[i] =0;

    for(int i=0;i<height;i++)
      for(int j=0;j<width;j++){
          if(elements[i*width+j]>maxRows[i])
            maxRows[i]=elements[i*width+j];
          if(elements[i*width+j]>maxCols[j])
            maxCols[j]=elements[i*width+j];
    }
    
   for(int i=0;i<height;i++)
      for(int j=0;j<width;j++)
          if(elements[i*width+j]<maxRows[i] && elements[i*width+j]<maxCols[j] ){
            std::cout << "NO"<< std::endl;
            return;
    }
        
    std::cout << "YES"<< std::endl;
}

int main(int argc, char *argv[]) {
string line;
  ifstream myfile(argv[1]);
  int number(0);
  int caseNum(0);
  if (myfile.is_open())
  {
      getline (myfile,line);
      
      if(number==0)  
        number=atoi(line.c_str());

      char content[16];
      int pos=0;
      memset(content,0,16);
      while ( caseNum<number)
      {
        getline (myfile,line);
        int matrixSize[2];
        stringToIntArray(line,&matrixSize[0],2);
        int elements[matrixSize[0]*matrixSize[1] ];
        for(int i=0;i<matrixSize[0];i++){
          getline(myfile,line);
          stringToIntArray(line,&elements[i*matrixSize[1] ],matrixSize[1]);
        }  
        std::cout <<"Case #"<< caseNum+1 << ": ";
        test(elements,matrixSize[0],matrixSize[1]);  
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
