#include <iostream>
#include <cstring>
#include <cctype>
#include <cmath>
#include <math.h>
#include <algorithm>
#include <vector>
#include <sstream>
#include <cstdio>


using namespace std;

//vector<string > a,b;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("inp.out","w",stdout);
    int n;
    cin >> n;
    for (int i=0;i<n;i++)
    {
        string str;
        cin >> str;
        int z,w,u,x,g,s,v,r,o,n;
        z=count(str.begin(),str.end(),'Z');
        w=count(str.begin(),str.end(),'W');
        u=count(str.begin(),str.end(),'U');
        x=count(str.begin(),str.end(),'X');
        g=count(str.begin(),str.end(),'G');
        s=count(str.begin(),str.end(),'S');
        v=count(str.begin(),str.end(),'V');
        r=count(str.begin(),str.end(),'R');
        o=count(str.begin(),str.end(),'O');
        n=count(str.begin(),str.end(),'N');
        s-=x;
        v-=s;
        r-=(z+u);
        o-=(w+u+z);
        n-=(o+s);


        cout << "Case #" << i+1 << ": " ;
        for (int j=0;j<z;j++)cout << "0";
        for (int j=0;j<o;j++)cout << "1";
        for (int j=0;j<w;j++)cout << "2";
        for (int j=0;j<r;j++)cout << "3";
        for (int j=0;j<u;j++)cout << "4";
        for (int j=0;j<v;j++)cout << "5";
        for (int j=0;j<x;j++)cout << "6";
        for (int j=0;j<s;j++)cout << "7";
        for (int j=0;j<g;j++)cout << "8";
        for (int j=0;j<n/2;j++)cout << "9";
        cout << "\n";


    }
}
