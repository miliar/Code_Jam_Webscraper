#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <stdio.h>
using namespace std;


int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int limit;
    cin >> limit;
    for (int i=0;i<limit;i++){
        int lettersCount;
        string text;
        cin >> lettersCount >> text;
        int result = 0 , total = 0;
        for (int j = 0 ; j < text.length();j++){
            if (j > total && text[j] - '0' !=0){
                result += j - total;
                total = j + text[j] - '0';
            }
            else{
                total += text[j] - '0';
            }
        }
        cout <<"Case #"<< i+1 << ": " <<result<< endl;
    }
    return 0;
}
