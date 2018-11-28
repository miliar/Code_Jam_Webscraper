#include <iostream>
#include <string>
using namespace std;

int pancakes(string stack);

int main() {
    int numTests;
    string stack;
    
    cin >> numTests;
    cin.ignore(10000, '\n');

    for (int i = 1; i <= numTests; i++)
    {
        getline(cin, stack);
        cout << "Case #" << i << ": ";
        
        int ans = pancakes(stack);
    
        cout << ans << endl;
    }
}

int pancakes(string stack)
{
    int flips = 0;
    
    char rec = stack[0];
    
    for (int i = 1; i < stack.length(); i++)
    {
        if (rec != stack[i])
            flips++;
        rec = stack[i];
    }
    
    if (rec == '-')
        flips++;
    
    return flips;
}