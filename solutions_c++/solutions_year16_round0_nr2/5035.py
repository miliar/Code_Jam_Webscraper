#include <iostream>
#include <string>
#include <stack>

using namespace std;
int flipping(string s);

int main()
{
    stack<int> firstStack;
    stack<int> secondStack;
    int t;

    cin >> t;

    int answer[t];
    string input[t];

    for(int i = 0; i < t; i++)
    {
        cin >> input[i];
        answer[i] = flipping(input[i]);
    }

    for(int i = 0; i < t; i++)
    {
        cout << "Case #" << (i + 1) << ": " << answer[i] << endl;
    }

}

//FUCK PARA QUE NO SE ME OLVIDE: FUCKING DIVIDE IT INTO STRINGS, TAKE UNTIL IT DIFFERENCIATES and flipt those, THEN REPEAT
//IN THE END JUST MAKE SURE YOU FLIP IT ONE MORE TIME IF IT ENDED ON -
int flipping(string s)
{
    bool needsFlipping = true;
    //char temp;
    stack<char> firstStack;
    stack<char> secondStack;
    char current = '\0';
    char nextOne = '\0';
    int counter = 0;

    for(int i = s.size() - 1; i >= 0; i--)
    {
        firstStack.push(s[i]);
    }

    if(firstStack.size() == 1)
    {
        if(firstStack.top() == '-')
            return 1;
        else
            return 0;
    }

    while(needsFlipping)
    {
        if(current == '\0')
        {
            current = firstStack.top();
            secondStack.push(firstStack.top());
            firstStack.pop();
        }
        else
        {
            while(!firstStack.empty())
            {

                nextOne = firstStack.top();
                //this means that the first one is the same so it continues
                if(current == nextOne)
                {
                    secondStack.push(firstStack.top());
                    firstStack.pop();
                    current = nextOne;
                }
                else
                {
                    //if it's not the same it means it stops there and starts flipping
                    if(secondStack.top() == '-')
                    {
                        while(!secondStack.empty())
                        {
                            firstStack.push('+');
                            secondStack.pop();
                        }
                    }
                    else
                    {
                        while(!secondStack.empty())
                        {
                            firstStack.push('-');
                            secondStack.pop();
                        }
                    }
                    counter++;
                    current = firstStack.top();
                    secondStack.push(firstStack.top());
                    firstStack.pop();
                }
            }
            if(secondStack.top() == '+')
            {
                needsFlipping = false;
                return counter;
            }
            else
            {
                needsFlipping = false;
                return counter + 1;
            }

        }
    }
}
