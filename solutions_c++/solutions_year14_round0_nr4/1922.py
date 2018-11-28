#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int dwar(int n, double* naomi, double* ken){
    int start = 0;
    int end = n-1;
    int ans = 0;
    for(int i = n-1; i >= 0; i--){
        if(naomi[i] < ken[end]){
            start++;
        }
        else if(naomi[i] > ken[end]){
            ans++;
            end--;
        }
    }
    return ans;
}

int war(int n, double* naomi, double* ken){
    int start = 0;
    int end = n-1;
    int ans = 0;
    for(int i = 0; i < n; i++){
        if(naomi[i] < ken[start]){
            start++;
        }
        else if(naomi[i] > ken[start]){
            ans++;
            end--;
        }
    }
    return ans;
}


int main(){

    int t;
    cin >> t;
    for(int k = 0; k < t; k++){
        int n;
        cin >> n;
        double naomi[n], ken[n];
        for(int i = 0; i <n ;i++) cin >> naomi[i];
        for(int i = 0; i <n ;i++) cin >> ken[i];
        sort(naomi, naomi+n);
        reverse(naomi, naomi+n);
        sort(ken, ken+n);
        reverse(ken, ken+n);
        cout << "Case #" << k+1 << ": " << dwar(n, naomi, ken) << " " << war(n, naomi, ken)  << endl;

    }
    return 0;
}
