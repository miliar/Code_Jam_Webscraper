#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <map>
#include <sstream>
#include <cmath>
using namespace std;
typedef unsigned long long int uint64;

map<uint64,bool> fairs;

bool isPalin( uint64 x )
{
    ostringstream temp;
    temp << x;
    string str( temp.str() );
    int len = str.length();
    if (len == 1) return true;
    
    for (int i=0; i<len/2; i++) {
        if (str[i] != str[len-i-1]) return false;    
    }
    return true;
}

bool isFair( uint64 x )
{
    if (fairs.find(x) != fairs.end())
       return fairs[x];
    
    uint64 root = (uint64) sqrt(x);
    if (root*root == x  && isPalin(x) && isPalin(root)) {
       fairs[x] = true;
       return true;
    }
    else {
       fairs[x] = false;
       return false;
    }
}

int main()
{
    int tests, ctr;
    uint64 a, b, i, y=0;
    cin >> tests;
    for (ctr=0; ctr<tests; ctr++) {
        cin >> a >> b;
        y = 0;
        for (i=a; i<b+1; i++) {
            if (isFair(i)) y++;
        }
        cout << "Case #" << ctr+1 << ": " << y << endl;
    }
    
    return 0;   
}
