#include <bits\stdc++.h>
#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <utility>
#include <deque>
#include <algorithm>
#include <string>
#include <sstream>
#include <fstream>
using namespace std;
//#define f  cin
//#define ff cout



int main()
{
    ios_base::sync_with_stdio(false);
    fstream f("fileName.in" , ios::in);
    fstream ff("fileName.out" , ios::out);
    int64_t t; f >> t;
    for(int64_t q = 0; q < t; q++)
    {
        int x , r , c;
        string ans;
        f >> x >> r >> c;
        if(x == 1)
        {
            ans = "GABRIEL";
        }
        else if(x == 2)
        {
            if((r*c)%2)
                ans = "RICHARD";
            else
                ans = "GABRIEL";

        }
        else if(x == 3)
        {
            if((r*c)%3)
                ans = "RICHARD";
            else if(r*c == 3)
                ans = "RICHARD";
            else if(r*c == 6)
                ans = "GABRIEL";
            else if(r*c == 9)
                ans = "GABRIEL";
            else if(r*c == 12)
                ans = "GABRIEL";
        }
        else if(x == 4)
        {
            if((r*c)%4)
                ans = "RICHARD";
            else if(r*c == 4)
                ans = "RICHARD";
            else if(r*c == 8)
                ans = "RICHARD";
            else if(r*c == 12)
                ans = "GABRIEL";
            else if(r*c == 16)
                ans = "GABRIEL";
        }
        ff << "Case #"; ff << q+1; ff << ": "; ff << ans; ff << '\n';
    }
}
