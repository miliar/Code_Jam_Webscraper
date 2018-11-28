#include<bits/stdc++.h>
#include <algorithm>
#define ll long long

using namespace std;

bool arr[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0};

int get_count(int N){
    while(N > 0){
        arr[N%10] = 1;
        N /= 10;
    }
    int sum = 0;
    for(int i = 0; i < 10; i++){
        if(arr[i] == 1) sum +=1;
    }
    //cout << "sum : " << sum << endl;
    return sum;
}

long long get_result(int N){
    int result = N;
    int i = 1;
    while(1){
        //cout << "result : " << result << endl;
        i++;
        if (get_count(result) == 10)break;
        result = N * i;
    }
    return result;
}

int main(){
    int T, N, i;
    cin >> T;
    i = 0;
    while (i < T){
        i++;
        cin >> N;
        for(int i = 0; i < 10; i++) arr[i] = 0;
        if (N == 0)cout << "Case #" << i << ": INSOMNIA" << endl;
        else cout << "Case #" << i << ": " << get_result(N) << endl;
    }
    return 0;
}
