#include <cstdio>

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main(){
   freopen("D-small-attempt1.in", "r", stdin);
   freopen("output.txt", "w", stdout);

   int test, ti = 1;
   cin >> test;

   while(test--){
      printf("Case #%d:", ti++);
      
      int n;
      cin >> n;
      
      double nom[50], ken[50];
      for(int i = 0; i < n; ++i) cin >> nom[i];
      sort(nom, nom+n);
      for(int i = 0; i < n; ++i) cin >> ken[i];
      sort(ken, ken+n);
      
      int ttt[50];
      for(int i = 0; i < n; ++i) ttt[i] = i;
      
      int war = 0, def = 0;
      do{
         int score = 0;
         for(int i = 0; i < n; ++i) if(nom[i] > ken[ttt[i]]) score++;
         if( score > war ) war = score;
      }while( next_permutation(ttt, ttt+n) );
      
      
      int score = 0;
      vector<double> kenlist(ken, ken+n);
      for(int i = 0; i < n; ++i){
         int j;
         for(j = 0; j < kenlist.size() && nom[i] > kenlist[j]; j++);
         if(j == kenlist.size()){
            kenlist.erase(kenlist.begin());
            score++;
         }else{
            kenlist.erase(kenlist.begin()+j);
         }
      }
      if( score > def ) def = score;
      
      printf(" %d %d\n", war, def);
   }

   return 0;
}
