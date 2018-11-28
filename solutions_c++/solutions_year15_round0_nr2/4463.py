#include<iostream>
#include<algorithm>
using namespace std;
const int MAX = 1010;
int A[MAX];
int main(){
   int T;
   cin >> T;
   for(int i = 1; i <= T; i++){
      int D; cin >> D;
      int max = 0;
      for(int j = 0; j < D; j++){
	 cin >> A[j];
	 if(A[j] > max)
	    max = A[j];
      }
      int min = MAX;
      for(int j = 1; j <= max; j++){
	 int res = 0;
	 res += j;
	 for(int k = 0; k < D; k++){
	    res += (A[k]-1)/j;
	 }
	 if(res < min)
	    min = res;
      }
      
      cout << "Case #" << i << ": " << min << endl;
   }

   return 0;
}
