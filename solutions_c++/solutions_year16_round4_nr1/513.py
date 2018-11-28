#include <stdio.h>
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

string calc(char f, int depth)
{
    if(depth == 0)
    {
        return string("") + f;
    }
    char L = f, R;
    if(f == 'R')
        R = 'S';
    else if(f == 'S')
        R = 'P';
    else if(f == 'P')
        R = 'R';
    string LS = calc(L, depth - 1), RS = calc(R, depth - 1);
    return min(LS+RS, RS+LS);
}


int main()
{
    int T;
    scanf("%d", &T);
    for(int ca = 1; ca <= T; ++ca)
    {
        int N, R, P, S;
        scanf("%d %d %d %d", &N, &R, &P, &S);
        string ret = "Z";
        string r = calc('R', N), s = calc('S', N), p = calc('P', N);
        int NN = (1<<N);
        int r1 = count(r.begin(), r.end(), 'R'), r2 = count(r.begin(), r.end(), 'P'), r3 = count(r.begin(), r.end(), 'S');
        int s1 = count(s.begin(), s.end(), 'R'), s2 = count(s.begin(), s.end(), 'P'), s3 = count(s.begin(), s.end(), 'S');
        int p1 = count(p.begin(), p.end(), 'R'), p2 = count(p.begin(), p.end(), 'P'), p3 = count(p.begin(), p.end(), 'S');
        if(r1 == R && r2 == P && r3 == S) ret = min(ret, r);
        if(s1 == R && s2 == P && s3 == S) ret = min(ret, s);
        if(p1 == R && p2 == P && p3 == S) ret = min(ret, p);
        if(ret == "Z") ret = "IMPOSSIBLE";
        printf("Case #%d: %s\n", ca, ret.c_str());
    }
}
