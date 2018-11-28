#include <iostream>
#include "ProplemC.hh"
using namespace std;

int main()
{
    ProblemC p;
    p.readfile("in.txt");
    p.run();
    return 0;
}
