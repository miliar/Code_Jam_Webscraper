#include <cstring>
#include <string>
#include <string.h>
#include <map>
#include <deque>
#include <iterator>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <list>

using namespace std;

#define FST first
#define SND second
#define MP make_pair
#define PB push_back

typedef long long LL;
typedef long double LD;

typedef stringstream SS;
typedef pair<long,int> PLI;
typedef pair<int ,int> PII;
typedef vector<PLI> VPLI;
typedef vector<string> VS;
typedef vector<int> VI;
typedef vector<string> VVS;
typedef vector<double> VD;

#define ALL(x) (x).begin(),(x).end()
#define FOR1(i,n) for(int i=0;i<(n);i++)
#define FOR2(i,n,m)for(int i=n;i<=(m);++i)
#define FORD(i,n,m) for(int i=n;i>=(int)(m);--i)
#define FORI(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define SIZE(a) ((int)((a).size()))

bool check(char c[4][4],char c1,int p)
{
    int pos=0,cnt=0,flag=1;
   FOR1(i,4)
    {
        if(p==0)
        {
             FOR1(j,4)
                if (c[j][i]==c1 || c[j][i]=='T')
                cnt++;
        }
        else if(p==1)
        {
            FOR1(j,4)
            {
                if (c[i][j]==c1 || c[i][j]=='T')
                cnt++;
            }
        }
        else if(p==2)
        {
            FOR1(j,4)
            {
             if (c[j][j]==c1 || c[j][j]=='T')
                cnt++;
            }
            if(cnt<4)
            {
                cnt=0;
                FORD(j,3,0)
                {
                    if (c[pos][j]==c1 || c[pos][j]=='T')
                    cnt++;
                    pos++;
                }
            }
            }

     else
     {
         FOR1(j,4)
         {
             if (c[i][j]==c1)
                {
                 flag=0;
                 break;
                }
         }
     }

        if (cnt==4 || flag==0)
            flag=0;
        else
            cnt=0;
    }

    if (flag==0)
        return true;
    else
        return false;
}

int main()
{
    freopen("input.in","rt",stdin);
    freopen("output.out","wt",stdout);
    string s1;
    char ch[4][4];
    int N;
    cin>>N;
    FOR1(nn,N)
    {

        FOR1(i,4)
         {
            cin>>s1;
                FOR1(j,4)
                  ch[i][j]=s1[j];
         }

            if ((check(ch,'X',0) || check(ch,'X',1) || check(ch,'X',2)))
                cout<<"Case #"<<nn+1<<": "<<"X won "<<endl;
            else if ((check(ch,'O',0)) || (check(ch,'O',1)) || (check(ch,'O',2)))
                cout<<"Case #"<<nn+1<<": "<<"O won "<<endl;
            else
            {
                if (check(ch,'.',3))
                cout<<"Case #"<<nn+1<<": "<<"Game has not completed "<<endl;
                else
                cout<<"Case #"<<nn+1<<": "<<"Draw "<<endl;
            }

    }

}
