#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;

int compare(int arr1[], int arr2[], int &key) {
    
    int count = 0;

    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            if (arr1[i] == arr2[j]) {
                count++;
                key = arr1[i];
            }
        }
    }
    
    return count;
}

int main() {

    int T, pos, ans, key, temp;
    int arr1[4], arr2[4];

    cin >> T;
    
    for (int i = 0; i < T; i++) {
        
        cin >> pos;
        for (int j = 1; j <= 4; j++) {
            for (int k = 0; k < 4; k++) {
                if (j == pos) {
                    cin >> arr1[k];
                }
                else {
                    cin >> temp;
                }
            }
        }
        
        cin >> pos;
        for (int j = 1; j <= 4; j++) {
            for (int k = 0; k < 4; k++) {
                if (j == pos) {
                    cin >> arr2[k];
                }
                else {
                    cin >> temp;
                }
            }
        }
        
        ans = compare(arr1, arr2, key);
        if (ans == 0) {
            printf("Case #%d: %s\n", i+1, "Volunteer cheated!");
        }
        else if (ans == 1) {
            printf("Case #%d: %d\n", i+1, key);
        }
        else { 
            printf("Case #%d: %s\n", i+1, "Bad magician!");
        }
    }

    return 0;
}
