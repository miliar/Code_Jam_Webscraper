#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;


int main() {

int t,g=1;
cin >> t;
while(t--)
{
    string s,z;
    cin >> s;
    z=s[0];

    for(int i=1;i<s.length();i++)
    {
        if(s[i]>=z[0])
            z=s[i]+z;
        else
            z=z+s[i];
    }

        cout << "Case #"<<g++<<": "<<z<<endl;
  
}
    return 0;
}