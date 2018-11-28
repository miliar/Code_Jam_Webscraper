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

double v1[1000];
double v2[1000];

uint calcWar(const uint size)
{
    uint war = 0;
    set<double> sv2(v2, v2+size);
    for(uint i = 0; i < size; i++)
    {
	if(v1[i] < *(sv2.rbegin()))//he beats her
	    sv2.erase(sv2.lower_bound(v1[i]));
	else
	{
	    sv2.erase(sv2.begin());
	    war++;
	}
    }
    return war;
}

uint calcDWar(const uint size)
{
    uint war = 0;
    set<double> sv1(v1, v1+size);
    for(uint i = 0; i < size; i++)
    {
	if(v2[i] < *(sv1.rbegin()))//he beats her
	{
	    sv1.erase(sv1.lower_bound(v2[i]));
	    war++;
	}
	else
	    sv1.erase(sv1.begin());
    }
    return war;
}


void opl()
{
    uint size;
    cin >> size;
    for(uint i = 0; i < size; i++)
	cin >> v1[i];
    for(uint i = 0; i < size; i++)
	cin >> v2[i];
    std::sort(v1, v1 + size, std::greater<double>());
    std::sort(v2, v2 + size);
    uint war = calcWar(size);
    uint dwar = calcDWar(size);
    cout << "Case #" << casei << ": " << dwar <<' '<< war << endl;
}

