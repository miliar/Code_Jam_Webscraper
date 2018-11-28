#include<stdio.h>
#include<iostream>
using namespace std;
int N = 0;

int war(float a[], float b[], int n){
    int valid2[n];

    for(int i=0; i<n; i++)
        valid2[i] = 0;
    int naomi_cnt = 0;
    for(int i=0; i<N; i++){
        float naomi = a[i];
        int state = 0;
        for(int j=0; j<N; j++){
            if(b[j] > naomi && valid2[j] == 0){
                valid2[j] = 1;
                state = 1;
                break;
            }
        }
        if(state == 0)
            naomi_cnt++;
    } 
    return naomi_cnt;
}
int deceitfulwar(float a[], float b[], int n){
    int ptr1 = 0, ptr2 = N-1;
    int naomi_cnt = 0;
    int valid1[n], valid2[n];
    for(int i=0; i<n; i++){ valid1[i] = valid2[i] = 0;}
    
    for(int i=0; i<N; i++){
        if(a[i] > b[ptr1]){
            naomi_cnt++; ptr1++;
        }
        else{
            ptr2--;
        }    
    }
    return naomi_cnt;
}
int main(){
    int cases, n, ans1, ans2;
    scanf("%d", &cases);
    for(int t=1; t<= cases; t++){
        scanf("%d", &n);
        float a[n], b[n];
        N = n;
        for(int i=0; i<n; i++){
            scanf("%f", &a[i]);
        }
        for(int i=0; i<n; i++){
            scanf("%f", &b[i]);
        }
        sort(a, a + N);
        sort(b, b + N);
        ans1 = war(a, b, n);
        ans2 = deceitfulwar(a,b, n);
        printf("case #%d: %d %d\n", t, ans2, ans1);
    }
}
