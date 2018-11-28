#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>
#include <sstream>
#include <set>
using namespace std;

#define FOR(i, a, b) for(int i=a; i<b; i++)
#define FORE(i, a, b) for(int i=a; i<=b; i++)

#define PI 3.1415926535897932384626433
/*
int num_steps2(int from, int to)
{
  if (from <= to) return 0;
  if (from%2 == 0) return 2*num_steps2(from/2, to) + 1;
  return num_steps2(from/2, to) + num_steps2(from/2 + 1, to) + 1;
}
*/

int num_steps(int from, int to)
{
  if (from <= to) return 0;
  if (from % to == 0) return from/to - 1;
  return from / to;
} 



int main() {
	 freopen ("myfile.txt","r",stdin);


    int T;
    cin >> T;
    
    int A[1100];
    int answer[1100];

    FOR(t, 0, T)
    {
      int D;
      cin >> D;

      FOR(i, 0, D) {
          cin >> A[i];
      }

      sort(A, A+D, greater<int>());

      int ans = A[0];
      
      for(int i = A[0]; i > 1; i--)
      {  
        int trythis = i;
     //  printf("Trying to leave %d.\n", i);
        for (int j = 0; j < D; j++) 
        {
  //          printf("   Added %d on reducing from %d to %d\n", num_steps(A[j], i), A[j], i);
   //         printf("   Second one would give %d\n", num_steps2(A[j], i));
            trythis+=num_steps(A[j], i);
        }
        if (trythis < ans) ans = trythis;
      } 

      answer[t] = ans;
    }

    FOR(i, 0, T) printf("Case #%d: %d\n", i+1, answer[i]);

    return 0;
}

