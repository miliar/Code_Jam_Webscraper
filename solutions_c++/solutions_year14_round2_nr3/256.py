#include <fstream>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <algorithm>
#include <cmath>
#include <string>
#include <sstream>
#include <stack>
using namespace std;

ifstream fin("in.txt");
ofstream fout("out.txt");

int n,m;
string v[1000];
string ans;
bool a[10][10];
int k[10];

bool check()
{
    int i;
    stack<int> s;
    s.push(k[0]);
    for(i=1; i<n; ++i)
    {
        while(!s.empty())
        {
            if(a[s.top()][k[i]])
                break;

            s.pop();
        }

        if(s.empty())
            return false;

        s.push(k[i]);
    }
    return true;
}

int main()
{
    int t,tt,i,j;
    fin>>tt;
    for(t=1; t<=tt; ++t)
    {
        fin>>n>>m;
        ans = "";
        for(i=0; i<n; ++i)
        {
            k[i]=i;
            v[i]="";
            for(j=0; j<n; ++j)
                a[i][j] = false;
        }
        for(i=0; i<n; ++i)
            fin>>v[i];
        for(i=0;i<m; ++i)
        {
            int p,q;
            fin>>p>>q;
            p--;
            q--;
            a[p][q] = true;
            a[q][p] = true;
        }
        while(1)
        {
            if(check())
            {
                string newans="";
                for(i=0;i<n;++i)
                    newans += v[k[i]];

                if(ans == "" || ans > newans)
                    ans = newans;
            }

            if(!next_permutation(k,k+n))
                break;
        }
        fout << "Case #" << t <<": " << ans << endl;
    }
    return 0;
}
