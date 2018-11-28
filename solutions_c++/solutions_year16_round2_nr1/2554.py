#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

int T, tcase, N;
string S, res;

int arr[26];

inline int convert(char c) {
    return (int)(c-'A');
}

int main()
{
    cin >> T;
    tcase = 1;
    while (tcase<=T) {
        memset(arr, 0, sizeof(int)*26);
        S = "";
        res = "";

        cin >> S;
        
        for (char c : S) {
            arr[convert(c)]++;
        }

        while (arr[convert('Z')]) {
            res.append("0");
            arr[convert('Z')]--; arr[convert('E')]--; arr[convert('R')]--; arr[convert('O')]--;
        }
        while (arr[convert('W')]) {
            res.append("2");
            arr[convert('T')]--; arr[convert('W')]--; arr[convert('O')]--;
        }
        while (arr[convert('U')]) {
            res.append("4");
            arr[convert('F')]--; arr[convert('O')]--; arr[convert('U')]--; arr[convert('R')]--;
        }
        while (arr[convert('X')]) {
            res.append("6");
            arr[convert('S')]--; arr[convert('I')]--; arr[convert('X')]--;
        }
        while (arr[convert('G')]) {
            res.append("8");
            arr[convert('E')]--; arr[convert('I')]--; arr[convert('G')]--; arr[convert('H')]--; arr[convert('T')]--;
        }
        while (arr[convert('O')]) {
            res.append("1");
            arr[convert('O')]--; arr[convert('N')]--; arr[convert('E')]--;
        }
        while (arr[convert('H')]) {
            res.append("3");
            arr[convert('T')]--; arr[convert('H')]--; arr[convert('R')]--; arr[convert('E')]--; arr[convert('E')]--;
        }
        while (arr[convert('S')]) {
            res.append("7");
            arr[convert('S')]--; arr[convert('E')]--; arr[convert('V')]--; arr[convert('E')]--; arr[convert('N')]--;
        }
        while (arr[convert('V')]) {
            res.append("5");
            arr[convert('F')]--; arr[convert('I')]--; arr[convert('V')]--; arr[convert('E')]--;
        }
        while (arr[convert('I')]) {
            res.append("9");
            arr[convert('N')]--; arr[convert('I')]--; arr[convert('N')]--; arr[convert('E')]--;
        }

        sort(res.begin(), res.end());

        cout << "Case #" << tcase++ << ": " << res << endl; 
    }
}
