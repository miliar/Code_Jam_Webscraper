#include <iostream>
#include <string.h>
# define MAXSIZE 100
using namespace std;

class PancakeRevenge{

    public:
            PancakeRevenge();
            char pancakeStack[MAXSIZE];
            int N; //Stack size
            PancakeRevenge(int N);
            void liftPancakes(int n);
            void displayPancakeStack(char pancakeStack[]);
            int minimumLifts();


};

int PancakeRevenge::minimumLifts()
{
    char happyStack[N];
    for(int i = 0; i < N; i++)
    {
        happyStack[i] = '+';
    }
    int minLifts = 0;
    if(strcmp(pancakeStack, happyStack) == 0)
    {
        cout <<"";
        return minLifts;
    }

    for(int i = 0; i < N; i++)
    {
       char lastface = pancakeStack[0];
       if(pancakeStack[i] != lastface)
       {
           liftPancakes(i);
           i = 0;
           minLifts++;
       }

    }
    if(strcmp(pancakeStack, happyStack) == 0)
    {
        return minLifts;
    }
    else
    {
        liftPancakes(N);
        return minLifts + 1;
    }

}

PancakeRevenge::PancakeRevenge()
{

}



void PancakeRevenge::displayPancakeStack(char pancakeStack[])
{
        for(int i = 0; i < N; i++)
        {
            cout << pancakeStack[i];
        }
        cout << endl;
}

void PancakeRevenge::liftPancakes(int n)
{
    char smallStack[n];

    //copies, flips and switches n pancakes into smaller stack
    for(int i = 0; i < n; i++)
    {
        smallStack[i] = pancakeStack[n-i-1];
        if(smallStack[i] == '+')
        {
            smallStack[i] = '-';
        }
        else if(smallStack[i] == '-')
        {
            smallStack[i] = '+';
        }

    }

    //puts the smaller stack back onto the pancake
    for(int i = 0; i < n; i++)
    {
        pancakeStack[i] = smallStack[i];
    }


}

int main()
{
    int T;
    PancakeRevenge stack1;
    cin >> T;
    for(int i = 0; i < T; i++)
    {
        cout << "Case #" << i+1 << ": ";
        cin >> stack1.pancakeStack;
        stack1.N = strlen(stack1.pancakeStack);
        cout << stack1.minimumLifts() << endl;
    }



    return 0;
}
