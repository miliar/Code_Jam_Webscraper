// CodilityProjectsCpp.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <utility>
#include <map>

using namespace std;

int standingOvation(int smax, char peopleLevels[])
{
	int nFriends = 0;
	int standing = 0;
	for (int i = 0; i < smax + 1; i++)
	{
		int friendsAdded = 0;
		if (standing < i) nFriends += (friendsAdded = i - standing);
		standing += peopleLevels[i] + friendsAdded;
	}

	return nFriends;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ofstream out("A-large.out");
	ifstream in("A-large.in");
	

	int t = 0;
	in >> t;
	
	for (int i = 0; i < t; i++)
	{
		int smax = 0;
		in >> smax;
		char c;
		char* peopleLev = new char[smax + 1];

		std::string str;
		in >> str;

		for (int i = 0; i < smax + 1; i++) peopleLev[i] = str[i] - '0';

		out << "Case #" << (i+1) << ": " << standingOvation(smax, peopleLev) << std::endl;
		delete peopleLev;
	}
	in.close();
	out.flush();
	out.close();
	
	return 0;
}

