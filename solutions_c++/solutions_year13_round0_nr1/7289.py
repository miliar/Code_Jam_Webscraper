#include <iostream>
#include "merd.hpp"

using namespace std;



int main(int argc,char **argv)
{
    Merd app(argv[1],(char*)"output.in");
    app.Output();
    system("pause");
    return 0;
}
