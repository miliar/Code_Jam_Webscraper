/*===============================================================
*   Copyright (C) 2013 All rights reserved.
*   
*   file: C.cpp
*   author: ivapple
*   date: 2013-04-13
*   description: 
*
*   update log: 
*
================================================================*/
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cstring>

#include <iostream>

#define out(x) (cout<<#x<<": "<<x<<endl)

#define FOR(i,s,t) for(i=s; i<t; i++)

using namespace std;

template<class T>void show(T a, int n){int i; for(i=0;i<n;i++)cout<<a[i]<<" ";cout<<endl;}

template<class T>void show(T a, int r, int l){int i; for(i=0;i<r;i++)show(a[i],l);cout<<endl;}

int itoa(int val, char* buf)
{

    const int radix = 10;

    char* p;
    int a;        //every digit
    int len;
    char* b;    //start of the digit char
    char temp;

    p = buf;

    if (val < 0)
    {
        *p++ = '-';
        val = 0 - val;
    }

    b = p;

    do
    {
        a = val % radix;
        val /= radix;

        *p++ = a + '0';

    } while (val > 0);

    len = (int)(p - buf);

    *p-- = 0;

    //swap
    do
    {
        temp = *p;
        *p = *b;
        *b = temp;
        --p;
        ++b;

    } while (b < p);

    return len;
}

const int MAXX = 1000;
int T;
bool result[MAXX+1];
bool ispalindrome[MAXX+1];
char str[10];
int A, B;

bool ispal(int num)
{
  int len;
  itoa(num, str);
  len = strlen(str);
  int i;
  for (i=0; i<len/2; i++)
  {
    if (str[i] != str[len-1-i])
      return 0;
  }
  return 1;
}

void init()
{
  int i;
  for (i=0; i<=MAXX; i++)
  {
    if (ispal(i))
      ispalindrome[i]=1;
  }
  for (i=0; i<=int(sqrt(MAXX)); i++)
  {
    if (ispalindrome[i] && ispalindrome[i*i])
    {
      result[i*i] = 1;
    }
  }
}

int solve(int s, int e)
{
  int i;
  int sum = 0;
  for (i=s; i<=e; i++)
  {
    sum += result[i];
  }
  return sum;
}

int main()
{
  int t = 1;
  int re;
  freopen("C-small-attempt0.in", "r", stdin);
  freopen("C-small.out", "w", stdout);
  scanf("%d", &T);
  init();
  t = 1;
  while (T--)
  {
    scanf("%d%d", &A, &B);
    printf("Case #%d: ", t);
    re = solve(A,B);
    printf("%d\n", re);    
    t++;
  }
  return 0;
}





