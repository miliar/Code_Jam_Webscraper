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
#include <string>

using namespace std;

typedef long long LL;

void Solve(void)
{
     int i,j,k;
     int ii,jj;
     int R,C;
     int ret=0;
     cin>>R>>C;
     char **A=new char*[R];
     for(i=0;i<R;i++)
     {
     *(A+i)=new char[C];
     }
     for(i=0;i<R;i++)
     {
      for(j=0;j<C;j++)
      {
       cin>>A[i][j];
      }
     }
     
     for(i=0;i<R;i++)
     {
      for(j=0;j<C;j++)
      {
       if(A[i][j]=='.')continue;
       if(A[i][j]=='^')
       {
        for(ii=0;ii<i;ii++)
        {
         if(A[ii][j]!='.')break;
        }
        if(ii==i)
        {
         int flag=0;
         for(k=0;k<R;k++)
         {
          if(A[k][j]!='.')flag++;
         }
         for(k=0;k<C;k++)
         {
          if(A[i][k]!='.')flag++;
         }
         if(flag==2)
         {
          cout<<"IMPOSSIBLE"<<endl;
          return;
         }
         else
         {
          ret++;
         }
         
        }
        
       }
       
       if(A[i][j]=='v')
       {
        for(ii=i+1;ii<R;ii++)
        {
         if(A[ii][j]!='.')break;
        }
        if(ii==R)
        {
         int flag=0;
         for(k=0;k<R;k++)
         {
          if(A[k][j]!='.')flag++;
         }
         for(k=0;k<C;k++)
         {
          if(A[i][k]!='.')flag++;
         }
         if(flag==2)
         {
          cout<<"IMPOSSIBLE"<<endl;
          return;
         }
         else
         {
          ret++;
         }
         
        }
        
       }
       
       if(A[i][j]=='<')
       {
        for(jj=0;jj<j;jj++)
        {
         if(A[i][jj]!='.')break;
        }
        if(jj==j)
        {
         int flag=0;
         for(k=0;k<R;k++)
         {
          if(A[k][j]!='.')flag++;
         }
         for(k=0;k<C;k++)
         {
          if(A[i][k]!='.')flag++;
         }
         if(flag==2)
         {
          cout<<"IMPOSSIBLE"<<endl;
          return;
         }
         else
         {
          ret++;
         }
         
        }
        
       }
       
       if(A[i][j]=='>')
       {
        for(jj=j+1;jj<C;jj++)
        {
         if(A[i][jj]!='.')break;
        }
        if(jj==C)
        {
         int flag=0;
         for(k=0;k<R;k++)
         {
          if(A[k][j]!='.')flag++;
         }
         for(k=0;k<C;k++)
         {
          if(A[i][k]!='.')flag++;
         }
         if(flag==2)
         {
          cout<<"IMPOSSIBLE"<<endl;
          return;
         }
         else
         {
          ret++;
         }
         
        }
        
       }
       
       
      }
     }
     cout<<ret<<endl;
     
     
}

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int tt;
  cin>>tt;
  for (int qq = 1; qq <= tt; qq++) {
    cout<<"Case #"<<qq<<": ";
    fflush(stdout);
    Solve();
    
    fflush(stdout);
  }
  
  
  return 0;
}
