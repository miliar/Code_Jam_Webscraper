#include <iostream>
#include <string>

using namespace std;

int main()
{
    int T;
    cin >> T;
    
    string str;
    
    for (int t = 1; t <= T; ++t)
    {
        int size;
        cin >> size >> str;
        
        int total = 0, friends = 0;
        for (int i = 0; i <= size; ++i)
        {
            if (total < i && str[i] != '0')
            {
                friends += i - total;
                total = i;
            }
            
            total += str[i] - '0';
        }
        
        cout << "Case #" << t << ": " << friends << '\n';
    }
}