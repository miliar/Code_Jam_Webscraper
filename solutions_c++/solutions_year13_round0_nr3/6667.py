
#include <iostream.h>
#include <fstream.h>
//#include <string.h>
#include<conio.h>
#include<math.h>

int find_fairsquares(unsigned long low,unsigned long high);

int main()
{
	clrscr();
	// files
	ifstream readFile;
	ofstream writeFile;

      //	char* fileIn="practice.txt";
	char * fileIn="small.txt";
	//string fileIn("large.txt");
	char * outFile="out.txt";
	//char * outfile="small_out.txt";
	//char * outfile="large_out.txt";
	readFile.open(fileIn);
	if (readFile.fail()){
		cout << "Could not find '" << fileIn << "'\n\n";
		return -1;
	}

	// output file
	writeFile.open(outFile,ios::out|ios::trunc);
	if (!writeFile){
		cout << "Could not find '" << outFile << "'\n\n";
		return -1;
	}


	// read # of lines
	int numCases;
	readFile >> numCases;
	// for each test case, ...
	for (int t = 0; t < numCases; ++t)
	{
		 readFile.get();//get rid of newline

	//INPUT
		unsigned long low=0, high=0;

		readFile>>low;
		readFile.get();
		readFile>>high;

		int r= find_fairsquares(low,high);

//		cout << "Case #" << t+1 << ": " << r << endl;
		writeFile << "Case #" << t+1 << ": " << r<< endl;
      }

	// close file handles
	readFile.close();
	writeFile.close();

	// no error
	return 0;
}

int find_fairsquares(unsigned long low, unsigned long high){

  int r=0;
  for(unsigned long i=low;i<=high;i++){
     double fsqri=sqrt(i);
     unsigned long isqri=fsqri;
     int issquare=0;
     if( (fsqri-isqri)==0)
	issquare=1;


     if(issquare){

	 int rev=0;

	 while(isqri){
	      int d=isqri%10;
	      isqri/=10;
	      rev=d+rev*10;
	 }
	 if(fsqri==rev){

		unsigned long k=i;
		rev=0;
		 while(k){
		      int d=k%10;
		      k/=10;
		      rev=d+rev*10;
		 }
		 if(i==rev){
			r++;
		 }
	}
      }
  }
 return r;
}