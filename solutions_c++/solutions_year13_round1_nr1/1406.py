#ifndef Bullseye_H_
#define Bullseye_H_

#include <string>
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstring>

using namespace std;

class BullseyeException {
public:
	BullseyeException(const string& msg) : message(msg) {}
	string& what() { return message; }
private:
	string message;
};

class Bullseye {
public:
	Bullseye();
	Bullseye(char* inputFile, char* outputFile);
	~Bullseye();
	void readFile(ifstream& fileIn);
	void analyze();
	void writeFile() const;
private:
	int numCases;
	long* volume;
	long* radius;
	long* numRings;
	FILE* fileOut;
	long computeOneCase(long r, long t) const;
	void writeLine(int lineNum, long val) const;
};



#endif /* Bullseye_H_ */
