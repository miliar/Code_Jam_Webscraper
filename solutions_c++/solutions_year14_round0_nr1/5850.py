#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>  
#include <stdlib.h>  
using namespace std;

int main(){
	ifstream in("A-small-attempt1.in"); 
	ofstream out("A-small-attempt1.out"); 

   if (! in.is_open())  
   { cout << "Error opening file"; exit (1); } 
	
	int N;
	in>>N;
	
	int casenum=1;
	while(N--){
		int a1[5][5];
		int a2[5][5];
		int i1, i2;
		in>>i1;
		for (int i = 1; i <5; ++i)
		{
			for (int j = 1; j < 5; ++j)
			{	
				in>>a1[i][j];		
			}
		}

		in>>i2;
		for (int i = 1; i <5; ++i)
		{
			for (int j = 1; j < 5; ++j)
			{	
				in>>a2[i][j];		
			}
		}

		int answer;
		int count=0;
		for (int i = 1; i < 5; ++i)
		{
			for (int j = 1; j < 5; ++j)
			{
				if(a1[i1][i]==a2[i2][j]){
					count++;
					answer=a1[i1][i];
				}
			}
		}

		result: 
			out<<"case #"<<casenum++<<": ";
			if(count==1) out<<answer<<endl;
			else if(count>1) out<<"Bad magician!"<<endl;
			else out<<"Volunteer cheated!"<<endl;
	}
	out.close();
	return 0;
}
