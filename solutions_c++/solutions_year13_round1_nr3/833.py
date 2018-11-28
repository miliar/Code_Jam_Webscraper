#ifndef GoodLuck_H_
#define GoodLuck_H_

#include <string>
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstring>

#define R 100
#define N 3
#define M 5
#define K 7

using namespace std;

class GoodLuckException {
public:
	GoodLuckException(const string& msg) : message(msg) {}
	string& what() { return message; }
private:
	string message;
};

class GoodLuck {
public:
	GoodLuck();
	GoodLuck(char* inputFile, char* outputFile);
	~GoodLuck();
	void readFile(ifstream& fileIn);
	void analyze(ifstream& fileIn);
	void writeFile() const;
private:
	long products[K];
	int digits[N];
	FILE* fileOut;
	int computeOneCase();
	//void writeLine(int lineNum, long val) const;
};



#endif /* GoodLuck_H_ */
