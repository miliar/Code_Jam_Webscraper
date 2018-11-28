#include <iostream>
#include <bits/stdc++.h>
#include <bitset>
#include <cmath>

 using namespace std;
            
 //bool isPrime(long int val, long int &div)
 bool isPrime(long long val, long long &div)
 {
   long long i,sqt,count=0;

   if( (val == 1) || (val == 2))
     return true;

   if(val%2 == 0) {
    div = 2;
    return false;
   }

   sqt=sqrt(val);

   for(i=2; i<=sqt; i++)
   {
     if(val%i==0) {
       div = i;
       return false;
     }
   }

   return true;
 }


long long ipow(int base, int exp)
{
  long long result = 1;
  while (exp)
  {
    if (exp & 1)
      result *= base;
    exp >>= 1;
    base *= base;
  }

  return result;
}

int main()
{
  int numInps = 1, base = 2;
  long long input = 0;
  int j = 0;
  int N = 0, J = 0;
  long long new_num = 0, new_num_max = 0, div_num = 0;
  //const int size= 6;
  //int number[size];
  long long  array_div[11];
  bool is_prime = false;
  long long conNum = 0;
  int counter=0;
  int totalCount = 0;
  long long  newGenNum = 0;
  int m = 0;
  //const int n = ipow(2, size);
  //bool prime[n+1];

  //SieveOfEratosthenes(n, prime);

  //memset(number, 0 ,size*sizeof(int));
  //number[0]=1;
  //number[size]=1;

  cin>>numInps;

  cin>>N>>J;

  input = (1<<(N-1))|1;
  for(j=1; j<(N-2);j++)
  {
    new_num = (new_num<<1)|1;
  }
  new_num_max = new_num;
  new_num = 0; newGenNum = input;
  cout<<"Case #1:"<<endl;
  do 
  {
   conNum = 0;
   counter=0;
   newGenNum = (input)| (new_num<<1);
   new_num += 1;
   for (base = 2; base <= 10; ++base) {
    long long data = newGenNum;
    conNum=0;
    for(m=0; m<N;m++)
    {
     conNum += ipow(base,m)*(data&0x1);
     data = data>>1;
    }
    /* check conNum is a prime or not */
    is_prime = isPrime(conNum, div_num);
    array_div[base] = div_num;
    //array_base[base] = conNum;
    if(is_prime)
    {
     break;
    }
    else
    {
     counter++;
    }
   } 
    
   if (counter == 9) {
    totalCount++;
    cout<<conNum;
    for (int iter = 2; iter <=10; ++iter) {
     cout<<" "<<array_div[iter];
    }
    cout<<endl;
   }
   if (totalCount == J) {
    break;
   }

  } while(new_num<=new_num_max);

  return 0;
}
