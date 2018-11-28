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

using namespace std;

int main()
{
    int cases; cin >> cases;
    int R,C,W;
    int Matrix[11][11];
    
    memset(Matrix, 0, sizeof(Matrix));
    
    for(int i=1; i<=10; i++)
    {
        Matrix[i][1] = i;
        Matrix[i][i] = i;
    }
    
    for(int j=2; j<=9; j++)
    {
        for(int i=j+1; i<=10; i++)
        {
            if((i-1)%j!=0)
                Matrix[i][j] = Matrix[i-1][j];
            else
                Matrix[i][j] = Matrix[i-1][j] + 1;
        }
    }
    
   
    for(int i=1; i<=cases; i++)
    {
        cin >> R >> C >> W;
        cout << "Case #" << i << ": "  << Matrix[C][W]<< endl;
    }
    
    return 0;
}