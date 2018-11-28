#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;

int main(){
    int runs, N, m1, m2, rate, arr[10001];
    int i, j;
    cin>>runs;
    for(j=1; j<=runs; j++){
        cin>>N;
        rate = 0;
        cin>>arr[0];
        rate = 0;
        for(i=1;i<N;i++){
            cin>>arr[i];
            rate = max(arr[i-1] - arr[i], rate);
        }
        m1=0;
        m2=0;
        for(i=1;i<N;i++){
            if(arr[i] < arr[i-1])
                m1+=(arr[i-1] - arr[i]);
            m2 += (arr[i-1] - rate) > 0 ? rate : arr[i-1];
        }
        printf("Case #%d: %d %d\n", j, m1, m2);
    }
}
