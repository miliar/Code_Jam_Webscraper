#include <bits/stdc++.h>
using namespace std;



int min(int a, int b){
    if (a < b)
        return a;
    else
        return b;
}


int game(int C){
    int res = 0, aux = 0, pos = 0;

    for (int i = 0; i < C; i++){
        pos = C - 1;
        aux++;

    }


}

int main(){

   int T, R, C, W, res;
   cin >> T;

   for (int i = 0; i < T; i++){
       cin >> R;
       cin >> C;
       cin >> W;

       if (C == W)
           res = W;
       else{

           if (W==1){
               res = R*C;
           }

           else if (R > 1){
               int j = 0;
               res = 0;

               while (j < (R)*(C)){
                   j += W;
                   res++;
               }
               res += W - 1;

           }else{

               int j = 0;
               res = 0;

               while (j < C){
                   j += W;
                   res++;
               }
               res += W - 1;

           }

       }



       cout << "Case #" << (i+1) << ": " << res << endl;
   }
   return 0;
}

