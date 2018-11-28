#include <iostream>
#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
double data1[1005], data2[1005];
int solve(double a[], double b[], int n){
    int begin = 0, end = n - 1, win = 0;
    for(int i = 0; i < n; i++){
        if(a[i] < b[begin]){
            end--;
        }
        else{
            begin++;
            win++;
        }
    }
    return win;
}
int main()
{
    freopen("D-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T, cas = 0;
    scanf("%d", &T);
    while(T--){
        printf("Case #%d: ", ++cas);
        int N;
        scanf("%d", &N);
        for(int i = 0; i < N; i++){
            scanf("%lf", &(data1[i]));
            //cout << data1[i] << " ";
        }
        //cout << endl;
        for(int i = 0; i < N; i++){
            scanf("%lf", &(data2[i]));
            //cout << data2[i] << " ";
        }
        //cout << endl;
        sort(data1, data1 + N);
        sort(data2, data2 + N);
        cout << solve(data1, data2, N) << " ";
        cout << N - solve(data2, data1, N) << endl;
    }
    return 0;
}
