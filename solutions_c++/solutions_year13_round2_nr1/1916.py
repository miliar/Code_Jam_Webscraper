#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int v[1000000 + 7];

int main() {

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int tests;
    cin >> tests;
    for(int i2 = 0; i2 < tests; i2++)
    {
        int sizeA, n;
        cin >> sizeA >> n;
        for(int i = 0; i < n; i++){
            cin >> v[i];
        }
        sort(v, v + n);
        int idLast = 0;
        int answer = n;
        int current = 0;
        for(int i = 0; i < n; i++)
        {
            if(v[i] < sizeA){
                idLast++;
                sizeA += v[i];
              // cout << "give" << sizeA << endl;
            } else {
                if ((n - i + current) < answer) {
                //    cout << "answer : " << answer << endl;
                    answer = n - i + current;
                }
                if(sizeA > 1) {
                    idLast++;
                    int del = 0;

                    while(sizeA <= v[i]){
                        sizeA += sizeA - 1;
                        del++;
                    }
                    sizeA += v[i];
                    current += del;
                    //sizeA += del * (sizeA-1) + v[i];
                } else {
                    break;
                }
            }
        }
        if(idLast == n){
            if (answer == -1 || (current) < answer) {
                    answer =  current;
            }
        }
        cout << "Case #" << i2 + 1<<": " ;
        cout << answer << endl;
    }
    return 0;
}
