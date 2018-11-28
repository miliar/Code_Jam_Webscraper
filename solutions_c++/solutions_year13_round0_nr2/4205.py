#ifndef LAWNMOWER_H_
#define LAWNMOWER_H_

using namespace std;

class LawnmowerException {
public:
	LawnmowerException(const string& msg) : message(msg) {}
	string& what() { return message; }
private:
	string message;
};


class Lawnmower {
public:
	Lawnmower(char* inputFile, char* outputFile);
private:
	int** lawn;
	int numLawns;
	int rows;
	int cols;
	bool analyze();
};

#endif /* LAWNMOWER_H_ */
