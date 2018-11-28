#include<iostream>
#include<cstdlib>
using namespace std;

int comp(const void *arr1, const void *arr2) {
    double a = *(double *)arr1, b = *(double *)arr2;
    return (a - b) > 0.0 ? 1 : 0;
}

int main() {
    int T;
    double arr1[1000], arr2[1000];
    
    cin>>T;
    for (int num = 1; num <= T; ++ num) {
        int score_d = 0, score_w = 0;
        int N;
        cin>>N;
        for (int i = 0; i < N; ++ i) {
            cin>>arr1[i];
        }
        for (int i = 0; i < N; ++ i) {
            cin>>arr2[i];
        }
        
        qsort(arr1, N, sizeof(double), comp);
        qsort(arr2, N, sizeof(double), comp);
        
        int i = N - 1, j = N -1 ;
        score_w = N;
        while (i >= 0 && j >= 0) {
            if (arr2[j] >= arr1[i]) {
                -- score_w;
                -- i;
                -- j;
            } else {
                -- i;
            }
        }
        
        i = N - 1; j = N - 1;
        while (i >= 0 && j >= 0) {
            if (arr1[i] > arr2[j]) {
                ++ score_d;
                -- i;
                -- j;
            } else {
                -- j;
            }
        }
        
        cout<<"Case #"<<num<<": "<<score_d<<" "<<score_w<<endl;
    }
}
