#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
using namespace std;
typedef long long LL;

string pancackes;
int flipnumber;

void flip(int i)
{
    flipnumber++;
    if(pancackes[0]=='+') pancackes[0] = '-';
    else pancackes[0] = '+';
    for(int j=0; j<=i; j++)
    {
        pancackes[j] = pancackes[0];
    }
}


main()
{
    FILE *fin = freopen("B-small-attempt0.in", "r", stdin);
    assert( fin!=NULL );
    FILE *fout = freopen("B-small.out", "w", stdout);
    int T;

    cin >> T;



    for(int t = 1; t <= T; t++)
    {

        flipnumber = 0;
        cin>>pancackes;

        for(int i=0; i<pancackes.length(); i++)
        {
            if(pancackes[i] != pancackes[i+1] && i!=pancackes.length()-1) flip(i);
            if(i==pancackes.length()-1)
                if(pancackes[i] == '-') flip(i);
        }
        cout << "Case #" << t << ": ";
        cout << flipnumber<< endl;

    }

    exit(0);
}
