//#include <bits/stdc++.h>
#include <fstream>
#include <iostream>
using namespace std;


int main()
{
    ifstream cin("A-large.in");
    ofstream cout("salida.txt");
    int n;

    int T;
    cin >> T;
    for(int i=1; i<=T; i++){
        cin >> n;
        int cont=0, sum=0, num;
        char digit;

        for(int i=0; i<=n; i++){
            cin >> digit;
            num = digit - '0';
            if(num != 0){
                if(sum-i < 0){
                    cont += i-sum;
                    sum += i-sum;
                }
                sum += num;
            }
        }
        cout << "Case #" << i << ": " << cont << "\n";
    }
    return 0;
}
