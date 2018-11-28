#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<iostream>

#define EPSILON 0.000000000001

using namespace std;

double a[1000],b[1000];
int n;

int compare(const void *a,const void *b){
    /*if (*(double*)a-*(double*)b<EPSILON && fabs(*(double*)a-*(double*)b)<EPSILON) return -1;
    else if (*(double*)a-*(double*)b>EPSILON && fabs(*(double*)a-*(double*)b)>EPSILON) return 1;*/
    const double *da=(const double *) a;
    const double *db=(const double *) b;
    return (*da < *db)-(*da > *db);
}

int deceitfulwar(void){
    int i=0,j=0,c=n;
    while(i<n&&j<n){
        while(a[i]<b[j]&&j<n){
            --c;
            ++j;
        }
        ++i;
        ++j;
    }
    return c;
}

int realwar(void){
    int i=n-1,j=n-1,c=0;
    while(i>=0&&j>=0){
        while(a[i]>b[j]&&j>=0){
            ++c;
            --j;
        }
        --i;
        --j;
    }
    return c;
}

int main(){
    int t,ccase=1;
    scanf("%d",&t);
    while(t--){
        scanf("%d",&n);
        for(int i=0;i<n;i++)
            scanf("%lf",&a[i]);
        for(int i=0;i<n;i++)
            scanf("%lf",&b[i]);
        qsort(a,n,sizeof(a[0]),compare);
        qsort(b,n,sizeof(b[0]),compare);
        printf("Case #%d: %d %d\n",ccase,deceitfulwar(),realwar());
        /*for(int i=0;i<n;i++)
            printf("%.3lf ",a[i]);
        printf("\n");
        for(int i=0;i<n;i++)
            printf("%.3lf ",b[i]);*/
        ++ccase;
    }
    return 0;
}
