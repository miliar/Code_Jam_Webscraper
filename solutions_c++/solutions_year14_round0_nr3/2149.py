#include <iostream>
#include <vector>
#include <cstring>
using namespace std;
int cnt1(int i) {
   int ans = 0 ;
   while (i) { ans +=(i%2); i/=2;}
   return ans;
}
char fa[64];
int getfa(int x) {
   if (fa[x] != x) return fa[x] = getfa(fa[x]);
}
void me(int a, int b) {
 fa[(getfa(a))] = getfa(b);
}
bool check(int i0, int x, int y) {
   //cout << i0 << endl;
   bool map[8][8]; int msk = 1;
   for (int i = 0 ; i < x; i++)
    for (int j = 0 ; j < y ; j ++) {
       if (i0&msk) map[i][j] = true; else map[i][j] = false;
       msk<<=1;
    }
   int cnt[8][8]; memset(cnt,0,sizeof(cnt));
   for (int i = 0 ; i < x; i++)
      for (int j = 0 ; j < y; j++) {
         if (map[i][j]) cnt[i][j] = -1; else
         for (int dx = -1; dx <=1; dx++)
            for (int dy= -1; dy<=1; dy++) if (i+dx >=0 && i+dx <x && j+dy>=0 && j+dy<y)
                if (map[i+dx][j+dy]) cnt[i][j]++;
      }
   int n = x*y;
//   for (int i = 0 ; i < x; i++) {for (int j = 0 ; j < y ; j++) cout <<cnt[i][j]<<"\t"; cout << endl; }
   for (int i = 0 ; i < n ; i++) fa[i] = i;
   int totcnt0 = 0;
   for (int i = 0 ; i<x; i++)
    for (int j = 0 ; j < y; j++)
       if (cnt[i][j] ==0) {
          if (i>0) if (cnt[i-1][j] ==0) me(i*y+j,(i-1)*y+j);
          if (j>0) if (cnt[i][j-1] ==0) me(i*y+j,i*y+j-1);
          totcnt0++;
       }
   int pos = -1;
   for (int i = 0 ; i <x; i++) 
      for (int j = 0 ; j < y; j++) 
         if (cnt[i][j] ==0) {
            if (pos <0) pos = i*y+j;
            if (getfa(i*y+j) != getfa(pos)) return false;
         }

   if (pos <0) {
     int totcntn0 = 0;
     for (int i = 0 ;  i < x; i++)
        for (int j = 0 ; j < y ; j++) if (map[i][j]==false) {
          pos = i*y+j;
          totcntn0++;
        }
        if (totcntn0!=1) return false;
   }
   int totcntn0 = 0;
   for (int i = 0 ;  i < x; i++)
      for (int j = 0 ; j < y ; j++) if (map[i][j]==false) totcntn0++;
   if (totcntn0>1)
   for (int i = 0 ; i < x; i++)
   for (int j = 0 ; j < y ; j++) 
     if (cnt[i][j] > 0 ) {
        int tt = 1;
         for (int dx = -1; dx <=1; dx++)
            for (int dy= -1; dy<=1; dy++) if (i+dx >=0 && i+dx <x && j+dy>=0 && j+dy<y)
                tt *= cnt[i+dx][j+dy];
          if (tt !=0) 
          return false;

     }
   for (int i = 0 ; i < x; i++ ) {
   for (int j = 0 ; j < y; j++) 
      if (i*y+j == pos) cout <<"c";
      else if (map[i][j]) cout <<"*"; else cout <<".";
      cout << endl;
   }
   return true;
}
void ff(int x, int y ,int z ){
   int nn = x*y;
   for (int i = 0; i < (1<<nn); i++)
      if (cnt1(i) == z) {
//      cout << cnt1(i) <<":"<<z<<endl;
        if (check(i,x,y))  return;
      }
      cout << "Impossible"<<endl;
}
int main() {
    int t;
    cin >> t;
    for (int c = 1; c<= t; c++)  {
        cout << "Case #" << c <<":" << endl;
        int x,y,z;
        cin >> x >> y >> z;
        ff(x,y,z);
    }

}

