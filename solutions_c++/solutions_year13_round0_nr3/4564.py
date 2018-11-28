// -*- mode:c++; tab-width:4; c-basic-offset:4; indent-tabs-mode:nil -*-  
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>

using namespace std;

static char numStr[200];
bool isPalindrome(long long int n)
{
    sprintf(numStr, "%lld", n);
    int len = strlen(numStr);
    if (len == 0)
        return false;
    if (len > 1 && numStr[len-1] == '0')
        return false;
    int midpoint = len/2;
    for (int i=0; i < midpoint; i++) {
        if (numStr[i] != numStr[len-1-i])
            return false;
    }
    return true;
}

int main() {
    int n, count;
    long long int A, B, sqRoot;
    cin >> n;
    for (int i=0; i<n; i++) {
        cin >> A >> B;
        count = 0;
        for (long long li=A; li <= B; li++) {
            if (isPalindrome(li)) {
                sqRoot = sqrt(li);
                if ((sqRoot*sqRoot == li) && (isPalindrome(sqRoot)))
                    count++;
            }
        }
        cout << "Case #" << i+1 << ": " << count << endl;
    }

    return 0;
}
