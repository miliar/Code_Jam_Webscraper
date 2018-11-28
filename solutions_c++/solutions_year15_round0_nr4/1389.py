#include <iostream>
#include <cstdio>
using namespace std;
int ntest;
int X,R,C;
string ans;
int main()
{
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    cin>>ntest;
    for (int kk =1 ;kk<=ntest; kk++)
    {
        cin>>X>>R>>C;
        if (R*C % X != 0) ans = "RICHARD";
        else
        {
            if (X < 3) ans = "GABRIEL";
            else
            if (X == 3)
            {
                if (min(R,C) == 1) ans = "RICHARD";
                else
                    ans = "GABRIEL";
            }
            if (X == 4)
            {
              if (min(R,C) <= 2 ) ans = "RICHARD";
              else
                  ans = "GABRIEL";
            }
        }
        cout<<"Case #"<<kk<<": "<<ans<<"\n";
    }
    return 0;
}
