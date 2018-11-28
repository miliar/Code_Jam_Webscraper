#include <cstring>
#include <string>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

#define FOR1(i,n) for(int i=0;i<(n);i++)
#define FOR2(i,n,m)for(int i=n;i<=(m);++i)
#define FORD(i,n,m) for(int i=n;i>=(int)(m);--i)


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
    freopen("A-large.in","rt",stdin);
    freopen("output.out","wt",stdout);
    string c1;
    char ch[4][4];
    int n;
    int T;
    cin>>T;
    FOR1(nn,T)
    {

        FOR1(i,4)
         {
            cin>>c1;
                FOR1(j,4)
                  ch[i][j]=c1[j];
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
