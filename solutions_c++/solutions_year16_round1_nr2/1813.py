#include <bits/stdc++.h>
using namespace std;
int main()
{
  // freopen("out.txt","w",stdout);
   int  test , cs = 1;
   cin >> test;
   while(test--){
      int n;
      cin >> n;
         map < int,int > hit;
         vector < int > v;
      for(int i = 0 ; i< 2*n-1 ; i++){
         for(int j = 0 ; j< n ; j++){
             int a;
             cin >> a ;
             if(hit[a] == 0) v.push_back(a);
             hit[a]++;
         }
      }
      vector < int > ans;
      for(int i = 0 ; i< v.size() ; i++){
          if(hit[v[i]]&1)
             ans.push_back(v[i]);
      }
      sort(ans.begin() , ans.end());
      printf("Case #%d:", cs++);
      for(int i = 0 ; i< ans.size() ; i++)
        cout << ' ' << ans[i] ;
      cout << "\n";
   }

}
