#include <iostream>
#include <cstdio>
#include <fstream>
#include <string>
#include <memory.h>
#include <cmath>

using namespace std;

#define Nmax 201

char A[Nmax], A1[Nmax], B[Nmax], T[Nmax];
char pal[Nmax];
char sq[2*Nmax];
int sqN, cA, cB, cA1;
long long intn;

void findNextPalindrome(char *a, int &n) {
   int i, j;
   //string res = a;
   j=n-1;
   while(j >= 0) {
      if(a[j] == '9')
         j--;
      else
         break;
   }
   
   if(j < 0) {
      a[0] = '1';
      for(j=1; j<=n; j++)
         a[j] = '0';
      n++;
   }
   /*else if(checkPalindrome(a,n) == true)
   
   if(n == 1) {
      pal[0] = a[0];
      pal[1] = '\0';
      return;
   }
      
   
   for(i=0; i<=n/2; i++) {
      if(a[i] < a[n-1-i]) {
         pal[i] = a[n-1-i];
         pal[n-1-i] = a[n-1-i];
      }
      else {
         pal[i] = a[i];
         pal[n-1-i] = a[i];
      }
   }
   pal[n] = '\0';*/
   
   
   int carry,low,high;
   char temp;
 
        i=0;j=n-1;
        while(i<j && a[j]>=a[i])
        i++,j--;
 
        if(i>=j) // if they cross each other
        {
                if(!(n&1))      //handle even length palindrome
                        i--,j++;
                carry=1;
                while(i>=0)
                {
                        a[i]+=carry;
                        carry=(a[i]-'0')/10;
                        a[i] = (a[i]-'0')%10 + '0';
                        a[j++]=a[i--];
                }
        }
        else
        {
                low=i+1;high=j-1;
                while(i>=0)
                        a[j++]=a[i--];
                while(low<high) // handle the case 8683
                {
                        temp = a[high];
                        a[high]=a[low]<a[high]?a[low]:a[high];
                        a[high]=a[low]<temp?a[low]:temp;
                        low++;high--;
                }
        }
}

void rightshift(char *a, int &n, int k) {
   int i;
   for(i=n; i>=0; i--)
      a[i+k] = a[i];
   for(i=k-1; i>=0; i--)
      a[i] = '0';
   n += k;
}

void add(char *a, int n) {
   int i;
   int sum, carry = 0;
   for(i=0; i<n; i++) {
      sum = (a[i]-'0') + (sq[i]-'0') + carry;
      sq[i] = sum%10 +'0';
      carry = sum/10;
   }
   while(carry > 0) {
      sum = sq[i]-'0' + carry;
      sq[i] = sum%10 +'0';
      carry = sum/10;
      i++;
   }
   if(i>sqN)
      sqN = i;
}

void square(char *num, int n) {
   int i, j, k;
   int carry = 0;
   int prod;
   char temp[2*Nmax];
   
   memset(sq, '0', sizeof(sq));
   sqN = 0;
   //cout << "num:" << num << "\n";
   for(i=n-1; i>=0; i--) {
      carry = 0;
      for(k=n-1, j=0; k>=0; k--, j++) {
         prod = (num[k]-'0')*(num[i]-'0') + carry;
         //cout << "prod: " << prod << "\n";
         temp[j] = prod%10 + '0';
         carry = prod/10;
      }
      while(carry > 0) {
         temp[j++] = carry%10 + '0';
         carry /= 10;
      }
      temp[j] = '\0';
      rightshift(temp, j, n-1-i);
      add(temp, j);
      //cout << "temp: " << temp << "\n";
   }
   
   for(i=0; i<sqN/2; i++) {
      carry = sq[i];
      sq[i] = sq[j-1-i];
      sq[j-1-i] = carry;
   }
   sq[sqN] = '\0';
}

bool checkPalindrome(char *a, int n) {
   //cout << "a: " << a << " --n: " << n << "\n";
   for(int i=0; i<n/2; i++)
      if(a[i] != a[n-1-i])
         return false;
   //cout << "ll\n";
   return true;
}

void copy(char *a, char *b, int n) {
   for(int i=0; i<=n; i++)
      b[i] = a[i];
}

bool comp(char *a, int na, char *b, int nb) {
   bool res = true;
   if(na > nb)
      res = false;
   else if(na == nb) {
      for(int i=0; i<na; i++) {
         if(a[i] > b[i]) {
            res = false;
            break;
         }
         else if(a[i] < b[i]) {
            res = true;
            break;
         }
      }
   }
   else
      res = true;
   return res;
}
        

long long findRes(char *a, int n) {
   long long res = 0;
   
   if(checkPalindrome(a,n) == false) {
      findNextPalindrome(a,n);
      //copy(pal, a, n);
   }      
   
   while(1) {
      //cout << "num: " << a << "\n";
      square(a,n);
      //cout << "sq: " << sq << "\n";
      if(comp(A1, cA1, sq, sqN) == true) {
         
         if(comp(sq, sqN, B, cB) == false)
            break;
         //cout << "h\n";
         if(checkPalindrome(sq, sqN) == true)
            res++;
      }
      findNextPalindrome(a,n);
      //copy(pal, a, n);
   }
   return res;
}

void convertToInt(char *a, int n) {
   intn = 0ll;
   for(int i=0; i<n; i++)
      intn = (intn*10ll) + (long long)(a[i]-'0');
}

void convertTochar(long long h, char *a, int &n) {
   n=0;
   while(h > 0) {
      a[n++] = (h%10ll) + '0';
      h /= 10ll;
   }
   a[n] = '\0';
   
   int tem;
   for(int i=0; i<n/2; i++) {
      tem = a[i];
      a[i] = a[n-1-i];
      a[n-1-i] = tem;
   }
}  

int main(void) {
   freopen("C-large-1.in", "r", stdin);
   freopen("fairAndSquare4.out", "w", stdout);
   int T;
   char c;
   int k;
   
   scanf("%d\n", &T);
   //printf("%d\n", T);
   
   for(k=1; k<=T; k++) {
      cA = cB = 0;
      while(scanf("%c", &c)) {
         //printf("%c\n", c);
         if(c == ' ' || c == '\n')
            break;
         else
            A[cA++] = c;
      }
      A[cA] = '\0';
      //cout << "A: " << A << "\n";
      //printf("jj\n");
      while(scanf("%c", &c)) {
         //printf("%c\n", c);
         if(c == ' ' || c == '\n')
            break;
         else
            B[cB++] = c;
      }
      B[cB] = '\0';
      //cout << "B: " << B << "\n";
      
      //findNextPalindrome(A, cA);
      //cout << pal << "\n";
      //square(A, cA);
      //cout << sq << "\n\n";
      copy(A, A1, cA);
      cA1 = cA;
      convertToInt(A, cA);
      //cout << "intn: " << intn << "\n"; 
      intn = sqrt(intn);
      //cout << "intn: " << intn << "\n";      
      convertTochar(intn, A, cA);
      //cout << "A: " << A << "\n\n";
      printf("Case #%d: %lld\n", k, findRes(A, cA));
   }
   
   return 0;
}
