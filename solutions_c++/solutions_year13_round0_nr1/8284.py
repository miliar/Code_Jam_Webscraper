
#include <iostream.h>
#include <fstream.h>
#include <string.h>
#include<conio.h>


int main()
{
	clrscr();
	// files
	ifstream readFile;
	ofstream writeFile;

	char* fileIn="practice.txt";
	//string fileIn("small.txt");
	//string fileIn("large.txt");
	char * outFile="practice_out.txt";
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
	readFile.get();  // get rid of the newline
	 cout<<"numcases="<<numCases;
	// for each test case, ...
	for (int t = 0; t < numCases; ++t)
	{
		// read a,b,c,d

		char b[4][4];
		int incomplete=0;

	//INPUT

	   for(int i=0;i<4;i++){
	      for(int j=0;j<4;j++){
		   readFile >> b[i][j];
		   if(b[i][j]=='.') {
				incomplete=1;
		   }
	      }
	      readFile.get();  // get rid of the newline
	    }
	    readFile.get();  // get rid of the newline


	int win=0;
	char s,winchar;
	//check first row for any wins, each col in 1st row, check down
	for(int j=0;j<3;j++){
		if(b[0][j]=='T')
			 s=b[1][j];
		else
			s=b[0][j];
		if(s!='.'&&(b[1][j]==s||b[1][j]=='T')&&
			(b[2][j]==s||b[2][j]=='T')&&
				(b[3][j]==s||b[3][j]=='T')){
					win=1;  winchar=s;
		}

	}

	//check 1st col, each row in 1st col, check right
	if(!win)
		for(int i=0;i<3;i++){
			if(b[i][0]=='T')
				 s=b[i][1];
			else
				s=b[i][0];
			if(s!='.'&&(b[i][1]==s||b[i][1]=='T')&&
				(b[i][2]==s||b[i][2]=='T')&&
					(b[i][3]==s||b[i][3]=='T')){
					win=1; winchar=s;
				}

		}

	if(!win){
		//check leading diag
		if(b[0][0]=='T')
			 s=b[1][1];
		else
			s=b[0][0];
		win=1;
		winchar=s;
		for(int i=1;i<4;i++)
		      if(s=='.'||(b[i][i]!=s&&b[i][i]!='T')){
				win=0;
				break;
		      }

	}

	if(!win){
		//check trailing diag
		if(b[3][0]=='T')
			 s=b[2][1];
		else
			s=b[3][0];
		win=1;
		winchar=s;
		for(int i=2;i>=0;i--)
			if(s=='.'||(b[i][3-i]!=s && b[i][3-i]!='T')){
				win=0;
				break;
			 }


	}
	char* status;
	 //finally
	if(win){
		if(winchar=='X')
		       status="X won";
		else
			status="O won";
	}
	else if(!incomplete)
	       status="Draw";
	else
	       status="Game has not completed";
	//OUTPUT
		cout << "Case #" << t+1 << ": " << status << endl;
		writeFile << "Case #" << t+1 << ": " << status<< endl;
      }

	// close file handles
	readFile.close();
	writeFile.close();

	// no error
	return 0;
}
