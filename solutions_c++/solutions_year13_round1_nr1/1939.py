#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <cstdlib>
#include <map>
#include <cmath>

using namespace std;

int main()
{
    ifstream fin;
    ofstream fout;

    fin.open("A-small-attempt0.txt", ios::in);
    if (!fin.is_open())
    {
        cerr << "Unable to open file" << endl;
        exit(10);
    }

    fout.open("A-small-attempt0-answer.txt", ios::out);
    if(!fout.is_open())
    {
        cerr << "Unable to open file" << endl;
        exit(10);
    }

long long int numOfCases(0), radius(0), level(0), usedLevelOnce(0), usedLevel(0), area(0), x(0), n(1), m(0);
fin >> numOfCases;

for (int i = 1; i < numOfCases+1; i++)
{   usedLevelOnce = 0;
    usedLevel = 0;
    area = 0;
    x = 0;
    n = 1;
    m = 0;

    fin >> radius;
    fin >> level;

    while (usedLevel <= level)
    {



        usedLevelOnce = (radius + n)*(radius + n) - (radius + m)*(radius + m);
        usedLevel = usedLevel + usedLevelOnce;
        x++;
        n = n+2;
        m = m+2;
    }
    x = x-1;

    cout << "Case #" << i << ": " << x << endl;
    fout << "Case #" << i << ": " << x << endl;

}









    return 0;
    }
