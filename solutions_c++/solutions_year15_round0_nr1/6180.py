#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <iostream>
#include <string.h>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
#define inf (long long)1e15
#define MAX_N 20

using namespace std;

int main()
{
	long long int t;
	ofstream out("output.txt");
	cin >> t;
	for(int i = 0; i < t; i++)
	{
	    long long int k;
	    cin >> k;
		string input;
		cin >> input;
		long long int cummul = 0;
		long long int rez = 0;
        cummul = input[0] - '0';
		for(int required = 1; required < input.length(); required++)
		{
			if(cummul < required)
			{
			     	int temp = required - cummul;
			     	rez += temp;
			     	cummul += temp;
			}
			cummul += input[required] - '0';
		}
		out << "Case #"<< i + 1 << ": " << rez << endl;
	}
}
