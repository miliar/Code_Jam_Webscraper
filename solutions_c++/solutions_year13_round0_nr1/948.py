#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

bool isGood(char c, vector<string> v)
{
    for(int i=0;i<v.size();i++)
    {
        for(int j=0;j<v[i].size();j++)
        {
            if(v[i][j]=='T')
                v[i][j]=c;
        }
    }
    for(int i=0;i<v.size();i++)
    {
        bool flag = true;
        for(int j=0;j<v[i].size();j++)
        {
           if(v[i][j]!=c)
           {
              flag = false; 
              break;
           }
        }
        if(flag)
            return true;
    }
    for(int i=0;i<v[0].size();i++)
    {
        bool flag = true;
        for(int j=0;j<v.size();j++)
        {
           if(v[j][i]!=c)
           {
              flag = false; 
             break;
           }
        }
        if(flag)
            return true;
    }
    bool flag = true;
    for(int i=0;i<4;i++)
    {
        if(v[i][i]!=c)
            flag = false;
    }
    if(flag)
        return true;
    flag = true;
    for(int i=0;i<4;i++)
    {
        if(v[i][3-i]!=c)
            flag = false;
    }
    if(flag)
        return true;
    return false;
}
bool hasEmpty(vector<string> v)
{
    for(int i=0;i<v.size();i++)
    {
        for(int j=0;j<v[i].size();j++)
        {
            if(v[i][j]=='.')
                return true;
        }
    }
    return false;
}

int main()
{
    int T;
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        cout<<"Case #"<<t<<": ";
        vector<string> v;
        string s;
        for(int i=0;i<4;i++)
        {
            cin>>s;
            v.push_back(s);
        }

        if(isGood('X', v))
        {
            cout<<"X won"<<endl;
        }else if(isGood('O', v))
        {
            cout<<"O won"<<endl;
        }else if(hasEmpty(v))
        {
            cout<<"Game has not completed"<<endl;
        }else
        {
            cout<<"Draw"<<endl;
        }
    }

    return 0;
}
