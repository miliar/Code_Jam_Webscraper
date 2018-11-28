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
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <queue>
#include <string>
#define rep(i,n) for(int i=0;i<n;i++)
#define F first
#define S second
#define mp make_pair
#define LL long long
#define pb push_back
using namespace std;
#define sz 300005
#define inf 0x7fffffff

char nxt(char i,char j)
{
    if(i=='1')return j;
    if(i=='i' && j=='j')return 'k';
    if(i=='j' && j=='k')return 'i';
    if(i=='k' && j=='i')return 'j';
    swap(i,j);
    if(i=='1')return j;
    if(i=='i' && j=='j')return 'k';
    if(i=='j' && j=='k')return 'i';
    if(i=='k' && j=='i')return 'j';
    return '1';
}
int nxp(char i,char j)
{
    if(i==j && i=='1')return 1;
    if(i==j)return -1;
    if(i=='i' && j=='k')return -1;
    if(i=='j' && j=='i')return -1;
    if(i=='k' && j=='j')return -1;
    return 1;
}

int main()
{
    freopen("C-small-attempt3.in","r",stdin);
    freopen("C-small-attempt3.out","w",stdout);

    int T;
    cin>>T;
    rep(cas,T)
    {
        int n,r;
        string str;
        cin>>n >>r;
        cin>>str;
        string s = "";
        rep(i,r)
            s+=str;
        char pre = '1';
        int pz = 1;

        //cout << s <<endl;
        rep(i,s.size())
        {

            pz *= nxp(pre, s[i]);
            pre = nxt(pre, s[i]);
            //cout << pz << " " << pre << endl;
        }
        int flag = false;
        //cout << pre << " " << pz <<endl;
        if(pre == '1' && pz == -1)
        {
            int f1 = -1;
            int f2 = -1;
            pre = '1';
            pz = 1;
            rep(i,s.size())
            {
                pz *= nxp(pre, s[i]);
                pre = nxt(pre, s[i]);
                if(pre=='i' && pz==1)
                {
                    f1 = i;
                    break;
                }
            }
            pre = '1';
            pz = 1;
            for (int i=s.size()-1;i>=0;i--)
            {
                pz *= nxp(s[i], pre);
                pre = nxt(s[i], pre);
                if(pre=='k' && pz==1)
                {
                    f2 = i;
                    break;
                }
            }
            //cout << f1 << " " << f2 <<endl;

            if(f1!=-1 && f2!=-1 && f2 - f1 >= 2)flag = true;
        }
        cout << "Case #" << cas+1 <<": "<< (flag?"YES":"NO") <<endl;
    }
}
/*
100
3 1
ijk
*/
