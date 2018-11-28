#include<iostream>
#include<algorithm>
#include<cstdio>

using namespace std;

int n;
double a[1000], b[1000];

int dwar()
{
   int res = 0;
   for(int i = 0, j = 0; i < n; ++i){
      if(a[i] > b[j]){
         ++res;
         ++j;
      }else{
         ;
      }
   }
   return res;
}

int war()
{
   int res = n;
   for(int i = 0, j = 0; i < n && j < n; ++i, ++j){
      while(j < n && a[i] > b[j]){
         ++j;
      }
      if(j < n)
         --res;
   }
   return res;
}

int main()
{
   int T;
   cin >> T;
   for(int h = 1; h <= T; ++h){
      cin >> n;
      for(int i = 0; i < n; ++i)
         cin >> a[i];
      for(int i = 0; i < n; ++i)
         cin >> b[i];
      sort(a, a+n);
      sort(b, b+n);
      /*
      for(int i = 0; i < n; ++i)
         cout << a[i] << ' ';
      cout << endl;
      for(int i = 0; i < n; ++i)
         cout << b[i] << ' ';
      cout << endl;
      */
      cout << "Case #" << h << ": " << dwar() << ' ' << war() << endl;
   }
   
   
   return 0;
}

