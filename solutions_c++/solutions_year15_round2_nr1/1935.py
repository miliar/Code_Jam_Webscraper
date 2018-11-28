#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

ifstream in("in.txt");
ofstream out("out.txt");

const int maxN = 1000001;

int maxx = 0;
vector <int> v(maxN, 9*maxN);

vector <int> q;

int reverseNum(int x)
{
    int ret = 0;
    for(; x;ret *= 10, ret += x % 10, x /= 10);
    return ret;
}

void read()
{
    int t;
    int x;
    in >> t;
    for(int i = 1; i <= t; i++)
    {
        in >> x;
        maxx = max(x, maxx);
        q.push_back(x);
    }
}

void countUpTo(int x)
{
    int rev;
    v[1] = 1;
    for(int i = 1; i < x; i++)
    {
        rev = reverseNum(i);
        v[rev] = min(v[rev], v[i]+1);
        v[i+1] = min(v[i+1], v[i] + 1);
    }
}

int roundTo(int x)
{
    if(x == 0) return 9;
    int ret = 0;
    while(x)
    {
        ret *= 10;
        ret+= 9;
        x/=10;
    }
    return ret;
}

int main()
{
    read();
    countUpTo(maxN);
    for(int i = 1; i <= q.size(); i++)
    {
        out << "Case #" << i << ": ";
        out << v[q[i-1]] << endl;
    }
    return 0;
}
