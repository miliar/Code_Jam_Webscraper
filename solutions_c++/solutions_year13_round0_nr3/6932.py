#include <stdio.h>
#include<stdlib.h>
#include <iostream>
#include <sstream>
#include <stack>
#include <queue>
#include <math.h>
using namespace std;

int arr[20];
bool isPerfectSq(unsigned long long num);

unsigned long long nextPalin(unsigned long long num);
bool isPalUtil(unsigned long long num, unsigned long long* dupNum);
unsigned long long oneDigit(unsigned long long num);
bool isPalin(unsigned long long num);

unsigned long long printArray(int* arr, int n);
// A utility function to check if num has all 9s
int AreAll9s(int* arr, int n);
void generateNextPalindromeUtil (int num[], int n );
unsigned long long generateNextPalindrome( unsigned long long );
bool isPerfectSquare(unsigned long long n);

unsigned long long oneDigit(unsigned long long num)
{
   return (num >= 0 && num < 10);
}

bool isPerfectSquare(unsigned long long n)
{
  if (n < 0)
    return false;

  long tst = (long)(sqrt(n) + 0.5);
  return tst*tst == n;
}

void generateNextPalindromeUtil (int num[], int n ){
    int mid = n/2;
    bool leftsmaller = false;
    int i = mid - 1;
    int j = (n % 2)? mid + 1 : mid;
    while (i >= 0 && num[i] == num[j])
      i--,j++;
     if( i < 0 || num[i] < num[j])
       leftsmaller = true;
     while (i >= 0)
     {
        num[j] = num[i];
        j++;
        i--;
     }
    if(leftsmaller == true)
    {
        int carry = 1;
        i = mid - 1;
        if (n%2 == 1)
        {
            num[mid] += carry;
            carry = num[mid] / 10;
            num[mid] %= 10;
            j = mid + 1;
        }
        else
            j = mid;
        while (i >= 0)
        {
            num[i] += carry;
            carry = num[i] / 10;
            num[i] %= 10;
            num[j++] = num[i--];
        }
     }
}
void swap(int *a, int *b)
{
    *a = *a ^ *b;
    *b = *b ^ *a;
    *a = *a ^ *b;
}

void reverse_arr(int length)
{
    int i=0, j = length - 1;
    while (i < j) {
	swap(&arr[i], &arr[j]);
	i++; j--;
    }
}

int convert_to_int_arr(unsigned long long num)
{
    memset(arr, 0, sizeof(arr));
    int dig, k=0;
    while (num > 0) {
	dig = num % 10;
	arr[k++] = dig;
	num = num/10;
    }
    reverse_arr(k);
    return k;
}
unsigned long long generateNextPalindrome( unsigned long long number )
{
         
         int n = convert_to_int_arr(number);
    int i;
    //printf("\nNext palindrome is:\n");
    if( AreAll9s( arr, n ) )
    {
        unsigned long long num9;
        stringstream ss;
       // printf( "1 ");
        ss << "1";
        for( i = 1; i < n; i++ )
        {
         // printf( "0 " );
          ss <<"0";
        }
          //printf( "1" );
          ss <<"1";
          ss >> num9;
          return num9;
    }
    else
    {
       generateNextPalindromeUtil ( arr, n );
       unsigned long long num1 = printArray (arr, n);
       return num1;
    }
}
int AreAll9s( int* num, int n )
{
    int i;
    for( i = 0; i < n; ++i )
      if( num[i] != 9 )
        return 0;
    return 1;
}
unsigned long long printArray(int arr[], int n)
{
    int i;
    std::stringstream  ss;
    unsigned long long num;
    for (i=0; i < n; i++)
    {
    // printf("%d ", arr[i]);
     ss << arr[i];
    }
    // printf("\n");
     
    
    ss >> num; 
    return num;
}

bool isPalUtil(unsigned long long num, unsigned long long* dupNum)
{
   if (oneDigit(num))
        return (num == (*dupNum) % 10);
    if (!isPalUtil(num/10, dupNum))
        return false;
    *dupNum /= 10;
    return (num % 10 == (*dupNum) % 10);
}
bool isPalin(unsigned long long num)
{     
    unsigned long long *dupNum = new unsigned long long(num);
    return isPalUtil(num, dupNum);
}


int main(){
    int T;
    int count =0;
    unsigned long long lowRange;
    unsigned long long highRange;
    char *end;
    int numLow[16];
    unsigned long long high;
    freopen("C-small-attempt2.in", "r", stdin);
    freopen("C-small-attempt2.out", "w", stdout);
    scanf("%d", &T);
    // cout <<T<<endl;
     
    for (int i=1;i<=T;i++)
      {  
               count = 0;
               cin >> lowRange >> highRange ;
               //scanf("%d %d", &lowRange, &highRange);
               //cout <<lowRange <<"---"<<highRange<<endl;

               if(isPerfectSquare(lowRange))
               {
                 unsigned long long sq = (long long) sqrt(lowRange);
                 if (isPalin(sq))
                   count++;         
               }
               
               while (1)
               {
                   //lowRange = lowRange -1;  
                   
                   unsigned long long p = generateNextPalindrome(lowRange);
            //       fprintf(stderr,"Palindorme: %d\n", p);
                   lowRange = p;
                   if (p > highRange)
                     break;
                   else
                     {
                       if(isPerfectSquare(p))
                       {
                         unsigned long long sq = (long long) sqrt(p);
                         if (isPalin(sq))
                           count++;         
                       }
                               
                     }           
               }
               
               //fprintf(stderr, "Case #%d: %d\n", i,count);
               //fprintf(stderr,"Case #%d: ", lowRange);
               //fprintf(stderr,"Case #%d: ", highRange);
      
               printf("Case #%d: %d\n", i,count);
               //printf("Case #%d: ", lowRange);
               //printf("Case #%d: ", highRange);
      
//               cout <<T<<" "<<lowRange<<" "<<highRange<<endl;
      }
    
}

