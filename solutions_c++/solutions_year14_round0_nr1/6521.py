#pragma once
#include <iostream>
#include <string>

using namespace std;
class TestCase
{
	int _ans1, _ans2;
	int _arr1[4][4], _arr2[4][4];
public:
	TestCase(fstream &);
	~TestCase(void);

	string solve();
};

