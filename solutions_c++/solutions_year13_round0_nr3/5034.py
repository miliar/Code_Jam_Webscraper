#include <iostream>
#include <vector>
#include <string>
#include <cmath>

using namespace std;

bool isPalindrome(long long n) {

    vector<int> vi;
    do {
        vi.push_back(n % 10);
    } while((n /= 10) != 0);
    for(int i = 0; i < vi.size() / 2; i++) {
        if(vi[i] != vi[vi.size() - i - 1])
            return false;
    }
    return true;
}  

int searchFSPalindrome(long long nMin, long long nMax) {
    int count = 0;
    nMin = (long long)(ceil(sqrt(nMin)));
    nMax = (long long)(floor(sqrt(nMax)));
    for(int k = nMin; k <= nMax; k++) {
        if(isPalindrome(k) && isPalindrome(k * k))
            count++; 
    }
    return count;
}

int main() {
    string stmp;
    int noTests, nMin, nMax;
    cin >> noTests;
    getline(cin, stmp);
    for(int i = 0; i < noTests; i++) {
        cin >> nMin >> nMax;
        getline(cin, stmp);
        cout << "Case #" << i + 1 << ": " << searchFSPalindrome(nMin, nMax) << endl;
    }
}

