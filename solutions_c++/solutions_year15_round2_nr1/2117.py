#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;


const int MAX = 1000*1000+1;
const int INFINI = MAX+1;

int N;
int pos[MAX];


int rev(int n){
      int res = 0;
      while(n>0)
      {
            res*=10;
            res+=n%10;
            n/=10;
      }
      return res;
}


int trouver(){
      pos[N] = 1;
      for(int i=N-1; i>=1; i--){
            int a = rev(i);
            pos[i] = pos[i+1]+1;
            if(a>i && a<=N){
              pos[i] = min(pos[i], pos[a]+1);
            }
      }
      return pos[1];
}

int main(){

   int nbTests;
   scanf("%d", &nbTests);
   for(int k=1; k<=nbTests; k++){
      scanf("%d", &N);
      printf("Case #%d: %d\n",k, trouver());
   }

}