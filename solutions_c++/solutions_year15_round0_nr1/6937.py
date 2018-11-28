#ifndef TESTCASE_H
#define TESTCASE_H

#include <vector>
#include <string>

class testCase
{
private:

	int maxShy;
	std::vector<int> shy;
	static int index;
	static int invites;
	static int standing;

public:

	testCase();
	testCase(std::string input);
	int testCase::Solve();
};

#endif