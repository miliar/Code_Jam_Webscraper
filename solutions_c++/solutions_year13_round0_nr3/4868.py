#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
using namespace std;

bool isPalindrom(int num){
    char str[100];
    itoa(num, str, 10);
    string s(str);
    string sReverse;
    sReverse.resize(s.size());
    for (int i=0;i<s.length();i++){
        sReverse[i] = s[s.length()-1-i];
    }
    if (sReverse == s)
        return true;
    else
        return false;
}

int solve(){
    int A,B;
    cin >> A >> B;
    int result = 0;
    int min = sqrt(A);
    int max = sqrt(B);
    for (int i=min;i<=max;i++){
        if (!isPalindrom(i))
            continue;
        int square = i*i;
        if (square < A)
            continue;
        if (square > B)
            break;
        if (isPalindrom(square)){
            result++;
        }
    }
    return result;
}

int main(int argc, char *argv[])
{
    int n;
    cin >> n;
    for (int i=1; i<=n;i++){
        cout << "Case #" << i << ": " << solve() << endl;
    }
    return 0;
}
