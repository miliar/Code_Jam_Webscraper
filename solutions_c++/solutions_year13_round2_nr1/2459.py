#include <cstdio>

#include <vector>
#include <algorithm>

using namespace std;

int main(){
   int test, ti = 1, my, num, list[100];
   scanf("%d", &test);
   
   while(test--){
      scanf("%d%d", &my, &num);
      
      for(int i = 0; i < num; ++i){
         scanf("%d", &list[i]);
      }
      vector<int> vlist(list, list+num);
      sort(vlist.begin(), vlist.end());
      
      int min = 0x7fffffff;
      for(int tt = 0; tt < (0x1 << vlist.size()); ++tt){
         int lmy = my;
  
         vector<int> nlist;
         for(int i = 0; i < vlist.size(); ++i){
            if( (tt >> i) % 2 ) nlist.push_back(vlist[i]);
         }
         sort(nlist.begin(), nlist.end());
         
         
         int ans = vlist.size() - nlist.size();
         while( nlist.size() ){
            if(nlist[0] < lmy){
               lmy += nlist[0];
               nlist.erase(nlist.begin());
            }else{
               if(lmy == 1){
                  ans = 0x7fffffff;
                  break;
               }
               
               while(1){
                        
                  
                  lmy += lmy-1;
                  ans++;
                  if(nlist[0] < lmy) break;
               }
            }
         }
         //printf("[%d]", ans);
         
         if(ans < min) min = ans;
      }
   
      printf("Case #%d: %d\n", ti++, min);
   }

   return 0;    
}
