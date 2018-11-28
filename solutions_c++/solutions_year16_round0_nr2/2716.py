#include <iostream>

using namespace std;

void flip(string & stack, size_t pos)
{
    string substack = stack.substr(0, pos + 1);
    for (int i = 0; i < pos + 1; ++i)
    {
        if (substack[pos - i] == '-')
        {
            stack[i] = '+';
        }
        else
        {
            stack[i] = '-';
        }
    }
}

int main()
{
    int T;
    cin >> T;
    for (int t = 0; t < T; t++)
    {
        string stack;
        cin >> stack;

        int counter = 0;

        size_t posOfLastMinus = stack.rfind("-");
        while (posOfLastMinus != string::npos)
        {
            cerr << "Stack is " << stack << endl;
            size_t posOfFirstMinus = stack.find("-");
            cerr << "posOfFirstMinus = " << posOfFirstMinus << endl;
            if (posOfFirstMinus != 0)
            {
                flip(stack, posOfFirstMinus - 1);
                counter++;
            }
            flip(stack, posOfLastMinus);
            counter++;

            posOfLastMinus = stack.rfind("-");
            cerr << endl;
        }

        cout << "Case #" << (t+1) << ": " << counter << endl;
    }
    return 0;
}
