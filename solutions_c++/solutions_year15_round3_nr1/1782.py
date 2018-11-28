#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
using namespace std;
#define ll long long int


int main()
{
    int tc,r,c,w,i;
    cin >> tc;
    for(i=0;i<tc;i++)
    {
        cin >> r >> c >> w;
        int range=ceil((float)c/w);
        cout <<"Case #" << i+1 << ": " << (range*r)+w-1 << "\n";
    }
}
