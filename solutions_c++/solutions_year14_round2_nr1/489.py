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
using namespace std;

ifstream fin("in.txt");
ofstream fout("out.txt");

int n;
string a[105];
int idx[105];
int cnt[105];

bool checkAll()
{
    int i;
    for(i=1; i<n; ++i)
        if(a[i][idx[i]] != a[0][idx[0]])
            return false;
    return true;
}

void counts()
{
    int i,j;
    for(i=0; i<n; ++i)
    {
        for(j=idx[i]+1; j<a[i].length(); ++j)
            if(a[i][j] != a[i][idx[i]])
                break;
        cnt[i] = j - idx[i];
        idx[i] = j;
    }
}

int avg()
{
    int i, ans = 0;
    sort(cnt, cnt+n);
    int l = cnt[n/2];
    for(i=0; i<n; ++i)
        ans += abs(l-cnt[i]);
    return ans;
}

int solve()
{
    int ans = 0;
    while(1)
    {
        if(!checkAll())
            return -1;
        
        if(a[0][idx[0]] == '#')
            break;
        
        counts();
        ans += avg();
    }
    return ans;
}

int main()
{
    int t,i,j,tt, ans;
    fin>>tt;
    for(t=1; t<=tt; ++t)
    {
        fin>>n;
        for(i=0; i<n; ++i)
        {
            fin>>a[i];
            idx[i]=0;
            a[i]+='#';
            a[i]+='-';
        }
        ans = solve();
        fout << "Case #" << t << ": ";
        if(ans == -1)
        {
            fout << "Fegla Won";
        }
        else 
            fout << ans;
        fout << endl;
    }
    return 0;
}
