#include <iostream>
#include <limits.h>
#include <cmath>
#include <string>
#include <stdio.h>
#include <algorithm>
#include <stdlib.h>
#include <vector>
#include <stack>
#include <map>
#include <fstream>
#include <list>
#include <windows.h>

using namespace std;

ifstream f("nr.in");
#define cin f
ofstream g("nr.out");

int i,j,n;
string s;

int main()
{
    int t , need = 0 , toti = 0;

    cin>>t;

    for(int x = 1; x<=t ; x++)
    {
        cin>>n>>s;
        need = 0;
        toti = 0;

        for(i=0; i<s.size(); i++)
        {
            if (i > toti and s[i] != '0' and i != 0)
                {
                    need += i - toti ;
                    toti += i - toti ;
                }

            toti += s[i]-'0';
        }
        g<<"Case #"<<x<<": "<<need<<'\n';
    }


    return 0;
}
