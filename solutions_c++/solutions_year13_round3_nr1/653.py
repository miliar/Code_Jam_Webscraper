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

string name;
bool endsc[1000004];


int main(int argc, char* argv[])
{
  int numCases;
  int i,j,k,l,m;
  
 // ifstream fin("input.txt");FILE *f2 = fopen("output.txt","w");
  	ifstream fin("A-large.in");FILE *f2 = fopen("A-large.out","w");
  //	ifstream fin("A-large-practice.in");FILE *f2 = fopen("A-large-practice.out","w");
  //ifstream fin("A-small-practice.in");FILE *f2 = fopen("A-small-practice.out","w");
  //	ifstream fin("A-small-attempt0.in");FILE *f2 = fopen("A-small-attempt0.out","w");
  //	ifstream fin("A-small-attempt1.in");FILE *f2 = fopen("A-small-attempt1.out","w");
  //	ifstream fin("A-small-attempt2.in");FILE *f2 = fopen("A-small-attempt2.out","w");
  //	ifstream fin("A-small-attempt3.in");FILE *f2 = fopen("A-small-attempt3.out","w");
  

 
  
  char temp[1000090];
  int n;
  fin >> numCases;
  fin.getline(temp,1000090);
  double count;
  
  for (int ii=0;ii<numCases;++ii)
  {
    fin.getline(temp,1000090);
	name.clear();

    strstream ss;
    ss << temp;
	  ss>>name;
    ss >> n;
  count  = 0;  
    int nrep = 0;
      for (j=0;j<name.length();++j)
      {
        endsc[j]=false;
      }
    for (j=0;j<name.length();++j)
    {
      char currchar = name[j];
      if ( (currchar=='a')||(currchar=='e')||(currchar=='i')||(currchar=='o')||(currchar=='u'))
      {
        nrep =0;
      }
      else
      {
        ++nrep;
        if (nrep>=n) endsc[j]=true;
      }
    }
    
    long currenttrue = 1000001;
     for (j=0;j<name.length();++j)
     {
       if (endsc[j]) {currenttrue = j; break;}
     }

     if (currenttrue == 1000001 ) {
       fprintf(f2,"Case #%d: %d\n",ii+1,0);
     }
     else
     {
       for (j=0;j<name.length();++j)
       {
         while (j>(currenttrue+1-n))
         {
           //find next currenttrue
           bool done = false;
           while (!done) { ++currenttrue; if (currenttrue>=name.length()) done= true; else if (endsc[currenttrue]==true) done = true;}
         }
         if( (j<=(currenttrue+1-n)) && (currenttrue < name.length()) ) count += (name.length()-currenttrue);
       }
       fprintf(f2,"Case #%d: %.0lf\n",ii+1,count);

     }

		
  }
	 
  
  return 0;	
}