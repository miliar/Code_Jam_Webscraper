/*Sarbajit Saha*/

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

int x,r,c;

int game()
{
    if(r>c)
    {
        int temp;
        temp=r;
        r=c;
        c=temp;
    }

    if(r==1)
    {
        if(c==1)
        {
            if(x==1)
                return 1;
            else
                return 0;
        }

        if(c==2)
        {
            if(x==1||x==2)
                return 1;
            else
                return 0;
        }

        if(c==3)
        {
            if(x==1)
                return 1;
            else
                return 0;
        }

        if(c==4)
        {
            if(x==1||x==2)
                return 1;
            else
                return 0;
        }
    }


    if(r==2)
    {
        if(c==2)
        {
            if(x==1||x==2)
                return 1;
            else
                return 0;
        }

        if(c==3)
        {
            if(x==4)
                return 0;
            else
                return 1;
        }

        if(c==4)
        {
            if(x==1||x==2)
                return 1;
            else
                return 0;
        }
    }

    if(r==3)
    {
        if(c==3)
        {
            if(x==1||x==3)
                return 1;
            else
                return 0;
        }

        if(c==4)
        {
                return 1;
        }
    }

    if(r==4)
    {
        if(c==4)
        {
            if(x==3)
                return 0;
            else
                return 1;
        }
    }


}

using namespace std;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        cin>>x>>r>>c;
        int ans=game();
        if(ans==1)
            cout<<"Case #"<<i<<": GABRIEL"<<endl;
        else
            cout<<"Case #"<<i<<": RICHARD"<<endl;
    }
    return 0;
}
