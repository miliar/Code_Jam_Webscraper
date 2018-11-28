#include<cstdio>
#include<vector>
#include<cmath>
#include<string>
#include<cstring>
#include<algorithm>
#include<queue>
#include<set>
#include<stack>
#include<map>
#include<sstream>
#include<bitset>
#include<deque>
#include<utility>
#include<cstdlib>
#include<iomanip>
#include<cctype>
#include<climits>
#include<iostream>
using namespace std;
#define ll             long long
#define ull            unsigned long long
#define all(x)         x.begin(),x.end()
#define vi             vector<int>
#define vvi            vector<vector<int> >
#define gcd            ll gcd(ll a,ll b){return b?gcd(b,a%b):a;}
#define INF            2147483647
#define LIMIT          1000
#define mod            1000000007
#define pi             pair<int,int>
#define mp             make_pair
#define pb(v)          v.push_back
#define sz(x)          x.size()

string tostr(ll x)
{ stringstream ss; ss << x; return ss.str(); }
ll toint(string &s)   
{ stringstream ss; ss << s; long long x; ss >> x; return x; }

    string grid[4];
int ondiag(int i,int j)
{
     if(i>=4 ||i<0) return 2;
     if(j>=4||j<0) return 2;
     if(i==j) return 0;
     else if(i+j==3) return 1;
     else
     return 2; 
}
char dot='O',cross='X';
int checkrow(int i)
{
      int dots=0,crosses=0,tts=0;
      for(int j=0;j<4;j++)  
      {
            if(grid[i][j]=='O') dots++;
            
            else if(grid[i][j]=='X')   crosses++;
            else if(grid[i][j]=='T')   tts++;
      }
      //cout<<grid[i]<<endl;
      //cout<<"row"<<i<<" "<<dots<<" "<<crosses<<" "<<tts<<endl;
      if(dots==4)
      return 2;
      else if(crosses==4)
      return 1;
      else if(dots==3 && tts==1) 
      {
         return 2;
      }
      else if(crosses==3 and tts==1)
      {
         return 1;
      }
      else
      return 3;
    
}
int checkcol(int i)
{
        int dots=0,crosses=0,tts=0;
      for(int j=0;j<4;j++)  
      {
            if(grid[j][i]=='O') dots++;
            else if(grid[j][i]=='X') crosses++;
            else if(grid[j][i]=='T') tts++;
      }
      if(dots==4)
      return 2;
      else if(crosses==4)
      return 1;
      else if(dots==3 && tts==1) 
      {
         return 2;
      }
      else if(crosses==3 and tts==1)
      {
         return 1;
      }
      else
      return 3;
     
}
int checkdg1()
{
    int dots=0,crosses=0,tts=0;
    for(int j=0,i=0;j<4;i++,j++) 
    
    {
              if(grid[i][j]=='O') dots++;
            else if(grid[i][j]=='X') crosses++;
            else if(grid[i][j]=='T') tts++;
    }   
     if(dots==4)
      return 2;
      else if(crosses==4)
      return 1;
      else if(dots==3 && tts==1) 
      {
         return 2;
      }
      else if(crosses==3 and tts==1)
      {
         return 1;
      }
      else
      return 3;
}
int checkdg2()
{
    int dots=0,crosses=0,tts=0;
    for(int j=3,i=0;i<4;i++,j--) 
    {
      //cout<<i<<j<<endl;
              if(grid[i][j]=='O') dots++;
            else if(grid[i][j]=='X') crosses++;
            else if(grid[i][j]=='T') tts++;
    }   
     if(dots==4)
      return 2;
      else if(crosses==4)
      return 1;
      else if(dots==3 && tts==1) 
      {
         return 2;
      }
      else if(crosses==3 and tts==1)
      {
         return 1;
      }
      else
      return 3;
}
int countspace()
{
   int c=0;
  for(int i=0;i<4;i++)
  for(int j=0;j<4;j++)
  {
       if(grid[i][j]=='.')  c++;
  }
  return c;
}
int main()

{
     
    #ifndef ONLINE_JUDGE
     freopen("gcj1.in","r",stdin);
     freopen("gcj2.out","w",stdout);
    #endif
   int t;
   scanf("%d",&t);
   
   for(int test=1;test<=t;test++)
   {
    
        for(int i=0;i<4;i++) cin>>grid[i];
        int ans=0;
        for(int i=0;i<4;i++)
        {
              int a=checkrow(i);
              int b=checkcol(i);
             if(a==1 || a==2) ans=a;
             if(b==1 || b==2) ans=b;
            // cout<<"a"<<a<<"b"<<b<<endl;
            
        }
        int a=checkdg1();
        int b=checkdg2();
        if(a==1 || a==2) ans=a;
        if(b==1 || b==2) ans=b;
        if(!ans && countspace()!=0)
        {
            ans=3;
        }
        else if(!ans)
        { 
            ans=4;
        }
        cout<<"Case #"<<test<<": ";
        if(ans==1)
        {
               cout<<"X won";
        }
        else if(ans==2)
        {
             cout<<"O won";
        }
        else if(ans==3)
        {
            cout<<"Game has not completed";
        }
        else if(ans==4)
        {
             cout<<"Draw";
        }
        cout<<endl;
   }
    return 0;
}
