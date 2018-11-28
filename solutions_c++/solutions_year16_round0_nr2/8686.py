#include <iostream>
#include <String>

using namespace std;

int orderHappySide (string stack)
{
    int i=0;
    long flips = 0;
    while (stack[i+1] != '\0')
    {
        if (stack[i] != stack[i+1])
        {
            for(int j=0; j<=i; j++)
            {
                stack[j] = stack[i+1];
            }
            //cout << stack << endl;
            flips++;
        }
        i++;
    }
    if(stack[i] == '-')
    {
        for(int k=0; k<=i; k++)
        {
            stack[k] = '+';
        }
        //cout << stack << endl;
        flips++;
    }
    //cout << "flips: " << flips << endl;
    //cout << endl;
    return flips;
}

int main ()
{
    int t;
    string pancakes;
    cin >> t;
    for (int i=1; i<=t; i++)
    {
        cin >> pancakes;
        cout << "Case #" << i << ": " << orderHappySide (pancakes) << endl;
    }
}
