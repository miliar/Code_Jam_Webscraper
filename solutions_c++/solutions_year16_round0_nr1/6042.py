#include <iostream>
using namespace std;

int bleatrix(int N);

int main() {
    int numTests;
    int num;
    cin >> numTests;
    
    for (int i = 1; i <= numTests; i++)
    {
        cin >> num;
        cout << "Case #" << i << ": ";
        
        int ans = bleatrix(num);
        
        if (ans != 0)
            cout << ans;
        
        cout << endl;
    }
}

int bleatrix(int N)
{
    if (N == 0)
    {
        cout << "INSOMNIA";
        return 0;
    }
    
    bool digits[10];
    
    for (int i = 0; i < 10; i++)
        digits[i] = false;
    
    int count = 1;
    
    while (true)
    {
        int numToCheck = count * N;
        int numToMan = numToCheck;
        int digit;
        
        while(numToMan != 0)
        {
            digit = numToMan%10;
            digits[digit] = true;
            numToMan = numToMan/10;
        }
        
        bool allTrue = true;
        for (int i = 0; i < 10; i++)
            if (!digits[i])
                allTrue = false;
        
        if (allTrue)
            return numToCheck;
        count++;
    }
}