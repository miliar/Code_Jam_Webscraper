#include <cstdio>
#include <iostream>
#include <fstream>
#include <cstring>
#include <algorithm>

using namespace std;

const int MAXN = 1010;

char str[MAXN];
int len;

bool moze(int koliko){
      int brojac = 0;
      int imam = koliko;

      brojac = str[0] - '0';

      for(int i = 1; i <= len; i++){
           int oni_zele_toliko = i;

           if(brojac >= oni_zele_toliko){
                  int koliko_ih_je = str[i] - '0';
                  brojac += koliko_ih_je;
                  continue;
           }

           else if(brojac < oni_zele_toliko){
                  int koliko_im_fali = oni_zele_toliko - brojac;
                  imam -= koliko_im_fali;
                  if(imam < 0) return false;
                  brojac += koliko_im_fali + (str[i] - '0');
           }
      }

      return imam >= 0;
}

int main(){
   ofstream izlaz("standing4.txt");
   freopen("aaa.in", "r", stdin);

   int t;
   scanf("%d", &t);

for(int j = 1; j <= t; j++){
   char out[25];
   bool mozeOdma = true;

   scanf("%d", &len);
   scanf("%s", &str);

   int koliko = str[0] - '0';

   for(int i = 1; i <= len; i++){
            int tmp = i;

            if(koliko < tmp){
                  mozeOdma = false;
                  break;
            }

            koliko += str[i] - '0';
   }

   if(mozeOdma){
        //printf("Case #%d: 0\n", j);
        sprintf(out, "Case #%d: 0\n", j);
        izlaz<<out;
        continue;
   }

   int lo = 0, hi = 20100;
   int mini = 20100;

   while(lo < hi){
       int mid = (lo + hi) / 2;
       if(moze(mid)){
            hi = mid;
            mini = min(mini, mid);
       }
       else{
            lo = mid + 1;
       }
   }

   //printf("Case #%d: %d\n", j, mini);
   sprintf(out, "Case #%d: %d\n", j, mini);
   izlaz<<out;
}

   return 0;
}
