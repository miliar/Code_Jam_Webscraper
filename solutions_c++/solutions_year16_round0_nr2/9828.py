#include <iostream>
#include <fstream>
#include <cstring>

using namespace std;

bool arr[200];


void reverse(int x){
    bool duplicate[200];
    for (int i = 0; i < 200; i++) duplicate[i] = arr[i];

    for (int i = 0; i <= x; i++){
        arr[i] = !duplicate[x-i];
    }
}

void print(int n){
    for (int i = 0; i < n; i++){
        cout << (arr[i] == true ? '+' : '-');
    }
    cout << endl;
}

bool allMinus(int n){
    for (int i = 0; i < n; i++){
        if (arr[i] == true) return false;
    }
    return true;
}

bool allPlus(int n){
    for (int i = 0; i < n; i++){
        if (arr[i] == false) return false;
    }
    return true;
}

int answer(string s){
    int len = s.length();
    for (int i = 0; i < len; i++){
        arr[i] = s[i] == '+' ? true: false;
    }

    int count = 0;


    while (true){
        for (int i = 0; i < len-1; i++){
            if (arr[i] != arr[i+1]){
                reverse(i);
                count++;
                break;
            }
        }

        if (allPlus(len)) break;
        else if (allMinus(len)){
            count++;
            break;
        }
    }

    return count;
}

int main(){
    ifstream cin("input.txt");
    ofstream cout("output.txt");

    int t;
    cin >> t;
    for (int i = 0; i < t; i++){
        string s;
        cin >> s;
        cout << "Case #" << (i+1) << ": " << answer(s) << endl;
    }
    return 0;
}
