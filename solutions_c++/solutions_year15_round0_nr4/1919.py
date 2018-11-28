#include <cmath>
#include <cassert>
#include <cstdio>
#include <ctime>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <queue>
#include <deque>
#include <algorithm>
#include <stack>

using namespace std;

int main()
{
    freopen("D-small-attempt4.in","r", stdin);
    freopen("result.out","w", stdout);

    int T;
    int N,X,R,C,r1,r2,r3,t,c1=0,c2=0,s1=0,c10=0,large;
    string s="";

    cin>>T;
    for(int i=1;i<=T;i++)
    {
        c1 = 0;
        s="";
        cin>>X>>R>>C;
        cerr<<X<<" "<<R<<" "<<C<<"\n";
        if(X == 1)
        {
               s = "GABRIEL";
        }
        else if(X == 2)
        {
            if((R * C)%2 == 0)
                s = "GABRIEL";
            else
                s = "RICHARD";

        }
        else if(X == 3)
        {
            //if((R == 2 && C == 3) || (R == 3 && C == 2))
              //  c1 = 6;
            //if(R != 1 && C != 1 && ((R * C)%3 == 0) && c1 != 6)
            if(R != 1 && C != 1 && ((R * C)%3 == 0))
                s = "GABRIEL";
            else
                s = "RICHARD";
        }
        else if(X == 4)
        {
            if((R == 2 && C == 2) || (R == 2 && C == 4) || (R == 4 && C == 2))
                c1 = 6;
            if(R != 1 && C != 1 && ((R * C)%4 == 0) && c1 != 6)
                s = "GABRIEL";
            else
                s = "RICHARD";
        }
        cout<<"Case #"<<i<<": "<<s<<"\n";
    }

    fclose(stdout);
    fclose(stdin);
    return 0;
}
