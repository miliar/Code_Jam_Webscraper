#include <string>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <bitset>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <fstream>
#include <math.h>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <valarray>
#include <memory.h>
#include <sstream>
#include <string>
using namespace std;

#define all(n) (n).begin(),(n).end()
#define rall(n) (n).rbegin(),(n).rend()
#define mp make_pair
#define pb push_back
#define sz size()
#define F first
#define S second
#define FO(i,x) for(int i=0;i<x;i++)
#define FOR(i,s,e) for(int i = int(s); i < int(e); i++)

#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)
char arr[4][4];
bool win(char k)
{
     FO(i,4) { bool c=1; FO(j,4) if(arr[i][j]!=c||arr[i][j]!='T') c=0; }
     for(int i=0;i<4;i++) 
     {
          bool c=1;
          for(int j=0;j<4 && c;j++)
               if(arr[i][j]!=k&&arr[i][j]!='T') c=0; 
          
          if(c) return 1; 
          
          c=1;
          for(int j=0;j<4 && c;j++) 
               if(arr[j][i]!=k&&arr[j][i]!='T') c=0;
          
          if(c) return 1;       
     }
     if( (arr[0][0]=='T'||arr[0][0]==k) && 
         (arr[1][1]=='T'||arr[1][1]==k) &&
         (arr[2][2]=='T'||arr[2][2]==k) &&
         (arr[3][3]=='T'||arr[3][3]==k) ) return 1;
         
     if( (arr[0][3]=='T'||arr[0][3]==k) && 
         (arr[1][2]=='T'||arr[1][2]==k) &&
         (arr[2][1]=='T'||arr[2][1]==k) &&
         (arr[3][0]=='T'||arr[3][0]==k) ) return 1;
             
     return 0;    
}
int main()
{
   READ("A-large.in");
   WRITE("A-large.out");
   int t,a=1;
   cin>>t;
   while(t--)
   {
          bool X=0,O=0,N=0;   
          FO(i,4)FO(j,4) 
          {
              cin>>arr[i][j];
              if(arr[i][j]=='.') N=1;
          }
          if(win('X')) X=1;
          if(win('O')) O=1;
          
          if(X&&O)   cout<<"Case #"<<a<<": Draw"<<endl;
          else if(X) cout<<"Case #"<<a<<": X won"<<endl;
          else if(O) cout<<"Case #"<<a<<": O won"<<endl;
          else if(N) cout<<"Case #"<<a<<": Game has not completed"<<endl;
          else       cout<<"Case #"<<a<<": Draw"<<endl;
          a++;
   }
   
   return 0;    
}

