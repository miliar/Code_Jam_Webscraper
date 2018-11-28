#include <iostream>
#include <fstream>
#include <stdlib.h> 
#include <string>
#include <algorithm>
#include <math.h>  

using namespace std;

/*
int atoichar(char a)
{
	if(a=='0') return 0;
	if(a=='1') return 1;
	if(a=='2') return 2;
	if(a=='3') return 3;
	if(a=='4') return 4;
	if(a=='5') return 5;
	if(a=='6') return 6;
	if(a=='7') return 7;
	if(a=='8') return 8;
	if(a=='9') return 9;
	
}
*/
bool cmp(int x,int y){return x>y;}

int main()
{
	
	 ifstream fin;
 	 fin.open("B-large.in");
 	  if (!fin.good()) throw "I/O error";
	int tests;
	fin>>tests;
	ofstream fout;
  	fout.open("datalargeBreallylarge.txt");
	for(int count = 1;count <=tests;count++)
	{
		int D;
		fin>>D;
		//cout<<D<<endl;
		int * P = new int [D];
		for(int count1 = 0;count1<=D-1;count1++)
		{
			fin>>P[count1];
		}
		
		sort(P,P+D,cmp);
		int min  = P[0];
	//	cout<<P[0]<<endl;
		for(int count2 = 1;count2<=P[0]-1;count2++)
		{
			int tempans =count2;
			for(int count3 =1;count3<=D;count3++ )
			{
				tempans +=(ceil(((double)P[count3-1])/count2)-1);
			}
			if (tempans<min) 
			{
				min = tempans; //cout<<count2<<endl;
			}
			if(count2 >=min) break;
		}
		fout<<"Case #"<<count<<": "<<min<<endl;
		
	}
	
}

