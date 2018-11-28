#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <cstring>

using namespace std;
typedef unsigned int uint;
typedef unsigned long ulong;

uint aantal;
uint casei;
void flushLine();
void opl();

string l[155];
string cl[155];

int main()
{
    cin >> aantal;
    flushLine();
    for(casei = 1; casei <= aantal; casei++)
	opl();
    return 0;
}

void flushLine()
{
    string str;
    getline(cin, str);
}

void opl()
{
    uint A, B, K;
    cin >> A >> B >> K;
    ulong opl = 0;
    for(uint i = 0; i < A; i++)
	for(uint j = 0; j < B; j++)
	    if((i&j) < K)
		opl++;
    cout << "Case #" << casei << ": " << opl << endl;
}

