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
   fptr=fopen("/Users/Jeffrey/Desktop/q1.txt","w");
    if(fptr==NULL){
      printf("Error!");
      exit(1);
   }
    
    int t;
    scanf("%d",&t);
    for (int z=0;z<t;z++){
        lld n;
        scanf("%lld",&n);
        int arr[10];
        for (int i=0;i<10;i++) arr[i]=0;
        int printed=0;
        for (lld i=1;i<10000;i++){
            lld k=n*i;
            lld orig=k;
            double p=log10(k);
            int len=((int) p) +1;
            
            
            for (int j=0;j<len;j++){
//            printf("%d",k%10);
                arr[k%10]++;
            k/=10;
        }
        
            int corr=1;
            for (int i=0;i<10;i++){
                if (arr[i]==0) corr=0;
            }
            if (corr){
                printf("CASE #%d: %lld\n",z+1,orig);
                
                fprintf(fptr,"CASE #%d: %lld\n",z+1,orig);
                printed=1;
                break;
            }
        }
        if (printed==0){
            printf("CASE #%d: INSOMNIA\n",z+1);
            
            fprintf(fptr,"CASE #%d: INSOMNIA\n",z+1);
        }
    }
    fclose(fptr);
}