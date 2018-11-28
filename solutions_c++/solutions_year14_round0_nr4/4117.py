#include<stdio.h>
#define SIZ 1001

void swap(float *A, int source, int target){
    float temp;
    temp = A[source];
    A[source] = A[target];
    A[target] = temp;
}

int partition(float *A, int low, int high){
    float x = A[high];
    int i = low-1, j;
    for(j = low; j <= high; j++){
        if(A[j]<=x){
            i++;
            swap(A, i, j);
        }
    }

    return i;
}

void quick_sort(float *A, int low, int high){
    int p;
    if  (low < high){
        p = partition(A, low, high);
        quick_sort(A, low, p - 1);
        quick_sort(A, p + 1, high);
    }
}

int main(){
    int t,n,y,z;
    float  ken[SIZ], naomi[SIZ];
    scanf("%d",&t);
    for(int x=1;x<=t;x++){
        y=0; z =0;
        scanf("%d",&n);
        for(int j =0;j<n;j++)
            scanf("%f",&naomi[j]);
        for(int j =0;j<n;j++)
            scanf("%f",&ken[j]);

        quick_sort(naomi, 0, n-1);
        quick_sort(ken, 0, n-1);

        for(int i=0,j = 0;i<n;i++)
            if(naomi[i]>ken[j]){
                y++;
                j++;
            }

        for(int i=n-1,j=n-1;i>=0;i--)
            if(naomi[i]>ken[j])
                z++;
            else
                j--;
        printf("Case #%d: %d %d\n",x,y,z);
    }
    return 0;
}
