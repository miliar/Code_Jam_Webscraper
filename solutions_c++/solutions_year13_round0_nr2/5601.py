#ifndef LAWN_H_
#define LAWN_H_

#include <vector>
#include <iostream>

class Lawn{
public:
	Lawn(int casenum):
		casenum(casenum),possible(false),
		done(false) {readInput();};

	void readInput();
	void runCase();
	void printOutput();

private:
	void grow(int height);
	int findLowest(int prev_lowest);
	void findPaths(int height);
	bool runRow(int i);
	bool runColumn(int j);

	int casenum;
	bool possible;
	bool done;


	std::vector<std::vector<int> > grass;
	int N,M;
};


#endif /* LAWN_H_ */
