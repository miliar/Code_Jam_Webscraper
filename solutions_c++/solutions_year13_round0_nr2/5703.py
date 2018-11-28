#include <iostream>
using namespace std;

class Board{
   int **b;
   int M,N;
public:
   Board(int n, int m) : N(n), M(m) {
      b = new int*[N];
      for(int i=0; i<N; i++){
         b[i] = new int[M];
         for(int j=0; j<M; j++) {
            cin >> b[i][j];
         }
      }
   }

   ~Board() {
      for(int i=0; i<N; i++)
         delete[] b[i];
      delete[] b;
   }
   
   bool valid() {
      bool valid = true;
      bool currently_valid;
      int max;
      for(int i=0; i<N; i++){
         for(int j=0; j<M; j++){
            currently_valid = true;
            // check if index is valid.
            max = b[i][j];
            for(int k=0; k<N; k++){
               if(k != i && max < b[k][j]) {
                  max = b[k][j];
               }
            }
            if( max > b[i][j])
               currently_valid = false;
            max = b[i][j];
            for(int k=0; k<M && !currently_valid; k++){
               if(k != j && max < b[i][k]) {
                  max = b[i][k];
               }
            }
            if(!currently_valid && max > b[i][j])
               return false;

         }
      }
      return true;
   }
};


int main() {
   Board *b; //new Board(3,3);
   int T;
   int N, M;
   bool ans;
   string str_ans;
   cin >> T;
   for(int i=0; i<T; i++) {
      cin >> N >> M;
      b = new Board(N,M);
      ans = b->valid();
      str_ans = ans?"YES":"NO";
      cout << "Case #" << i+1 << ": " << str_ans << endl;;
      delete b;
   }


   return 0;
}
