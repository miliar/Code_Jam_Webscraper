#include <iostream>

using namespace std;

#define debug cout

int toAdd;
int counter;
int Smax;

void RunInstance()
{
    int Si, diff;
    char tmp;
    cin >> Smax;
    
    toAdd = 0;
    counter = 0;
    for (int i = 0; i <= Smax; i++)
    {
        cin >> tmp;
        Si = tmp - '0';
        
        if (counter < i)
        {
            diff = i - counter;
            toAdd += diff;
            counter += diff;
        }
        
        counter += Si;
    }
    
    cout << toAdd;
}

// ============================ Nothing to change here ============================ //

int main() 
{
    int num_of_instances = 0;
    cin >> num_of_instances;
    
    for (int i = 1; i <= num_of_instances; ++i) 
    {
        cout << "Case #" << i << ": ";
        RunInstance();
        cout << endl;
    }
}