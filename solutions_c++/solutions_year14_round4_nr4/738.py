#include "testlib.h"

#include <iostream>
#include <stdio.h>
#include <algorithm>

using namespace std;

int main(int argc, char ** argv)
{
    registerValidation();
    int n, k, d;
    n = inf.readInt(1, 100); inf.readSpace();
    k = inf.readInt(1, 100); inf.readSpace();
    d = inf.readInt(1, k); inf.readEoln();
    inf.readEof();
    return 0;
}