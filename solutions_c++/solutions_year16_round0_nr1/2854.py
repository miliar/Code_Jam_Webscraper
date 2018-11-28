#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;

int solve(int n) {
     if (n == 0) 
         return -1;
     
     int occ[10];
     memset(occ, 0, sizeof(occ));
     
     for (int i = 1;; i++) {
         
         int temp = i * n;
         while (temp > 0) {
            occ[temp % 10] = 1;
            temp /= 10;         
         }
         
         int count = 0;
         for (int j = 0; j < 10; j++)
            count += occ[j];
            
         if (count == 10) 
            return i * n;
     }
}

int main(void)
{
     freopen("A-large.in","r",stdin);
     freopen("A-large.out","w",stdout);
     
     int T, N;
     
     cin >> T;
     for (int cases = 1; cases <= T; cases++) {
         cin >> N;
         cout << "Case #" << cases << ": ";
         
         int ans = solve(N);
         if (ans == -1)
            cout << "INSOMNIA\n";
         else
            cout << ans << endl; 
     }
}
