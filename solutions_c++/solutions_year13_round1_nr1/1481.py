/**
ID: coboy122
PROG: A
LANG: C++
**/

#include<iostream>
#include<fstream>
#include<algorithm>
#include<string>
#include<vector>
#include<set>
#include<queue>
#include<cstring>
#include<cmath>

using namespace std;


void work()
{
    int T ; 
    cin >> T ; 
    for(int cases = 0 ; cases < T ; cases ++)
    {
    long long r,t;
    cin  >> r >> t;
    int count=0 ; 
    while(t > 0)
    {
        long long area = (r+1)*(r+1) - r*r ; 
        if(t >= area) 
        {
            count ++ ; 
            t = t - area ; 
            r = r + 2 ;  
        } 
        else 
            break;
    }    
        cout << "Case #" << (cases+1) << ": " << count << endl; 
    }
}

int main()
{
    work();
    return 0; 
}
