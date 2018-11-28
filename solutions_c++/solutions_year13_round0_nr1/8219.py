/*************************************
******** Team : BUBT_HIDDEN **********
**************************************
*********** Shipu Ahamed *************
*************************************/

#include<algorithm>
#include<iostream>
#include<iterator>
#include<cassert>
#include<sstream>
#include<fstream>
#include<cstdlib>
#include<cstring>
#include<utility>
#include<complex>
#include<string>
#include<cctype>
#include<cstdio>
#include<vector>
#include<bitset>
#include<stack>
#include<queue>
#include<cmath>
#include<deque>
#include<list>
#include<set>
#include<map>

#define ll long long
#define sc scanf
#define pf printf
#define pi 2*acos(0.0)

#define ft first
#define se second
#define st(s) s.size();
#define intput freopen("in.txt","r",stdin)
#define output freopen("out.txt","w",stdout)
#define maxall(v) *max_element(v.begin(),v.end())
#define minall(v) *min_element(v.begin(),v.end())
#define Sort(v) sort(v.begin(),v.end())
#define un(v) Sort(v), v.erase(unique(v.begin(),v.end()),v.end())
#define cover(a,d) memset(a,d,sizeof(a))
using namespace std;
int main()
{
//    intput;
//    output;
    int t,no=0;
    cin>>t;
    while(t--)
    {
        string s[1000];
        map<char,int>mp;
        for(int i=0;i<4;i++)
        {
            cin>>s[i];
        }
        int dot=0,x=0,o=0,T=0,f=0;
        for(int j=0;j<4;j++)
        {
           for(int i=0;i<4;i++)
           {
               if(s[i][j]=='X')
                x++;
               else if(s[i][j]=='O')
                o++;
               else if(s[i][j]=='.')
                dot++;
                else if(s[i][j]=='T'){
                  if(x==3)
                  x++;
                  else if(o==3)
                  o++;
                }
           }
            if(x==4)
            {
                pf("Case #%d: X won\n",++no);
                f=1;
               break;
            }
            else if(o==4)
            {
                pf("Case #%d: O won\n",++no);
                f=1;
                break;
            }
            else
            {
                x=0,o=0,dot=0;
            }
        }
        if(f==1)
        {
            continue;
        }

        for(int i=0;i<4;i++)
        {
           for(int j=0;j<4;j++)
           {
               if(s[i][j]=='X')
                x++;
               else if(s[i][j]=='O')
                o++;
               else if(s[i][j]=='.')
                dot++;
                else if(s[i][j]=='T'){
                  if(x==3)
                  x++;
                  else if(o==3)
                  o++;
                }
           }
            if(x==4)
            {
                pf("Case #%d: X won\n",++no);
                f=1;
               break;
            }
            else if(o==4)
            {
                pf("Case #%d: O won\n",++no);
                f=1;
                break;
            }
            else
            {
                x=0,o=0,dot=0;
            }
        }
        if(f==1)
        {
            continue;
        }

        for(int i=0;i<4;i++)
        {
            if(s[i][i]=='X')
            x++;
            else if(s[i][i]=='O')
            o++;
            else if(s[i][i]=='.')
            dot++;
            else if(s[i][i]=='T'){
                if(x==3)
                x++;
                else if(o==3)
                o++;
            }
        }

            if(x==4)
            {
                pf("Case #%d: X won\n",++no);
                f=1;
               continue;
            }
            else if(o==4)
            {
                pf("Case #%d: O won\n",++no);
                f=1;
                continue;
            }
        x=0,o=0,dot=0;
        int p=0;
        for(int i=3;i>=0;i--,p++)
        {
               if(s[p][i]=='X')
                x++;
               else if(s[p][i]=='O')
                o++;
               else if(s[p][i]=='.')
                dot++;
                else if(s[p][i]=='T'){
                  if(x==3)
                  x++;
                  else if(o==3)
                  o++;
                }
        }
        if(x==4)
        {
            pf("Case #%d: X won\n",++no);
            f=1;
            continue;
        }
        else if(o==4)
        {
                pf("Case #%d: O won\n",++no);
                f=1;
                continue;
        }
        if(f!=1)
        {
           for(int i=0;i<4;i++)
           {
               for(int j=0;j<4;j++)
               mp[s[i][j]]++;
            }
            if(mp['X']==7 && mp['O']==8 || mp['X']==8 && mp['O']==8)
            {
                pf("Case #%d: Draw\n",++no);
            }
            else if(mp['X']==8 && mp['O']==7)
            {
                pf("Case #%d: Draw\n",++no);
            }
            else
            {
                pf("Case #%d: Game has not completed\n",++no);
            }

        }

    }

    return 0;
}

