#include <iostream>
#include <fstream>
using namespace std;

int fupper(int n)
{
    if(n < 4) return 1;
    if(n < 9) return 2;
    if(n < 121) return 3;
    if(n < 484) return 4;
    return 5;
}

int flower(int n)
{
    if(n == 1) return 0;
    if(n <= 4) return 1;
    if(n <= 9) return 2;
    if(n <= 121) return 3;
    if(n <= 484) return 4;
    return 5;
}

int main()
{

    ifstream Cfile("C-small-attempt1.in");
    ofstream Canswers("CsmallAnswers.txt");

    int numtrials;
    Cfile >> numtrials;
    Cfile.ignore(255,'\n');

    int lower, upper;

    for(int trial=1; trial <= numtrials; trial++)
    {
        Cfile >> lower >> upper;
        Cfile.ignore(255,'\n');
        Canswers << "Case #" << trial << ": " << fupper(upper) - flower(lower);
        if(trial != numtrials) Canswers << endl;
    }
    return 0;
}
