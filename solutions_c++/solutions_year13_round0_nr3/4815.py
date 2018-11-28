#include "stdafx.h"
#include <fstream>
#include <cmath>
#include <string>
using namespace std;

bool isPalindrome(int ival)
{
	char cval[5];
	sprintf(cval,"%d",ival);
	int length=strlen(cval);
	int i;
	for(i=0;i<length/2;i++){
		if(cval[i]!=cval[length-i-1])
			break;
	}
	if(i==length/2) 
		return true;
	else 
		return false;
}

int main (int argc, char *argv[])
{
	ifstream infile("C-small-attempt0.in");
	ofstream outfile("out.txt");
	int T;
	infile>>T;
	for(int i=1;i<=T;++i){
		int A,B;
		infile>>A>>B;
		int count=0;
		for(int j=A;j<=B;j++){
			if(isPalindrome(j)){
				float fval=sqrt((float)j);
				if(fval-floor(fval)>0.00001) continue;
				if(isPalindrome((int)fval))
					count++;
			}
		}
		char cval[6],countString[4];
		sprintf(cval,"%d",i);
		sprintf(countString,"%d",count);
		outfile<<"Case #"+string(cval)+": "+string(countString)<<endl;
	}
	return 0;
}

