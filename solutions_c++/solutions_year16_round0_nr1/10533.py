#include <iostream>
using namespace std;
#include <stdio.h>

void check(int arr[], long long int n, long long int j, int val[], int count) {
    long long int  carry = 0;
    long long int t = n;
    for(int i = 0;i < count;i++) {
       long long int val1 = ((t % 10) * j) + carry;
        carry = val1 / 10;
        val1 = val1 % 10;
        if(arr[val1] == 0) {
            arr[val1] = 1;
            val[0]++;
        }
        t = t/10;
    }
    if(carry) {
        while(carry) {
            if(arr[carry%10] == 0) {
                arr[carry%10] = 1;
                val[0]++;
            }
            carry = carry / 10;
        }
    }
}

int main() {
// your code goes here
freopen("1.txt", "r", stdin);
freopen("2.txt", "w", stdout);
int t;
scanf("%d", &t);

for(int i = 1;i <= t;i++) {
   long long int n;
   scanf("%lld", &n);
   if(n == 0) {
       printf("Case #%d: INSOMNIA\n",i);
       continue;
   }
   int arr[10] = {0};
   int val[1] = {0};
   long long int j = 1;
   int count = 0;
   long long int t1 = n;
   while(t1) {
       count++;
       t1 = t1 / 10;
   }
   long long int tt = n;
   while(1) {
       tt = n * j;
       check(arr, n, j, val, count);
       if(val[0] >= 10) {
           break;
       }
       j++;
       
   } 
   printf("Case #%d: %lld\n",i, tt);
}
return 0;
}
