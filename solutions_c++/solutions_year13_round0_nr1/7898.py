//Data Structure includes
#include<vector>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<deque>
#include<string>


//Other Includes
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cassert>
#include<cstdlib>
#include<cstdio>
#include<cmath>

#define PB push_back
#define MP make_pair
#define MAXIMUM 18446744073709551615ULL
#define MAX 1010

using namespace std;

typedef long long int LL;
typedef unsigned long long int ULL;
typedef unsigned int UI;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector< pair<int,int> > VPI;

bool checkRows(string grid[4], char p)
{
    for (int i=0; i<4; ++i)
    {
        bool found = false;
        for (int j=0; j<4; ++j)
        {
            if (grid[i][j] == p || grid[i][j] == 'T') continue;
            found = true;
            break;
        }
        if (!found) return true;
    }
return false;
}

bool checkCols(string grid[4], char p)
{
    for (int j=0; j<4; ++j)
    {
        bool found = false;
        for (int i=0; i<4; ++i)
        {
            if (grid[i][j] == p || grid[i][j] == 'T') continue;
            found = true;
            break;
        }
        if (!found) return true;
    }

return false;
}

bool checkDiag(string grid[4], char p)
{
    bool found = false;
    for (int i=0; i<4; ++i)
    {
        if (grid[i][i] == p || grid[i][i] == 'T') continue;
        found = true;
        break;
    }
    if (!found) return true;

    found = false;
    for (int i=0; i<4; ++i)
    {
        if (grid[3-i][i] == p || grid[3-i][i] == 'T') continue;
        found = true;
        break;
    }
    if (!found) return true;
return false;
}
bool Xwon(string grid[4])
{
    if (checkRows(grid, 'X')) return true;
    if (checkCols(grid, 'X')) return true;
    if (checkDiag(grid, 'X')) return true;
return false;
}

bool Owon(string grid[4])
{
    if (checkRows(grid, 'O')) return true;
    if (checkCols(grid, 'O')) return true;
    if (checkDiag(grid, 'O')) return true;
return false;
}

bool Draw(string grid[4])
{
    bool dot = false;
    for (int i=0; i<4; ++i)
    {
        for (int j=0; j<4; ++j)
        if (grid[i][j] == '.')
        {
            dot = true;
            break;
        }
    }
    if (dot) return false;
return true;
}

int main()
{
   freopen("inp.txt", "r", stdin);
   freopen("Op.txt", "w", stdout);
   int t;
    cin>>t;
   for (int c=1; c<=t; ++c)
   {
       string grid[4];
       for(int i=0; i<4; ++i) cin>>grid[i];
       printf("Case #%d: ",c);
       //cout<<"checking for x..";
       if (Xwon(grid))
       {

           printf("X won\n");
           continue;
       }
       //cout<<"checking for O..";
       if (Owon(grid))
       {

           printf("O won\n");
           continue;
       }
       if (Draw(grid))
       {
         //  cout<<"checking for draw..";
           printf("Draw\n");
           continue;
       }

       printf("Game has not completed\n");
   }
   //system("pause");
   return 0;
}
