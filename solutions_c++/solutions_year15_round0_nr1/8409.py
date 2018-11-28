#include <vector>
#include <list>
#include <map>
#include <set>
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

using namespace std;

int T,solv;
int shy,deb;
int  tab[4][4];

string ss;
int t;


int main ()
{
    freopen("A-large.in","r",stdin);
    freopen("result.txt","w",stdout);

    ss="10";
    cin >> T;
    for (int i=0;i<T;i++)
    {
        cin >> shy;

        cin >> ss;
        solv=0;
        //deb=s[0]-'0';
        deb=0;
        for (int j=0;j<(shy+1);j++)
        {
            t=ss[j]-'0';
            if (t!=0)
            {
                if (deb>=j) deb = deb+t;
                else
                {
                    solv=solv+(j-deb);
                    deb=deb+(j-deb)+t;
                }

            }

        }



            cout << "Case #" << (i+1) << ": " <<solv <<endl;



    }

}



