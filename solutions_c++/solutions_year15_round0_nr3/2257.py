#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

#define in cin
#define out cout
#define abs(a) ( (a)>0?(a):(-(a)) )
#define sign(a) ( (a)>0?(1):(-1) )
#define minn(a,b) (((a)>(b)?(b):(a)))

enum
{
    P1=1, Pi=2, Pj=3, Pk=4
};

int m[5][5] = { 0,  0,  0,  0,  0,
                0,  P1, Pi, Pj, Pk,
                0,  Pi,-P1, Pk,-Pj,
                0,  Pj,-Pk,-P1, Pi,
                0,  Pk, Pj,-Pi,-P1
                };
int c2n[999];
char n2c[99];

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

c2n['i'] = 2;
c2n['j'] = 3;
c2n['k'] = 4;

n2c[1] = '1';
n2c[2] = 'i';
n2c[3] = 'j';
n2c[4] = 'k';


    int tc; in >> tc;
    for(int tci=1; tci<=tc; tci++)
    {
        long long len, rep; in >> len >> rep;
        string tstr; in >> tstr;
        string str = "";

        if(rep > 8LL) {rep %= 8; rep += 8LL;}
        for(int i=0; i<rep; i++) str += tstr;

        int cur = P1;
        int flag = 0;

        for(int i=0; i<str.length(); i++)
        {
            cur = m[abs(cur)][c2n[str[i]]]*sign(cur);
            //out << sign(cur) << n2c[abs(cur)] << endl;

            if(flag == 0 && cur == Pi) flag++;
            else if(flag == 1 && cur == Pk) flag++;
            else if(flag == 2 && cur == -P1) flag++;
        }

        if(flag == 3 && cur == -P1)
            out << "Case #" << tci << ": " << "YES" << endl;
        else
            out << "Case #" << tci << ": " << "NO" << endl;
    }


    return 0;
}
