#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>

#include <iostream>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <algorithm>
#include <map>

using namespace std;

int check(char *base, char strings[][200], int num){
   for(int i = 0; i < num; ++i){
      char thisbase[200] = {0};
      thisbase[0] = strings[i][0];
      int thisbasei = 1;
      for(int j = 1; strings[i][j]; j++){
         if(strings[i][j] != thisbase[thisbasei-1]) thisbase[thisbasei++] = strings[i][j];         
      }
      if( strcmp(base, thisbase) ) return 0;
   }
   return 1;
}

int main(){
   freopen("A-small-attempt0.in", "r", stdin);
   freopen("A-small-attempt0.out", "w", stdout);
   
   int testn;
   cin >> testn;
   
   for(int test = 1; test <= testn; test++){
      int num;
      cin >> num;
      
      char strings[200][200] = {0};
      
      for(int i = 0; i < num; ++i) cin >> strings[i];
      
      char base[200] = {0};
      base[0] = strings[0][0];
      int basei = 1;
      for(int i = 1; strings[0][i]; i++){
         if(strings[0][i] != base[basei-1]) base[basei++] = strings[0][i];         
      }
      
      printf("Case #%d: ", test);
      if( check(base, strings, num) ){
         int myfre[200][200] = {0}; 
         int fre[200] = {0};
         
         for(int i = 0; i < num; ++i){
            char last = strings[i][0];
            int basei = 0;
            fre[0]++;
            myfre[i][0]++;
            
            for(int j = 1; strings[i][j]; j++){
               if(strings[i][j] == last){
                  fre[basei]++;
                  myfre[i][basei]++;
               }else{
                  last = strings[i][j];
                  basei++;
                  fre[basei]++;
                  myfre[i][basei]++;
               }
            }
         }
         
         // test
         //for(int i = 0; fre[i]; ++i) printf("%d ", fre[i]);
         
         //for(int i = 0; i < num; ++i){
            //for(int j = 0; myfre[i][j]; j++) printf("%d ", myfre[i][j]);
            //printf("\n");
         //}
         
         double avg[200] = {0};
         for(int i = 0; fre[i]; ++i){
            avg[i] = (double)(fre[i]) / num;
         }
         
         int sum1 = 0, sum2 = 0;
         for(int i = 0; i < num; ++i){
            for(int j = 0; fre[j]; ++j){
               int b1 = floor(avg[j]);
               int b2 = ceil(avg[j]);
               
               if( myfre[i][j] > b1 ) sum1 += myfre[i][j] - b1;
               if( myfre[i][j] < b1 ) sum1 += b1 - myfre[i][j];
               
               if( myfre[i][j] > b2 ) sum2 += myfre[i][j] - b2;
               if( myfre[i][j] < b2 ) sum2 += b2 - myfre[i][j];
            }
         }
         
         if(sum1 < sum2) printf("%d\n", sum1);
         else printf("%d\n", sum2);
      }else{
         printf("Fegla Won\n");
      }
   }
   
   return 0;
}
