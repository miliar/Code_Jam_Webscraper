#include "stdafx.h"
#include <fstream>
#include <stdlib.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>


using namespace std;


int gcc(int x,int y)
{
 int k;
 if(x<y)
 {
  k=x;
  x=y;
  y=k;
 }
 if(x%y==0)
  return abs(y);
  else    
 return gcc(y,x%y);   
}

inline int s2i(string p)
{
	int re;
	stringstream(p) >> re;
	return re;
}


int _tmain(int argc, _TCHAR* argv[])
{

	vector <long long > B;
	int numca,n,a,b,m,k;
	vector  <int > map[1005];
	vector  <int > mapc[1005];

	ifstream fin("e:\\ggg.txt");
	ofstream fout("e:\\7.txt");
	fin>>numca;
	fin.ignore();
	for (long long ii=0;ii<numca;ii++)
	{
		int min_v;
		string sss,s1,s2;
		
		std::getline(fin,sss);
		int pos=sss.find('/');
		s1=sss.substr(0,pos);
		s2=sss.substr(pos+1);
		
		
		istringstream buffer(s1);
        long long ss1,ss2;
        buffer >> ss1;   

		istringstream buffer1(s2);
        buffer1 >> ss2;   
		

		ss1=s2i(s1);
		ss2=s2i(s2);
		cout<<ss1<<" "<<ss2<<endl;
		int tt=gcc(ss1,ss2);


		
		ss1/=tt;
		ss2/=tt;
		

		


		if ((ss2&(ss2-1))!=0)
		{
			fout<<"Case #"<<ii+1<<": "<<"impossible" <<endl;
			continue;
		}
		int g=0;


		while (ss1<ss2)
		{
			ss1*=2;
			g++;
		}
		fout<<"Case #"<<ii+1<<": "<<g <<endl;
	}

	return 0;
}

