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

template<uint n>
void readSomeNumbers()
{
	uint hulp;
	for(uint i = 0; i < n; i++)
	    cin >> hulp;
}

void opl()
{
    uint getallen[4];
    uint r1, r2;
    int opl = -1;
    cin >> r1;
    for(uint ri = 1; ri < r1; ri++)
	readSomeNumbers<4>();
    for(uint i = 0; i < 4; i++)
	cin >> getallen[i];
    for(uint ri = r1; ri < 4; ri++)
	readSomeNumbers<4>();
    cin >> r2;
    for(uint ri = 1; ri < r2; ri++)
	readSomeNumbers<4>();
    for(uint i = 0; i < 4; i++)
    {
	uint hulp;
	cin >> hulp;  
	if(opl!=-2)
	{
	    uint j = 0;
	    while(j < 4 && getallen[j] != hulp)
		j++;
	    if(j < 4)
	    {
		if(opl==-1)
		    opl = getallen[j];
		else
		    opl = -2;
	    }
	}
    }
    for(uint ri = r2; ri < 4; ri++)
	readSomeNumbers<4>();
    if(opl == -2)
    	cout << "Case #" << casei << ": " << "Bad magician!" << endl;
    else if(opl == -1)
    	cout << "Case #" << casei << ": " << "Volunteer cheated!" << endl;
    else
    	cout << "Case #" << casei << ": " << opl << endl;
}

