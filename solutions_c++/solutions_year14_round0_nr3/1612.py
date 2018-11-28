#include <algorithm>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <cstring>
#include <cstdlib>
#include <climits>
#include <fstream>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <map>
#include <set>
using namespace std;

#define pb push_back
#define mp make_pair
#define sz size()
#define bg begin()
#define en end()
#define Y second
#define X first
typedef long long ll;

#define fi freopen("input.txt","r",stdin)
#define fo freopen("output.txt","w",stdout)

const double pi     =   acos(-1.0);
const double eps    =   1e-8;

#define print(a) cout<<(#a)<<" = "<<a<<"  ";
#define println(a) cout<<(#a)<<" = "<<a<<"\n";
#define fill(a,val) memset(a ,val, sizeof(a) );

vector <string> parse(string s, string c)
{
  int len = c.length(), p = -len, np;
  vector <string> ans;

  do
    {
      np = s.find(c, p+len);
      ans.push_back(s.substr(p+len, np - p - len));
      p = np;
    }
  while (p != string::npos);

  return ans;
}


/*Solution code starts here */

int dx[]={-1,-1,-1, 0,0,  1, 1, 1};
int dy[]={-1, 0, 1, -1,1, -1 ,0, 1};

int val[5][5];
int in[5][5];//0 if empty ,1 if mines

bool done[5][5];
bool  cover[5][5];

int row,col,mines;

void dfs( int x, int y)
{
     if( done[x][y])
         return ;

     done[x][y]=true;
     cover[x][y]=true;

     for(int i=0;i<8;i++)
     {
          int nx=x+dx[i];
          int ny=y+dy[i];

          if( (nx < 0) || (nx >=row) || (ny <0) || (ny >=col) )
           continue;

          if( val[nx][ny]==0)
             dfs(nx,ny);

          if( val[nx][ny]<=8)
             cover[nx][ny]=true;
     }

}

bool process( int cn)
{
     fill(val,0);

     for(int i=0;i<row;i++)
         for(int j=0;j<col;j++)
           if( in[i][j]==1)
        {
             val[i][j]=20;

             for(int k=0;k<8;k++)
             {
                  int tx=i+dx[k];
                  int ty=j+dy[k];

                  if( (tx <0) || (tx>=row) || (ty<0) || (ty >=col) )
                    continue;

                  val[tx][ty]++;
             }
     }
//
//     cout<<"\n\n\nin\n";
//     for(int i=0;i<row;i++,cout<<endl)
//         for(int j=0;j<col;j++)
//            cout<<in[i][j]<<" ";
//
//     cout<<"\nVal is\n";
//
//          for(int i=0;i<row;i++,cout<<endl)
//         for(int j=0;j<col;j++)
//          cout<<val[i][j]<<" ";


     //start dfs , all '0' must be in compnent



     int x=-1,y=-1;

    //find a zero
       for(int i=0;i<row;i++)
          for(int j=0;j<col;j++)
            if( val[i][j]==0)
       {
           x=i;
           y=j;
           break;
       }

       if(x==-1)//kow zero wala nahi mila
       {
            return  false;
       }

       fill(done,0);
       fill(cover,0);

       dfs(x,y);

       //all zero must be connexted
       for(int i=0;i<row;i++)
         for(int j=0;j<col;j++)
           if( val[i][j]<=8)
              if( cover[i][j]==false)
               {
                  return false;
               }



        return true;

}

void solve( int t)
{

	bool mila=false;


	cin>>row>>col>>mines;

	if( row*col-mines==1)//only one
    {
         printf("Case #%d:\n",t);

         for(int i=0;i<row;i++,cout<<endl)
             for(int j=0;j<col;j++)
         {
                if(i==row-1)
                     if(j==col-1)
                       {cout<<"c";
                         continue;
                       }

                       cout<<"*";

         }

         return;
    }

//	cout<<row<<" "<<col<<" "<<mines<<endl;

  for(int mask=0;mask< ( 1<<(row*col) ) ; mask++ )
      if( __builtin_popcount(mask)==mines)
    {

            int cont=0;

          for(int i=0;i<row;i++)
             for(int j=0;j<col;j++)
            {
                 int id=i*col+j;

                 if( mask&(1<<id) )
                     in[i][j]=1;
                 else
                     { in[i][j]=0;
                       cont++;
                     }


//                  cout<<id<<"  "<<(mask&(1<<id))<<"  "<<i<<" "<<j<<endl;
            }

//            cout<<"\nHere maks is "<<mask<<endl;;



            if( process(cont) )
            {
                mila=true;
				break;
            }
    }




    if( !mila)
    {
       printf("Case #%d:\n",t);
       printf("Impossible\n");
       return;
    }
    else
    {
       printf("Case #%d:\n",t);

	    bool zd=0;

	    for(int i=0;i<row;i++,cout<<endl)
	         for(int j=0;j<col;j++)
	            if( val[i][j]<=8)
	              {
	                    if( val[i][j]==0)
	                    {
	                        if(zd==true)
	                         cout<<".";
	                        else
	                        {
	                            cout<<"c";
	                            zd=true;
	                        }
	                    }
	                   else
	                      cout<<".";
	              }
	              else
	              {
	                  cout<<"*";
	              }
	}
}


int main()
{

  fi;fo;

  int test;

  cin>>test;

  for(int i=1;i<=test;i++)
  {
        solve(i);
  }

 return 0;

}

