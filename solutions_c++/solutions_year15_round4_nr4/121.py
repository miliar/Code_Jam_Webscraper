#include<algorithm>
#include<cstdio>
#include<iostream>
#include<map>
#include<set>
#include<sstream>
#include<queue>
#include<vector>

using namespace std;

#define forn(i,n) for(int i=0;i<n;i++)
#define all(v) v.begin(),v.end()

int calc(int r, int c)
{
    if(r == 2)
    {
        if(c == 3)
            return 2;
        if(c == 4)
            return 1;
        if(c == 5)
            return 1;
        if(c == 6)
            return 3;
    }
    if(r == 3)
    {
        if(c == 3)
            return 2;
        if(c == 4)
            return 3;
        if(c == 5)
            return 2;
        if(c == 6)
            return 2;
    }
    if(r == 4)
    {
        if(c == 3)
            return 3;
        if(c == 4)
            return 1;
        if(c == 5)
            return 1;
        if(c == 6)
            return 5;
    }
    if(r == 5)
    {
        if(c == 3)
            return 3;
        if(c == 4)
            return 3;
        if(c == 5)
            return 1;
        if(c == 6)
            return 5;
    }
    if(r ==  6)
    {
        if(c == 3)
            return 6;
        if(c == 4)
            return 4;
        if(c == 5)
            return 2;
        if(c == 6)
            return 19;
    }
}

int main()
{
    freopen("D-small.in","r",stdin);
    freopen("D-small.out","w",stdout);
	int casos;
    cin >> casos;
    for(int casito = 1; casito <= casos; casito++)
    {
        int r,c;
        cin >> r >> c;
        cout << "Case #"<<casito<<": "<<calc(r,c) << endl;
    }
}
