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
	ifstream in("input.txt");
	cin >> t;
	for(int i = 0; i < t; i++)
	{
        int x, r, c;
        cin >> x >> r >> c;
        if(x == 1)
        {
            out << "Case #"<< i + 1 << ": " << "GABRIEL" << endl;//
            continue;
        }
        else if((r*c)%x != 0)
        {
            out << "Case #"<< i + 1 << ": " << "RICHARD" << endl;
            continue;
        }
        else if(x == 2)
        {
            out << "Case #"<< i + 1 << ": " << "GABRIEL" << endl;
            continue;
        }
        else if(x == 3 && r == 1 && c == 3)
        {
            out << "Case #"<< i + 1 << ": " << "RICHARD" << endl;
            continue;
        }
        else if(x == 3 && r == 3 && c == 1)
        {
            out << "Case #"<< i + 1 << ": " << "RICHARD" << endl;
            continue;
        }
        else if(x == 3)
        {
            out << "Case #"<< i + 1 << ": " << "GABRIEL" << endl;
            continue;
        }
        else if(x == 4 && r == 3 && c == 4)
        {
            out << "Case #"<< i + 1 << ": " << "GABRIEL" << endl;
            continue;
        }
        else if(x == 4 && r == 4 && c == 3)
        {
            out << "Case #"<< i + 1 << ": " << "GABRIEL" << endl;
            continue;
        }
        else if(x == 4 && r == 4 && c == 4 )
        {
            out << "Case #"<< i + 1 << ": " << "GABRIEL" << endl;
            continue;
        }
        else if(x == 4)
        {
            out << "Case #"<< i + 1 << ": " << "RICHARD" << endl;
            continue;
        }
	}
}
