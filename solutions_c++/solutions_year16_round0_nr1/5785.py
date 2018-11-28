#include <iostream>
#include <fstream>
using namespace std;

int main() {
	// your code goes here
	

	int test;

  ifstream myfile;
  myfile.open ("input.txt");
  myfile>>test;

  ofstream myfile2;
  myfile2.open ("output.txt");


	for (int j=0;j<test;j++){
		int number;
		int numbercopy;
		int counter=2;
		bool sleep=false;
		int digits[10]={};
		int zerocount=0;
		myfile>>number;	
		if (number==0){
			myfile2<<"Case #"<<j+1<<": "<<"INSOMNIA"<<endl;
		}
		else{
			while (!sleep){
				numbercopy=number;
			
				while (numbercopy>=1){
					digits[numbercopy%10]++;
					numbercopy/=10;
				}
	
				for (int i=0; i<10;i++){
					if (digits[i]==0){
						zerocount++;
					}
				}
				if (zerocount==0){
					sleep=true;
				}
				else{
					zerocount=0;
					number=number*counter/(counter-1);
					counter++;
				}
			}
			myfile2<<"Case #"<<j+1<<": "<<number<<endl;
		}
	
	}	



  myfile.close();
  myfile2.close();

	return 0;
	
}