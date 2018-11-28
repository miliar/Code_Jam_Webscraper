#include <cstdlib>
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

bool isPalindrome(int x)
{
     vector<int> digits;
     while(x > 0){
             digits.push_back(x % 10);
             x /= 10;
     }
     for(int i = 0; i < digits.size(); i++)
             if(digits[i] != digits[digits.size() - 1 - i]) return false;
     return true;
}

int main(int argc, char *argv[])
{
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    for(int x = 1; x <= 100; x++){
            int a, b;
            cin >> a >> b;
            int k = 0;
            for(int i = a; i <= b; i++)
                    if((int)sqrt(i) == sqrt(i) && isPalindrome(i) && isPalindrome(sqrt(i)))
                                    k++;
            cout << "Case #" << x << ": " << k << endl;
    }
    return EXIT_SUCCESS;
}
