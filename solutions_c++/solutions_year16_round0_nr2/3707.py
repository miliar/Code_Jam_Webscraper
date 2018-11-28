#include <stdio.h>
#include <string>

using namespace std;

string flip(string stack)
{
    string newStack;
    for (int i = stack.length()-1; i >= 0; --i)
    {
        if (stack[i] == '+')
            newStack += "-";
        else
            newStack += "+";
    }
    return newStack;
}

int flipsNumber(string stack)
{
    if (stack.length() == 0)
        return 0;
    if (stack.back() == '+')
        return flipsNumber(stack.substr(0, stack.length()-1));
    if (stack[0] == '-')
    {
        string n = flip(stack);
        return 1 + flipsNumber(n.substr(0, n.length()-1));
    }

    string first, last;
    for (int i = 0; i < stack.length(); ++i)
    {
        if (stack[i] == '-')
            break;
        first += "-";
    }
    last = stack.substr(first.length());
    return 1 + flipsNumber(first + last);
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t)
    {
        char temp[100];
        scanf("%s", temp);
        string stack(temp);
        printf("Case #%d: %d\n", t, flipsNumber(stack));
    }
    return 0;
}
