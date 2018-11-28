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
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#define inf 1000*1000*1000
#define f first
#define s second
#define mp make_pair
using namespace std;
bool p;
int n, a[109], b[109][109], ind[109], qq;
string s[109], t[109], d[109];
int sum, mi, ans;
int te;
int main()
{
    ifstream cin("A-small-att.in");
    ofstream cout("A-small-att.out");
    cin>>te;
    while(te--)
    {
        qq++;
        cin>>n;
        for(int i=1;i<=n;i++)
        {
            cin>>s[i];
            for(int j=0;j<s[i].length();j++)
            {
                if(s[i][j]==s[i][j-1])
                {
                    b[i][ind[i]]++;
                    continue;
                }
                ind[i]++;
                t[i][ind[i]]=s[i][j];
                b[i][ind[i]]++;
            }
        }
        cout<<"Case #"<<qq<<": ";
        p = 0;
        for(int i=2;i<=n;i++)
        {
            if(ind[i]!=ind[i-1])
            {
                p=1;
                break;
            }
            for(int j=1;j<=ind[i];j++)
            {
                if(t[i][j] != t[i-1][j])
                {
                    p=1;
                    break;
                }
            }
            if(p == 1)
                break;
        }
        sum = 0, mi = inf, ans = 0;
        //cout<<sum<<" "<<mi<<" "<<ans<<" "<<p<<endl;
        if(p == 1)
        {
            for(int i=0;i<=n;i++)
            {
                for(int j=1;j<=ind[i];j++)
                {
                    b[i][j]=0;
                }
                ind[i]=0;
            }
            cout<<"Fegla Won"<<endl;
            continue;
        }
        for(int j=1;j<=ind[1];j++)
        {
            mi = inf;
            for(int q=1;q<=100;q++)
            {
                sum = 0;
                for(int i=1;i<=n;i++)
                {
                    sum += abs(b[i][j]-q);
                }
                mi = min(mi, sum);
            }
            ans += mi;
        }
        cout<<ans<<endl;
        sum = 0, mi = inf, ans = 0;
        for(int i=0;i<=n;i++)
        {
            for(int j=1;j<=ind[i];j++)
            {
                b[i][j]=0;
            }
            ind[i]=0;
        }
    }
}
