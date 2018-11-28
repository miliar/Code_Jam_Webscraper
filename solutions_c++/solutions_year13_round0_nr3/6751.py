
#include <sstream>
#include <fstream>
#include <iostream>
#include <cmath>

using namespace std;
int check(unsigned long int n)
{	unsigned long int r,rev=0;
	unsigned long int m=n;
	while(m>0)
	{
		r=m%10;
		rev=rev*10+r;
		m=m/10;
	}
	if(n==rev)
		return 1;
	else
		return 0;
}
int main(int argc, char *argv[]){
	int tests,k,a,b,count=0;
	//setup the input file
	string dirName = "input/";
	stringstream ss;
	ss << dirName << "C-small-attempt4.in";
	puts(ss.str().c_str());
	ifstream inputFile;
	inputFile.open(ss.str().c_str());
	
	//setup the output file
	dirName = "results/";
	ss.str("");
	ss.clear();
	ss << dirName << "C-small-attempt4.out";
	puts(ss.str().c_str());
	ofstream outputFile;
	outputFile.open(ss.str().c_str());
	
	//read input file*/
	inputFile >> tests;
  cout << "Number of tests: " << tests << endl;
  for(int t = 0; t<tests; t++) {
		inputFile >> a >> b;
		count=0;
  	for(int i=a; i<=b; i++){
 		  k = sqrt(i) ;   
 		  unsigned long int sq=k*k; 
		  if (i == sq)   
			if(check(i))
				if (check(k))
					count++;		
		
  	
  	}
  
  	cout << "Case #" << t+1 << ": " << count << endl;
  	outputFile << "Case #" << t+1 << ": " << count<< endl;
  }
	
	//close the files
	outputFile.close();
	inputFile.close();
	
	return 0;
}
