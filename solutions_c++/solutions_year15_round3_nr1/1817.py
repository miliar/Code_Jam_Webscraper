#include <bits/stdc++.h>

using namespace std;
//#define in cin
//#define out cout
int main()
{
    fstream in("A-small-attempt4.in" , ios::in);
    fstream out("out.out" , ios::out);
    int t; in >> t;
    for(int i = 0; i < t; i ++)
    {
        int r , c , w;
        in >> r >> c >> w;
        out << "Case #" << i+1 << ": " << (c/w + (w-1) + (c%w||0))*r<< '\n';
    }
}
