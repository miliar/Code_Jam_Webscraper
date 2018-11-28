#include <stdio.h>
#include <stdlib.h>
#include <cstdlib>
#include <math.h>
#include <iostream>
#include <string>
#include <ctime>
//#include <string.h>
#include <fstream>
#include <sstream>
#include <map>
#include <vector>
#include <algorithm>
#include <queue>
#include <set>


using namespace std;



int main() 
{

	ifstream fin("A-large.in");  
	ofstream fout("output.out");

	/*ifstream fin("input.txt");  
	ofstream fout("output.out");*/
	
	int T;
	fin>>T;
	
	
	for (int cnt=1; cnt<=T; cnt++)
	{
		int start_index=1500;
		int left_index=start_index-1;
		int right_index=start_index+1;
		char word[3000];
		char largest;
		string s;
		fin>>s;
		largest=s[0];
		word[start_index]=largest;

		for (int i=1; i<s.length(); i++)
		{
			if (s[i]>=largest)
			{
				word[left_index--]=s[i];
				largest=s[i];
			}
			else
			{
				word[right_index++]=s[i];
			}
		}

		fout<<"Case #"<<cnt<<": ";
		for (int i=left_index+1; i<right_index; i++)
			fout<<word[i];
		fout<<endl;
	}




	


	
		



	//system("pause");
	//return 0;
}
