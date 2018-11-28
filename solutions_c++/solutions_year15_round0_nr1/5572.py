#include<iostream>
#include <fstream>
#include <stdlib.h>
#include <string.h>

#define MAX_SIZE 1000 

using namespace::std;

int main()
{
	string sdata;
	char inputChar[MAX_SIZE]={0};
	int length=0, data=0, testcases=0;
	int totalAud=0, totalF=0;
	ofstream oFile("output.text");
	ifstream iFile("A-large.in");
	if(iFile.is_open()){
		iFile>>testcases;
		//oFile<<testcases<<endl;
		for(int i=1; i<=testcases; i++){
			iFile>>length>>inputChar;
			oFile<<"Case #"<<i<<": ";
			totalAud=0;
			totalF=0;
			for(int j=0; j<=length;j++){
				//sdata>>inputChar;
				switch(inputChar[j]){
					case '0': data = 0;
							break;
					case '1': data = 1;
								break;
					case '2': data = 2;
								break;
					case '3': data = 3;
								break;
					case '4': data = 4;
								break;
					case '5': data = 5;
								break;
					case '6': data = 6;
								break;
					case '7': data = 7;
								break;
					case '8': data = 8;
								break;
					case '9': data = 9;
								break;
					default: ;//do nothing
				}
				//oFile<<data<<endl;
				totalAud = totalAud+data;
				if(j+1>totalAud+totalF)
					totalF++;
			}			
			oFile<<totalF<<endl;
		}
		iFile.close();
	}
	else
		oFile<<"Can't open input file"<<endl;
	return 0;
}