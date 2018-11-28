#include <stdio.h>
#include <string.h>
#include <math.h> 
#include <stack>
#include <queue>
#include <cstdlib>
#include <stdlib.h>
//#include <bits/stdc++.h>
using namespace std;

#define MIN(X, Y) (((X) < (Y)) ? (X) : (Y))
#define MAX(X, Y) (((X) > (Y)) ? (X) : (Y))


//#define VAR(a, b) __typeof(b) a = (b)
//#define FOR(i, a, b) for(VAR(i, a); i != (b); ++i)

//using namespace std;

typedef long long int lld;

const double PI  =3.141592653589793238463;
const float  PI_F=3.14159265358979f;


int contains(int arr[],int len,int search){
    for (int i=0;i<len;i++){
        if (arr[i]==search) return 1;
    }
    return 0;
}

void printarray (int arr[],int len){
    if (len!=0){
    for (int i=0;i<len-1;i++){
        printf("%d ",arr[i]);
    }
    printf("%d\n",arr[len-1]);
    }
}

void swap (int *a,int *b){
    int k=*a;
    *a=*b;
    *b=k;
}

int bsearch(int arr[],int len,int search){
    int first,last,middle;
    
   first = 0;
   last = len - 1;
   middle = (first+last)/2;
 
   while (first <= last) {
      if (arr[middle] < search)
         first = middle + 1;    
      else if (arr[middle] == search) {
         return 1;
         //location middle+1
         break;
      }
      else
         last = middle - 1;
 
      middle = (first + last)/2;
   }
   if (first > last)
      return 0;
}

int compare (const void * a, const void * b)
{
  return ( *(int*)b - *(int*)a );
}

int compare2 (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}

int comparec (const void * a, const void * b)
{
  return ( *(char*)a - *(char*)b );
}

int comparel (const void * a, const void * b)
{
    if( *(long long int*)a - *(long long int*)b < 0 )
        return -1;
    if( *(long long int*)a - *(long long int*)b > 0 )
        return 1;
    if( *(long long int*)a - *(long long int*)b == 0 )
        return 0;
}

int comparef (const void * a, const void * b)
{
    if( *(float*)a - *(float*)b < 0 )
        return -1;
    if( *(float*)a - *(float*)b > 0 )
        return 1;
    if( *(float*)a - *(float*)b == 0 )
        return 0;
}

int compared (const void * a, const void * b)
{
    if( *(double*)a - *(double*)b < 0 )
        return -1;
    if( *(double*)a - *(double*)b > 0 )
        return 1;
    if( *(double*)a - *(double*)b == 0 )
        return 0;
}

int asciisum(char str [], int len){
    int sum=0;
    for (int i=0;i<len;i++) sum+=(int)str[i];
    return sum;
}

int main(){
    
    FILE *fptr;
   fptr=fopen("/Users/Jeffrey/Desktop/q2.txt","w");
    if(fptr==NULL){
      printf("Error!");
      exit(1);
   }
   
   int t;
   scanf("%d",&t);
   
   for (int z=0;z<t;z++){
       char in[1000];
       scanf("%s",in);
       int len=strlen(in);
       
       int reallen=1;
       char curr=in[0];
       for (int i=1;i<len;i++){
           if (in[i]!=curr) {reallen++;
           curr=in[i];
           }
       }
//       printf("%d\n",reallen);
       int ans=reallen;
       if (in[len-1]=='+') ans--;
       printf("Case #%d: %d\n",z+1,ans);
       fprintf(fptr,"Case #%d: %d\n",z+1,ans);
   }
   
   
   
   
    fclose(fptr);
}