#include <bits/stdc++.h>
using namespace std;
int main()
{
//  freopen("out.txt", "w", stdout);
  int test, cs = 1 ;
  cin >> test;
  map < char , int > hit;
  hit['+'] = 1;
  hit['-'] = 0;
  while(test--){
      vector < pair<int,int> > v;
      string s ;
      cin >> s;
      for(int i = 0 ; i< s.size() ; i++){
            char ch = s[i];
            int counter = 0;
            while(s[i] == ch && i < s.size()){
               counter++;
               i++;
            }
            i--;
            v.push_back(make_pair(counter,hit[ch]));
      }
      int flip = 0;
      for(int i = 0 ; i< v.size() ; i++){
         int ff = v[i].first;
         int ss = v[i].second;
         if( i == v.size() -1 && ss == 1) continue;

         flip++;
      }

      printf("Case #%d: %d\n",cs++ , flip);
      v.clear();

  }

}
