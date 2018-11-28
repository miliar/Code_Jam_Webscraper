#include <iostream>
#include <iomanip>
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

double calc(const double C, const double F, const double X, const double v)
{
    double tf = X/v;
    double tfmc = C/v + X/(v+F);
    if(tf < tfmc)
	return tf;
    else 
	return calc(C,F,X,v+F)+C/v;
}

double calc(const double C, const double F, const double X)
{
    return calc(C,F,X,2);
}

void opl()
{
    double C, F, X;
    cin >> C;
    cin >> F;
    cin >> X;
    cout << "Case #" << casei << ": " << setprecision(20) << calc(C,F,X) << endl;
}

