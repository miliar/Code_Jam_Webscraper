#include <iostream>
#include <vector>
#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>
#include <utility>
#include <stack>
#include <sstream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <deque>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <stdlib.h>
#include <stdint.h>
#include <unistd.h>

using namespace std;

#define FOR(i,a,b)				for (i=a;i<b;i++)
#define s(n)					scanf("%d",&n)
#define p(n)					printf("%d\n",n)
#define sd(n)					int n;scanf("%d",&n)
#define pb(n)                                   push_back(n)
#define clr(a)                                  memset(a,0,sizeof(a))
#define all(c)                                  (c).begin(),(c).end()
#define PI 3.14159265
#define mod 747474747
#define MAX 6666

typedef vector <int> vi;
typedef vector <vi> vvi;
typedef vector <string> vstr;
typedef long long ll;
int i,j,k;

int mulmod(int a,int b,int MOD)
{
	ll t=(ll)a*b;
	if (t>=MOD) t=t%MOD;
	return t;
}

int addmod(int a,int b,int MOD)
{
	ll t=(ll)a+(ll)b;
	if (t>=MOD) t=t%MOD;
	return t;
}

int main()
{
    
    int T=1;
    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    //T = g_fi.ReadNext();
    cin>>T;
    FOR(k,0,T)
    {
        bool win=false;
        bool inc=false;
        char bd[4][4];
        string str;
        FOR(i,0,4)
        {
            cin>>str;
            FOR(j,0,4)
            {
                    bd[i][j]=str[j];
                    if(bd[i][j]=='.')
                        inc=true;
            }            
        }
        FOR(i,0,4)
        {
            int xs = 0;
            int os = 0;
            char ch;
            FOR(j,0,4)
            {
                ch = bd[i][j];
                if(ch=='X')
                    xs++;
                else if(ch=='O')
                    os++;
                else if(ch=='T')
                {
                    xs++;
                    os++;
                }
            }
            if(xs==4)
            {
                win=true;
                cout<<"Case #"<<k+1<<": X won"<<endl;
                break;
            }
            else if(os==4)
            {
                win=true;
                cout<<"Case #"<<k+1<<": O won"<<endl;
                break;
            }            
        }
        if(win)
            continue;
        FOR(j,0,4)
        {
            int xs = 0;
            int os = 0;
            char ch;
            FOR(i,0,4)
            {
                ch=bd[i][j];
                if(ch=='X')
                    xs++;
                else if(ch=='O')
                    os++;
                else if(ch=='T')
                {
                    xs++;
                    os++;
                }
            }
            if(xs==4)
            {
                win=true;
                cout<<"Case #"<<k+1<<": X won"<<endl;
                break;
            }
            else if(os==4)
            {
                win=true;
                cout<<"Case #"<<k+1<<": O won"<<endl;
                break;
            }            
        }
        if(win)
            continue;
        
        int xs = 0;
        int os = 0;
        char ch;
        FOR(i,0,4)
        {
            char ch = bd[i][i];
            if(ch=='T')
            {
                xs++;
                os++;
            }
            else if(ch=='X')
                xs++;
            else if(ch=='O')
                os++;
        }
        if(xs==4)
        {
            win=true;
            cout<<"Case #"<<k+1<<": X won"<<endl;
        }
        else if(os==4)
        {
            win=true;
            cout<<"Case #"<<k+1<<": O won"<<endl;
        } 
        if(win)
            continue;
        xs=0;
        os=0;
        FOR(i,0,4)
        {
            char ch = bd[i][3-i];
            if(ch=='T')
            {
                xs++;
                os++;
            }
            else if(ch=='X')
                xs++;
            else if(ch=='O')
                os++;
        }
        if(xs==4)
        {
            win=true;
            cout<<"Case #"<<k+1<<": X won"<<endl;
        }
        else if(os==4)
        {
            win=true;
            cout<<"Case #"<<k+1<<": O won"<<endl;
        } 
        if(win)
            continue;
        if(inc)
        {
            cout<<"Case #"<<k+1<<": Game has not completed"<<endl;
        }
        else
            cout<<"Case #"<<k+1<<": Draw"<<endl;
    }
    return 0;
}