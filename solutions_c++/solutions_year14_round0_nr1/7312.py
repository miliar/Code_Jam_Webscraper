#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <limits>

using namespace std;

#define MAX_TOKEN_SIZE		80

class FileReader
{
public:
   FileReader(char* fileName)
   {
		strcpy(fName, fileName);
   }
   
   void openFile()
   {
        in.open(fName);
		if(in.is_open()) {
		;//		 cout << fName << " file opened successfully ..." << endl;
	    } else {
			cout << "Unable to open " << fName << " file..." << endl;
	    }
	}
   int readInt()
   {
		int val = 0;
		if(in >> val)
			return val;
		else
			cout << "\nEOF reached ..." << endl;
		return val;
   }

   unsigned int readUInt()
   {
		unsigned int val = 0;
		if(in >> val)
			return val;
		else
			cout << "\nEOF reached ..." << endl;
		return val;
   }
   
   long readLong()
   {
		long val = 0;
		if(in >> val)
			return val;
		else
			cout << "\nEOF reached ..." << endl;
		return val;
   }
   
   unsigned long readULong()
   {
		unsigned long val = 0;
		if(in >> val)
			return val;
		else
			cout << "\nEOF reached ..." << endl;
		return val;
   }

   bool readBool()
   {
		bool val = 0;
		if(in >> val)
			return val;
		else
			cout << "\nEOF reached ..." << endl;
		return val;
   }

   float readFloat()
   {
		float val = 0;
		if(in >> val)
			return val;
		else
			cout << "\nEOF reached ..." << endl;
		return val;
   }   

   double readDouble()
   {
		double val = 0;
		if(in >> val)
			return val;
		else
			cout << "\nEOF reached ..." << endl;
		return val;
   }
   
   char readChar()
   {
		char val = 0;
		if(in >> val)
			return val;
		else
			cout << "\nEOF reached ..." << endl;
		return val;
   }
   
   string readLine()
   {
		string val;
		if(getline(in, val))
			return val;
		else
			cout << "\nEOF reached ..." << endl;
		return val;
   }
   
   string readToken()
   {
		char buff[MAX_TOKEN_SIZE], ch;
		unsigned int i=0;
		while(in>>ch)
		{
			if(ch == ' ' || ch == '\t') {
				break;
			} else {
				buff[i++] = ch;
			}
			
			if (i == MAX_TOKEN_SIZE -1)
				break;
		}
		buff[i] = NULL;
		return string(buff);
   }
   
   ~FileReader()
   {
		in.close();
   }
   
   bool isEOF()
   {
		return in.eof();
   }
   
private:
   ifstream in;
   char fName[256];
};


unsigned int testCount = 0;
int firstArr[4][4];
int secArr[4][4];
int firstNum, secNum;

void readNextTestCase(FileReader& fr)
{
	// Read the first number told by Volunteer
	firstNum = fr.readUInt();
	
	// Read the first card arrangement 
	for(int i=0; i<4; i++) {
		for(int j=0; j<4; j++) {
			firstArr[i][j] = fr.readUInt();
		}
	}
	
	// Read the second number told by Volunteer
	secNum = fr.readUInt();
	
	// Read the second card arrangement 
	for(int i=0; i<4; i++) {
		for(int j=0; j<4; j++) {
			secArr[i][j] = fr.readUInt();
		}
	}
}

string getResult() {
	char buff[512];
	
/*	cout << "\nFirst number: " << firstNum << endl;
	
	cout << "\nFirst card arrangement: " << endl; 
	for(int i=0; i<4; i++) {
		for(int j=0; j<4; j++) {
			cout << firstArr[i][j] << "\t";
		}
		cout << endl;
	}
	
	cout << "\n\nSecond number: " << secNum << endl;	
	
	cout << "\nSecond card arrangement: " << endl; 	
	for(int i=0; i<4; i++) {
		for(int j=0; j<4; j++) {
			cout << secArr[i][j] << "\t";
		}
		cout << endl;
	}
*/	
	
	// Program Logic here
	vector<bool> cardPresent;
	int cardNo;
	
	for(int i=0; i<4; i++)
		cardPresent.push_back(false);
		
	for(int i=0; i< 4; i++) {
		for(int j=0; j<4;j++) {
			if(firstArr[firstNum - 1][i] == secArr[secNum  -1][j]) {
				cardPresent[i] = true;
				cardNo = firstArr[firstNum - 1][i];
				break;
			}
		}
	}
	
	int presentCount = std::count_if(cardPresent.begin(), cardPresent.end(), [](bool val) { return (val == true);});
	if(presentCount == 0) {
		sprintf(buff, "%s", "Volunteer cheated!");
	} else if (presentCount == 1) {
		sprintf(buff, "%d", cardNo);
	} else {
		sprintf(buff, "%s", "Bad magician!");
	}
	
	
	return string(buff);
}

int main(int argc, char* argv[])
{
	FileReader fr(argv[1]);
	fr.openFile();
	
	testCount = fr.readUInt();
//	cout << "No of test cases: " << testCount << endl;
	for(int i =0; i< testCount; i++) {
		readNextTestCase(fr);
		//cout<<"\n Optimal Score is: " << getDeceitfulWarScore(NaomiM, KenM) << endl;
		cout << "Case #" << i+1 << ": " << std::setprecision(10) << getResult() << endl;
	}
	
	return 0;
}