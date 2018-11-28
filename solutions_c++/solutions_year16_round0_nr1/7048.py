#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
#include <bitset>
#define MMAX 2147483647

using namespace std;

int n;
bitset<15> dig;
long long int m;

void readData(){
   scanf("%d", &n);
}

void markDigits(int x){
   do {
      dig[x%10] = 1;
      x /= 10;
   }while (x);
}

void printData(){
   long long int i;
   dig = 0;
   m = n;
   i = 0;
   while (dig != 1023 && m*i < MMAX && i <= 100000){
      i++;
      markDigits(m*i);
   }
   if (dig == 1023)
      printf("%lld", m*i);
   else
      printf("INSOMNIA");
}

int main()
{
   freopen("data.in", "r", stdin);
   freopen("data.out", "w", stdout);
   int T, t;
   scanf("%d", &T);
   t = T;
   while (t--){
      readData();
      printf("Case #%d: ", T-t);
      printData();
      printf("\n");
   }

   return 0;
}
