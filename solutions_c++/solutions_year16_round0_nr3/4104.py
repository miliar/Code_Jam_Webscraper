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

void printarray (lld arr[],lld len){
    if (len!=0){
    for (int i=0;i<len-1;i++){
        printf("%lld ",arr[i]);
    }
    printf("%lld\n",arr[len-1]);
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


lld arrp[10];


lld isprime(lld k,int base){
    lld lim=pow(k,0.5);
//    printf("  %lld  ",lim);
    for (lld i=2;i<=lim;i++){
        if (k%i==0) {
            arrp[base-2]= i;
            return 0;
        }
    }
    return 1;
}

lld tobase(lld n,lld base){
//    lld len=log10(n)+1;
    lld ans=0;
    lld s[200];
    for (int i=0;i<200;i++) s[i]=0;
    int curr=0;
    while (n>0){
        s[curr]=n%base;
        n/=base;
        curr++;
    }
//    printf(" curr %d ", curr);
    int count=0;
    for (int i=0;i<curr;i++){
        ans+=s[i]*pow(10,count);
        count++;
    }
    
    return ans;
}

lld tonum(lld n,lld base){
    lld len=log10(n)+1;
    lld ans=0;
    lld curr=1;
    for (lld i=0;i<len;i++){
        ans+=n%10*curr;
        curr*=base;
        n/=10;
    }
    return ans;
}


int main(){
//    ans[0]=99;
    FILE *fptr;
   fptr=fopen("/Users/Jeffrey/Desktop/q3.txt","w");
    if(fptr==NULL){
      printf("Error!");
      exit(1);
   }
   
   printf("Case #1:\n");
   fprintf(fptr,"Case #1:\n");
   lld n=6;
   lld j=50;
   
   for (lld i=32769;i<=65536;i+=2){
//    for (lld i=33;i<=64;i+=2){   
       int br=0;
       lld t=tobase(i,2);
       for (lld j=2;j<=10;j++){
           lld k=tonum(t,j);
           if (isprime(k,j)==1){
               br=1;
               break;
           }
       }
       
       if (br==0){
           printf("%lld ",tobase(i,2));
           fprintf(fptr,"%lld ",tobase(i,2));
           for (int q=0;q<9;q++){
               printf("%lld",arrp[q]);
               fprintf(fptr,"%lld",arrp[q]);
               
               if (q!=9-1) printf(" ");
               else printf("\n");
               
               if (q!=9-1) fprintf(fptr," ");
               else fprintf(fptr,"\n");
               
           }
//           printarray(arrp,9);
           
       j--;
       
       if (j==0) break;
       }
   }
   fclose(fptr);
}