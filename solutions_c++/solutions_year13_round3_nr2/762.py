#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

struct T
{
   int x;
   int y;
   int p;
   T() {}
   T(int x, int y, int p) : x(x), y(y), p(p) {}
};

const int delta[][2] = { {0,-1}, {0, 1}, {-1,0}, {1, 0} };
const char inv[] = "NSEW";
const char deb[] = "SNWE";

int t[1000][1000];

bool c(int x, int y)
{
   return 0 <= x && x < 1000 && 0 <= y && y < 1000;
}

void debug(string x)
{
   int X = 0, Y = 0;
   for(int i=0; i<x.size(); i++)
      for(int j=0; ; j++)
         if(x[i] == deb[j])
         {
            X += (i+1)*delta[j][0];
            Y += (i+1)*delta[j][1];
            break;
         }
}

void f(int X, int Y)
{
   for(int i=0; i<1000; i++)
      for(int j=0; j<1000; j++)
         t[i][j] = -1;
   t[500][500] = 0;
   queue<T> file;
   file.push( T(500, 500, 1) );
   while(!(file.front().x == X+500 && file.front().y == Y+500))
   {
      T z = file.front();
      file.pop();
      for(int dir=0; dir<4; dir++)
      {
         T v(z.x + z.p*delta[dir][0], z.y + z.p*delta[dir][1], z.p+1);
         if(c(v.x, v.y) && t[v.x][v.y] == -1)
         {
            t[v.x][v.y] = z.p;
            file.push(v);
         }
      }
   }
   string r;
   int x = X+500, y = Y+500;
   for(int i=t[x][y]; i>0; i--)
      for(int dir=0; dir<4; dir++)
      {
         int x_ = x + i*delta[dir][0], y_ = y + i*delta[dir][1];
         if(c(x_, y_) && t[x_][y_] == i-1)
         {
            x = x_;
            y = y_;
            r += inv[dir];
            break;
         }
      }
   for(int i=r.size()-1; i>=0; i--)
      cout << r[i];
}

int main()
{
   int nbTests;
   cin >> nbTests;
   for(int test=1; test<=nbTests; test++)
   {
      int X, Y;
      cin >> X >> Y;
      cout << "Case #" << test << ": ";
      f(X, Y);
      cout << endl;
   }
   return 0;
}