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
double C, F, X;


void readNextTestCase(FileReader& fr)
{
	C = fr.readDouble();
	F = fr.readDouble();
	X = fr.readDouble();
	
//	std::cout << "\n" << std::setprecision(9)<< C << "\t" << F << "\t" << X;
}

double getTime() {
	double cProd = 2, time1, time2, ccc=0,  time = 0.0000000;
	
	while(ccc < X) {
		time1 = (X - ccc)/cProd;
		time2 = C/cProd + X/(cProd + F);
		if(time2 < time1) {
			ccc = 0;
			time += C/cProd * 1.0;
			cProd += F;
		} else {
			if(X-ccc >= cProd) {
				ccc += cProd;
				time += 1.0;
			} else {
				time += (X-ccc)*1.0/cProd;
				ccc = X;
				break;
			}
		}
	}
	return time;
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
		cout << "Case #" << i+1 << ": " << std::setprecision(10) << getTime() << endl;
	}
	
	return 0;
}