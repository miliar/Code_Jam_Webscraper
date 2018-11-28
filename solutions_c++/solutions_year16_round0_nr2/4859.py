#include <iostream>
#include <string>

using namespace std;

int GetNumberMoves(string current)
{
    int firstPlus = 0, lastMinus = current.size() - 1;
    for (; firstPlus < current.size() && current[firstPlus] != '+'; ++firstPlus)
        ;
    
    for (; lastMinus >= 0 && current[lastMinus] != '-'; --lastMinus)
        ;
    
    // Were no minus
    if (lastMinus < 0)
        return 0;
    
    // Can all be flipped at once
    if (lastMinus < firstPlus)
        return 1;
    
    int numMoves = 1;
    
    if (current[0] == '+')
    {
        ++numMoves;
        
        // Invert the front
        for (int i = 0; current[i] == '+'; ++i)
            current[i] = '-';
    }
    
    string newString(current);
    for (int i = 0; i <= lastMinus; ++i)
    {
        newString[i] = (current[lastMinus - i] == '+') ? '-' : '+';
    }
    
    return GetNumberMoves(newString) + numMoves;
}


int main()
{
    int T;
    cin >> T;
    
    for (int t = 1; t <= T; ++t)
    {
        string start;
        cin >> start;
        
        cout << "Case #" << t << ": " << GetNumberMoves(start) << '\n';
    }
}