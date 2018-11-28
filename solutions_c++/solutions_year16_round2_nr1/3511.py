#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <array>
#include <string>
using namespace std;

array<char, 256> occur;
array<int, 10> numbers;

string numtostr[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

void getnums(int num, char identchar){
    while (occur[identchar]){
        numbers[num]++;
        for(char c : numtostr[num])
            occur[c]--;
    }
}

int main() {
    int N;
    cin >> N;
    for(int C = 1; C <= N; C++){
        occur.fill(0);
        numbers.fill(0);
        string str, res;
        cin >> str;
        
        for(char c : str)
            occur[c]++;

        getnums(0,'Z');
        getnums(2,'W');
        getnums(6,'X');
        getnums(7,'S');
        getnums(8,'G');
        getnums(5,'V');
        getnums(4,'F');
        getnums(3,'R');
        getnums(9,'I');
        getnums(1,'O');
        
        for(int i = 0; i < 10; i++)
            //cout << numbers[i] << endl;
            res += string(numbers[i], '0'+i);
        
        cout << "Case #" << C << ": " << res << endl;
    }
    return 0;
}
