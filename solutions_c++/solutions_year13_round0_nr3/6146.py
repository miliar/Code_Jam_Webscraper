#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <set>
#include <string>
#include <cmath>
#include <stdio.h>
#include <map>
#include <stack>
#include <fstream>
#define SZ(a) (int)a.size()
#define SS stringstream
#define all(a) (a).begin(),(a).end()
#define rll(a) (a).rbegin(),(a).rend()
#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)

using namespace std;

int main()
{
    READ("C-small-attempt0.in");
    WRITE("C-small-attempt0.out");

int T,a,b;
float sqr;
cin >> T;
for (int i = 0;i < T;i ++){
    cin >> a >> b;
    int ctr = 0;
    for (int z = a; z <= b;z ++){
        sqr = sqrt((double)z);
        string one,two,three,four;
        SS s;
        s << z;
        s >> one;
        s.clear();
        s << sqr;
        s >> two;
        three = one;
        four = two;
        reverse(all(one));reverse (all(two));
        if (one == three && two == four)ctr ++;

    }
    cout <<"Case #"<<i + 1<<": "<<ctr<<endl;
}
    return 0;
}
