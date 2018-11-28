// stdafx.h : include file for standard system include files,
// or project specific include files that are used frequently, but
// are changed infrequently
//

#pragma once


#include <stdio.h>
#include <tchar.h>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <limits.h>

using namespace std;

bool isPrime(long long alpha);
long long fib(int index);
bool permute(int myArray[],int length);
long stringDistance(char* a,char* b,int substituteCost = 1,int insertCost=1,int deletionCost = 1);

class node;
class node
{
public:
	node();
	bool visited;
	int distance;
	vector<node*> neighbors;
	vector<int> distanceToNeighbor;
	int traverse(node* destination);
	static vector<node*> unvisited;
	bool operator<(node& lhs);
	void addNeighbor(node* rhs,int distance);
};






// TODO: reference additional headers your program requires here
