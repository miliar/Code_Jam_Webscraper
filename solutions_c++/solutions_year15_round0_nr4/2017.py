#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include "fstream"

#define sz(X) ((int)X.size())
#define FOR(i,x,y) for(int i=x; i<y; ++i)

using namespace std;

#define GA "GABRIEL"
#define RI "RICHARD"

int main()
{
    ofstream cout ("output.txt");
    ifstream cin ("input.txt");

    int T;
    cin>>T;

    FOR(i,1,T+1)
    {

        int X,R,C;
        cin>>X>>R>>C;

        cout<<"Case #"<<i<<": ";

        if ((R*C) % X !=0)              cout<<RI;
        else if (X == 1)                cout<<GA;
        else if (X == 2)                cout<<GA;
        else if (X == 3)
        {
            if(R>1 && C>1)              cout<<GA;
            else                        cout<<RI;
        }
        else if(X == 4)
        {

            if(R == 1 || C==1)          cout<<RI;
            else if(R>=3 && C>=3)       cout<<GA;
            else if(R == 2 || C == 2)   cout<<RI;
            else                        cout<<RI;
        }

        cout<<endl;

    }

    return 0;
}
// END KAWIGIEDIT TESTING

//Powered by KawigiEdit 2.1.4 (beta) modified by pivanof!
