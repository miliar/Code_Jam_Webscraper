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


using namespace std;

unsigned __int64 x;





int main(int argc, char* argv[])
{
  int numCases;
  int i,j,k,l;

  
 // ifstream fin("input.txt");FILE *f2 = fopen("output.txt","w");
 	//ifstream fin("B-large.in");FILE *f2 = fopen("B-large.out","w");
  	ifstream fin("B-small-attempt0.in");FILE *f2 = fopen("B-small-attempt0.out","w");
  //	ifstream fin("B-small-attempt1.in");FILE *f2 = fopen("B-small-attempt1.out","w");
  //	ifstream fin("B-small-attempt2.in");FILE *f2 = fopen("B-small-attempt2.out","w");
  //	ifstream fin("B-small-practice.in");FILE *f2 = fopen("B-small-practice.out","w");
  

 
  int ii;
  char temp[2000];
  fin >> numCases;
  fin.getline(temp,2000);
  long X, Y;
 
  for (ii=0;ii<numCases;++ii)
  {
	  double timetomove = 0;
   
    fin.getline(temp,2000);

    strstream ss;
    ss << temp;
    ss>> X;
    ss >> Y;

    string path;

    long x =0; 
    long y =0;
    int xdir,ydir;
    if (x==X) xdir =0;
    if (x> X) xdir = -1;
    if (x < X) xdir = 1;
    if (y==Y) ydir =0;
    if (y> Y) ydir = -1;
    if (y < Y) ydir = 1;
    bool evenStep = false;

for (j=x;j<abs(X);++j)
{
  if (xdir==1) path += "WE";
  if (xdir==-1) path += "EW";
}
for (j=y;j<abs(Y);++j)
{
  if (ydir==1) path += "SN";
  if (ydir==-1) path += "NS";
}
   
    fprintf(f2,"Case #%d: %s\n",ii+1,path.c_str());



  };
    
    
    
    
    
  
  return 0;	
}