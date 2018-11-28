#pragma once
#include <iostream>
#include <string>

using namespace std;
class TestCase
{
	double C, F, X;
public:
	TestCase(fstream &);
	~TestCase(void);

	string solve();
};

