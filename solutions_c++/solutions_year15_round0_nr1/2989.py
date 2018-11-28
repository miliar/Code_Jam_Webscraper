#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>
#include <sstream>
using namespace std;

#define FOR(i, a, b) for(long long i=a; i<b; i++)
#define FORE(i, a, b) for(long long i=a; i<=b; i++)

#define PI 3.1415926535897932384626433

int main() {
	
    int T;
    cin >> T;
    
    char A[1100];
    int answer[1100];

    FOR(t, 0, T)
    {
      int l;
      scanf("%d %s", &l, A);

      int ans = 0;
      int standing = 0;
 //     printf("Test case %lld.\n", t);
      FORE(i, 0, l)
      {
        if (standing < i) 
        {   ans++; standing++;  }

   //    printf("standing = %d, i = %lld\n", standing, i);
        standing+=A[i] - 48;
      }
      answer[t] = ans;
    }

    FOR(t, 0, T) printf("Case #%lld: %d\n", t+1, answer[t]);
    return 0;
}

