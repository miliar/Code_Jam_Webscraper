
#include <iostream>
#include <stdio.h>
#include <cmath>

using namespace std;

bool is_pal(string& s){
    int len = s.length();
    for(int i = 0; i < len / 2; i++)
    {
        if(s[i] != s[len - i - 1])
        {
            return false;
        }
    }
    return true;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int tests;
    cin >> tests;
    for(int i2 = 0; i2 < tests; i2++)
    {
       int a, b;
       cin >> a >> b;
       int lower = (int)sqrt(a);
       int answer = 0;
       while(lower * lower <= b )
       {
           if(lower * lower >= a)
           {
                string number1 = to_string(lower);
                string number2 = to_string(lower*lower);
                if(is_pal(number1) && is_pal(number2)){
                    answer++;
                }
           }
           lower++;
       }
       cout << "Case #" << i2 + 1 << ": " << answer << endl;
    }
    return 0;
}

