#include <stdlib.h>
#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>
#include <cmath>
#include <deque>
#include <map>
#include <iostream>
#include <set>
#define FOR(x,z) for(int x=0;x<(z);++x)
#define DS(i) fprintf(stderr, "DEBUG: %s\n",i);
#define DI(i) fprintf(stderr, "DEBUG: %d\n",i);
#define DF(i) fprintf(stderr, "DEBUG: %f\n",i);
using namespace std;
string S;

vector<string> vec = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

void wczytaj()
{
    cin >> S;

}
void wykonaj()
{
    int c['Z'-'A'+1] = {};
    for(char a: S)
        c[a-'A']++;

    int l[10] = {};
 //   DI(1)
    while(c['Z'-'A']) // 0
    {
        l[0]++;
        FOR(i,vec[0].length())
        {
            c[vec[0][i]-'A']--;
        }
    }
//DI(2)
    while(c['U'-'A']) // 4
    {
        l[4]++;
        FOR(i,vec[4].length())
        {
            c[vec[4][i]-'A']--;
        }
    }
//DI(3)
    while(c['X'-'A']) // 6
    {
        l[6]++;
        FOR(i,vec[6].length())
        {
            c[vec[6][i]-'A']--;
        }
    }
//DI(4)
    while(c['G'-'A']) // 8
    {
        l[8]++;
        FOR(i,vec[8].length())
        {
            c[vec[8][i]-'A']--;
        }
    }
//DI(5)
    while(c['F'-'A']) // 5
    {
        l[5]++;
        FOR(i,vec[5].length())
        {
            c[vec[5][i]-'A']--;
        }
    }
//DI(6)
    while(c['S'-'A']) // 7
    {
        l[7]++;
        FOR(i,vec[7].length())
        {
            c[vec[7][i]-'A']--;
        }
    }
//DI(7)
    while(c['H'-'A']) // 3
    {
        l[3]++;
        FOR(i,vec[3].length())
        {
            c[vec[3][i]-'A']--;
        }
    }
//DI(8)
    while(c['T'-'A']) // 2
    {
        l[2]++;
        FOR(i,vec[2].length())
        {
            c[vec[2][i]-'A']--;
        }
    }
//DI(9)
    while(c['O'-'A']) // 1
    {
        l[1]++;
        FOR(i,vec[1].length())
        {
            c[vec[1][i]-'A']--;
        }
    }
//DI(10)


    while(c['I'-'A']) // 9
    {
        l[9]++;
        FOR(i,vec[9].length())
        {
            c[vec[9][i]-'A']--;
        }
    }
DI(11)
    FOR(i,10)
    {
        while(l[i]--)
        {
            cout << i;
        }
    }

    cout << endl;

}
int main()
{
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        wczytaj();
        DI(t)
        printf("Case #%d: ",t);
        wykonaj();
    }
    return 0;
}
