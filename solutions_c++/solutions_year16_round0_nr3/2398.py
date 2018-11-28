#include<iostream>
#include<stdio.h>
#include<string.h>
#include<string>
#include<bitset>
#include<vector>
using namespace std;
#define LL long long int

int T, N, J;

string decimalToBinary(int num) {
     string ret = "";
     while (num > 0) {
        ret = (char) ((num%2) + '0') + ret;
        num /= 2;         
     }      
     return ret;
}

int smallestDivisor(LL num) {
     for (LL i = 2; i * i <= num; i++) {
         if (num % i == 0)
            return (int) i;
     }
     
     return -1;
}

int main(void)
{
     freopen("C-small-attempt0.in","r",stdin);
     freopen("C-small-attempt0.out","w",stdout);
     
     
     cin >> T;
     for (int cases = 1; cases <= T; cases++) {
         cin >> N >> J;
         
         cout << "Case #" << cases << ":\n";
         for (int mask = (1 << (N - 1)) + 1; mask < (1 << N); mask += 2) {
             
             bool can = true;
             vector<int> temp;
             
             for (int base = 2; base <= 10; base++) {
                 
                 LL num = 0, power = 1;
                 for (int i = 0; i < N; i++, power *= (LL) base) {
                     if (mask & (1 << i))
                        num = num + power;
                 }
                 
                 int divisor = smallestDivisor(num);
                 
                 if (divisor == -1) {
                     can = false;
                     break;            
                 }
                 
                 temp.push_back(divisor);
             }
             
             if (can) {
                J--;
                cout << decimalToBinary(mask);
                for (int i = 0; i < temp.size(); i++) 
                    cout << " " << temp[i];
                
                cout << endl;
                
                if (J == 0) 
                    break;         
             }
         }
         
     }
}
