#include <bits/stdc++.h>
/*#include <boost/multiprecision/cpp_int.hpp> */
#define ll long long
#define pb push_back
#define mp make_pair
#define mod 1000000007
#define gc getchar_unlocked
#define pp pair<int,int>
#define bigint boost::multiprecision::cpp_int
#define PLIM 68000000
using namespace std;


string s[500];



int T,R,C;


bool dfs(int r,int c,int d)
{
    if(r<1 || r>R || c<1 || c>C)return false;

//if(r==3 && c==2)cout<<"here\n";
    if(s[r][c-1]=='.')
    {
        if(d==1)return dfs(r-1,c,1);
        else if(d==2)return dfs(r,c+1,2);
        else if(d==3)return dfs(r+1,c,3);
        else if(d==4)return dfs(r,c-1,4);
    }

   return true;

}

int main()
{
    cin>>T;
    int cas=1;
    while(T--)
    {
        cin>>R>>C;


        for(int i=1;i<=R;i++)cin>>s[i];

         int ans=0;
      /*
        for(int i=1;i<=C;i++)
        {
            if(s[1][i-1]=='^' ){ ans++; s[1][i-1]='v';}
            if(s[R][i-1]=='v'){ ans++; s[R][i-1]='^'; }
        }

        for(int i=1;i<=R;i++)
        {
            if(s[i][0]=='<'){ ans++; s[i][0]='>'; }
            if(s[i][C-1]=='>'){ ans++; s[i][C-1]='<'; }
        }
     */

        bool f=true;

        for(int i=1;i<=R;i++)
        {
            for(int j=1;j<=C;j++)
            {
                /*
                if(i==1)
                {
                if(s[i][j-1]=='^'){ f=false; break; }
                }
                else if(i==R)
                {
                if(s[i][j-1]=='v'){ f=false; break; }
                }
                else if(j==1)
                {
                if(s[i][j-1]=='<'){ f=false; break; }
                }
                else if(j==C)
                {
                if(s[i][j-1]=='>'){ f=false; break; }
                }
                */
                if(s[i][j-1]!='.')
                {
                    if(s[i][j-1]=='^' && !dfs(i-1,j,1))ans++;
                    else if(s[i][j-1]=='>' && !dfs(i,j+1,2))ans++;
                    else if(s[i][j-1]=='v' && !dfs(i+1,j,3))ans++;
                    else if(s[i][j-1]=='<' && !dfs(i,j-1,4))ans++;

                    if(!(dfs(i-1,j,1) | dfs(i,j+1,2) | dfs(i+1,j,3) | dfs(i,j-1,4) ))
                    {
                        f=false;
                        break;
                    }
                }
            }

            if(!f)break;
        }

        if(!f)
        {
            printf("Case #%d: IMPOSSIBLE\n",cas++);
            continue;
        }


        printf("Case #%d: %d\n",cas++,ans);
    }


return 0;
}
