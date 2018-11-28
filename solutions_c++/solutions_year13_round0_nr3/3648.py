#include <iostream>
#include <cstdio>
#include <string>
#include <cmath>
#include <sstream>

using namespace std;

bool isPalindrome(int num)
{
    ostringstream ostr;
    ostr << num;

    string numStr = ostr.str();
    int strLen = numStr.size();
    for (int i = 0; i < strLen; ++i) 
    {
        if (numStr[i] != numStr[strLen - i - 1] )
            return false;
    }
    return true;
}

int main()
{
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++ )
    {
        int count = 0;
        int A, B;
        cin >> A >> B;

        int minSqrt = (int)sqrt((double)(A-1)) + 1;
        int maxSqrt = (int)sqrt((double)B);

        for (int j = minSqrt; j <= maxSqrt; ++j)
            if ( isPalindrome(j) && isPalindrome(j*j) )
                count++;

        printf("Case #%d: %d\n", i, count);
    }
}
