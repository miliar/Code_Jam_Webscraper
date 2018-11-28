#include<cstdio>
#include<iostream>
#include<string>
using namespace std;


int main()
{
    int test, T, Smax;
    string Slevel;
/*
freopen("A.in", "r", stdin);
freopen("A.out", "w", stdout);
*/
    cin>>test;
    for(T = 1; T <= test; T++)
    {
        cin>>Smax>>Slevel;
        int counter = 0;
        int total = 0;
        for(int I = 0; I < Slevel.size(); I++)
        {
            if(Slevel[I] != '0' && I > total)
            {
                counter += (I - total);
                total += (I - total);
            }
            total += (Slevel[I] - '0');
        }
        printf("Case #%d: %d\n", T, counter);
    }

    return 0;
}
