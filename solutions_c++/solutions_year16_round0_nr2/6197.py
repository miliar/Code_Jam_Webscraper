#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>


using namespace std;

string opposite(string stack)
{
    for(int i = 0 ; i < stack.size() ; i++)
    {
        if(stack[i] == '+')
            stack[i] = '-';
        else
            stack[i] = '+';
    }

    return stack;
}

string flip(string stack)
{
    string opp = opposite(stack);
    reverse(opp.begin(), opp.end());
    return opp;
}

int minNbMove(string stack)
{
    if(stack.size() == 0)
        return 0;

    if(stack[stack.size()-1] == '-')
    {
        if(stack[0] == '-')
            return 1 + minNbMove(flip(stack));
        else
            return 1 + minNbMove(opposite(stack));
    }
    else
    {
        int i;
        for(i = stack.size() - 1 ; i >= 0 && stack[i] == '+' ; i--);

        stack = stack.substr(0, i+1);
        return minNbMove(stack);
    }

    return 0;
}

int main(int argc, char** argv)
{
    ifstream file(argv[1]);
    ofstream output(argv[2]);

    if(!file)
        return -1;

    int T = 0;

    file >> T;

    for(int i = 0 ; i < T ; i++)
    {
        string stack;
        file >> stack;

        output << "Case #" << i+1 << ": " << minNbMove(stack) << endl;
    }

    file.close();
    output.close();

    return 0;
}
