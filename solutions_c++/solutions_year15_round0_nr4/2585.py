#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>
#include <cassert>
#include <stack>
#include <complex>
#include <utility>
#include <cstdio>

#define NODES 200002


#define MAX 200002

using namespace std;


int max(int a,int b)
{
    return a>b?a:b;
}

int min(int a,int b)
{
    return a<b?a:b;
}

int main() {
    int cases; cin >> cases;
    for(int i=1; i<=cases; i++)
    {
        bool answer = true;
        
        int x,r,c; cin >> x >> r >> c;
        
        int m = min(r,c);
        r = max(r,c);
        c = m;
        
        if (r*c%x != 0 || x > r || x>2*c)
            answer = false;
        
        if(x==2*c && x>=4)
           answer = false;
           
        if(x>7)
            answer = true;
        
        if(answer)
            cout << "Case #" << i << ": GABRIEL" << endl;
        else
            cout << "Case #" << i << ": RICHARD" << endl;
    }
}