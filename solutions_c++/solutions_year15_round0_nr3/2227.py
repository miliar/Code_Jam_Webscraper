#include <iostream>
#include <vector>
#include <set>
#include <queue>
#include <algorithm>
#include <string>
#include <fstream>
#include <cctype>
#include <iomanip>
#include <cmath>
#include <cstring>
#include <map>
#include <bitset>
#include <stack>
/*  //c++11
#include <unordered_map>
#include <unordered_set>
#include <tuple>
*/

using namespace std;

ifstream fin("1.in");
ofstream fout("1.out");

char R[4]={'1','i','j','k'};

int getIndex(char c)
{
    for(int i = 0; i < 4; i++)
        if(c == R[i])
            return i;
    return -1;
}

pair<int, int> multiplication(pair<int, int> a, pair<int, int> b)
{
    int sign = a.first * b.first;
    if(a.second == 0)
    {
        return make_pair(sign, b.second);
    }
    if(b.second == 0)
    {
        return make_pair(sign, a.second);
    }
    if(a.second == b.second)
    {
        return make_pair(-sign, 0);
    }

    if(a.second == 1)
    {
        if(b.second == 2)
            return make_pair(sign, 3);
        if(b.second == 3)
            return make_pair(-sign, 2);
    }
    if(a.second == 2)
    {
        if(b.second == 1)
            return make_pair(-sign, 3);
        if(b.second == 3)
            return make_pair(sign, 1);
    }
    if(a.second == 3)
    {
        if(b.second == 1)
            return make_pair(sign, 2);
        if(b.second == 2)
            return make_pair(-sign, 1);
    }

}

string s, bigS;
void solve()
{
    int L;
    long long X;
    fin>>L>>X;

    fin>>s;
    if(L*X < 3)
    {
        fout<<"NO";
        return;
    }
    X = min(X, 20  + X%4);
    bigS = "";
    pair<int, int> A = make_pair(1,0);
    for(int i = 0; i < s.size(); i++)
    {
        pair<int, int> e = make_pair(1, getIndex(s[i]));
        A = multiplication(A, e);
    }
    pair<int, int> B = make_pair(1,0);
    for(int i = 1; i <= X; i++)
    {
        B = multiplication(B, A);
        bigS += s;
    }
    s = bigS;
    if(B != make_pair(-1,0))
    {
        fout<<"NO";
        return;
    }
    B = make_pair(1,0);
    int st = L*X, dr = 0;
    for(int i = 0; i < s.size(); i++)
    {
        pair<int, int> e = make_pair(1, getIndex(s[i]));
        B = multiplication(B,e);
        if(B == make_pair(1,1))
        {
            st = i;
            i = s.size() + 5;
        }
    }
    B = make_pair(1,0);
    for(int i = s.size() - 1; i >= 0; i--)
    {
        pair<int, int> e = make_pair(1, getIndex(s[i]));
        B = multiplication(e,B);
        if(B == make_pair(1,3))
        {
            dr = i;
            i = 0;
        }
    }
    if(st < dr - 1)
    {
        fout<<"YES";
        return;
    }
    fout<<"NO";
    return ;
}



int main()
{
    //freopen("1.in","r",stdin);
    //freopen("1.out","w",stdout);
    int T;
    fin>>T;
    for(int i = 1; i <= T; i++)
    {
        fout<<"Case #"<<i<<": ";
        solve();
        fout<<'\n';
    }


    return 0;
}


//FILE!!!
