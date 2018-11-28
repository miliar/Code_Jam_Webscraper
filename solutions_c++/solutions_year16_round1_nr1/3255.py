#include <iostream>
#include <iomanip>
#include <string>
#include <cstring>
#include <cstdio>
#include <queue>
#include <stack>
#include <algorithm>
#include <cmath>
#include <list>
#include <map>
#include <fstream>
using namespace std;
#define MAX_N 101

int main()
{
    ifstream fin;
    fin.open("A-large.in");
    ofstream fout;
    fout.open("R.txt");

    int T;
    fin>>T;
    for(int t=1;t<=T;t++)
    {
        string s;
        fin>>s;
        string result="";
        result+=s[0];
        for(int i=1;i<s.length();i++)
        {
            if(s[i]>=result[0])result=s[i]+result;
            else result+=s[i];
        }
        fout<<"Case #"<<t<<": "<<result<<endl;

    }


}
