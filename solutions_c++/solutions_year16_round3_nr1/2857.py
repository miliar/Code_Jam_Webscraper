#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stack>
#include <queue>
#include <cstdlib>
#include <stdlib.h>
#include <limits.h>
#include <algorithm>
#include <time.h>
using namespace std;

typedef long long int lld;

const double PI  =3.141592653589793238463;
const float  PI_F=3.14159265358979f;

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

int comparel (const void * a, const void * b)
{
    if( *(long long int*)a - *(long long int*)b < 0 )
        return -1;
    if( *(long long int*)a - *(long long int*)b > 0 )
        return 1;
    if( *(long long int*)a - *(long long int*)b == 0 )
        return 0;
}


typedef struct{
    int letter;
    int times;
}letter;

int comparefunc(const void * a,const void *b){
    letter *pa= (letter*) a;
    letter *pb= (letter*) b;

    return (pb->times - pa->times);
}

int testcompare(const void *a, const void*b){
    return (*(int*)a-*(int*)b);
}

typedef struct{
    int val;
}tester;

int structcompare(const void *a, const void *b){

    tester *ta=(tester*) a;
    tester *tb=(tester*) b;

    return (ta->val-tb->val);
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
    for (int x=0;x<t;x++){
        printf("Case #%d: ",x+1);
        fprintf(fptr,"Case #%d: ",x+1);
        int n;
        scanf("%d",&n);
        int arr[n];
        for (int i=0;i<n;i++) scanf("%d",&arr[i]);
        
        int sum=0;
        for (int i=0;i<n;i++){
            sum+=arr[i];
        }
        
        while (sum!=0){
        int max=0;
        int maxindex=0;
        for (int i=0;i<n;i++){
            if (arr[i]>max){
                max=arr[i];
                maxindex=i;
            }
        }
        
        printf("%c",'A'+maxindex);
        fprintf(fptr,"%c",'A'+maxindex);
        arr[maxindex]--;
        sum--;
        max=0;
        for (int i=0;i<n;i++){
            if (arr[i]>max){
                max=arr[i];
                maxindex=i;
            }
        }
        if (max>sum/2){
            printf("%c",'A'+maxindex);
            fprintf(fptr,"%c",'A'+maxindex);
            arr[maxindex]--;
            sum--;
        }
        
        if (sum==0) {
            printf("\n");
            fprintf(fptr,"\n");
        }
        else {
            printf(" ");
            fprintf(fptr," ");
        }
        }
    }
}

