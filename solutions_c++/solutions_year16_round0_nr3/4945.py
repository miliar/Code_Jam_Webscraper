#include<bits/stdc++.h>
#include <algorithm>
#define ll long long

using namespace std;

void coinjam(int x, int N){
    string s1 = "";
    long long arr[9] = {0, 0, 0, 0, 0, 0, 0, 0, 0};
    long long power[9] = {1, 1, 1, 1, 1, 1, 1, 1, 1};
    while(x > 0){
        for(int i = 0; i < 9; i++)
            power[i]*= (i+2);
        if(x%2 == 0)
            s1 = '0' + s1; 
        else{
            s1 = '1' + s1;
            for(int i = 0; i < 9; i++){
                arr[i] += power[i];
            }
        }
        x /= 2;
    }
    int y = (N / 2) - s1.size() - 1;
    cout << "1" << s1.substr(1) + "1" + string(y, '0') + string(y, '0') + s1 + "1";
    for(int i = 0; i < 9; i++){
       cout << " " << arr[i] + 1;
    }
    cout << endl;
}

int main(){
    int T, N, J, i;
    cin >> T;
    i = 0;
    while (i < T){
        i++;
        cin >> N >> J;
        T--;
        cout << "Case #" << i << ":" << endl;
        for (int k = 1; k <= J; k++){
            coinjam(k, N);
        }
    }
    return 0;
}
