#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <utility>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <stack>
#include <string>
#include <algorithm>
#include <iostream>
#include <sstream>

using namespace std;

bool isPalin(long long n)
{
    stringstream ss;
    ss << n;
    string s = ss.str();
    for(int i=0; i<s.size(); i++)
        if(s[i] != s[s.size()-1-i])
            return false;
    return true;
}

long long palindromize(int n, bool even)
{
    stringstream ss;
    ss << n;
    string s = ss.str();
    ss.str("");
    int size = s.size();
    if(even)
        for(int i=0; i<size; i++)
            s += s[size-1-i];
    else
        for(int i=0; i<size-1; i++)
            s += s[size-2-i];
    long long p;
    ss << s;
    ss >> p;
    return p;
}

int main()
{
    vector<long long> fairSquare;
    for(int i=1; i<10000; i++)
    {
        long long odd = palindromize(i,false);
        long long even = palindromize(i,true);
        if(isPalin(odd*odd))
            fairSquare.push_back(odd*odd);
        if(isPalin(even*even))
            fairSquare.push_back(even*even);
    }
    int T;
    cin >> T;
    for(int t=1; t<=T; t++)
    {
        int A,B;
        cin >> A >> B;
        int num=0;
        for(int i=0; i<fairSquare.size(); i++)
            if(fairSquare[i] >= A && fairSquare[i] <= B)
                num++;
        cout << "Case #" << t << ": " << num << endl;
    }
}
