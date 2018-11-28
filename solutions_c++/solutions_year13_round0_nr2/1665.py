// round12p2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <cassert>
#include <set>
#include <string>
#include <vector>
#include <iostream>
#include <fstream>
#include <strstream>
#include <map>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <algorithm>

#define rep(i,a,b) for(i=a;i<b;i++)
#define repz(i,n) rep(i,0,n)
#define min(x,y) ((x)>(y)?(y):(x))


using namespace std;

unsigned __int64 x;
int board[100][100];
 int rowmax[100];
 int colmax[100];
int N,M;



string Process()
{
  int i,j,k;
  for (i =0;i<100;++i) rowmax[i]=-1;
  for (i =0;i<100;++i) colmax[i]=-1;

  for (i =0;i<N;++i)
  {
    for (j=0;j<M;++j)
    {
      if (board[i][j]>rowmax[i]) rowmax[i]=board[i][j];
      if (board[i][j]>colmax[j]) colmax[j]=board[i][j];
    }
  }

  for (i =0;i<N;++i)
  {
    for (j=0;j<M;++j)
    {
      int minnum = min(rowmax[i],colmax[j]);
       if (board[i][j]<minnum) return "NO";
    }
  }

  return "YES";
}

int main(int argc, char* argv[])
{
  int numCases;
  int i,j,k,l,m;
  
//  ifstream fin("input.txt");FILE *f2 = fopen("output.txt","w");
  	ifstream fin("B-large.in");FILE *f2 = fopen("B-large.out","w");
  	//ifstream fin("B-small-attempt0.in");FILE *f2 = fopen("B-small-attempt0.out","w");
  //	ifstream fin("A-small-attempt1.in");FILE *f2 = fopen("A-small-attempt1.out","w");
  //	ifstream fin("A-small-attempt2.in");FILE *f2 = fopen("A-small-attempt2.out","w");
  //	ifstream fin("A-small-attempt3.in");FILE *f2 = fopen("A-small-attempt3.out","w");
  

 
  
  char temp[2000];
  fin >> numCases;
  fin.getline(temp,2000);

  for (i=0;i<numCases;++i)
  {
    
   
      fin.getline(temp,2000);
      strstream ss;
      ss << temp;
      ss >> N;
      ss >> M;
      for (int j=0;j<N;++j)
      {
        fin.getline(temp,2000);
        strstream ss1;
        ss1 << temp;
          for (int k=0;k<M;++k)
          {
            ss1>>board[j][k];
          }
      }


    string result = Process();
    fprintf(f2,"Case #%d: %s\n",i+1,result.c_str());

  }
    
    
    
    
    
  
  return 0;	
}


