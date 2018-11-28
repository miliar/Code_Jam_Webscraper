#include <iostream>
#include <iomanip>
using namespace std;

double timer(int numFarms, double C, double F, double X);

int main()
{
    int cases;
    cin >> cases;
    double C, F, X;
    
    for(int i = 0; i < cases; i++)
    {
        cin >> C;
        cin >> F;
        cin >> X;
        
        double time = -1;
        double prev;
        
        int numFarms = 0;
        do
        {
            prev = time;
            time = timer(numFarms, C, F, X);
            numFarms++;
        }while(time < prev || prev == -1);
        
        cout << setprecision(7) << fixed << "Case #" << i + 1 << ": " << prev << endl;
    }
}

// Given the number of farms purchased, calculate the time
double timer(int numFarms, double C, double F, double X)
{
    double time = X/(2 + numFarms * F);
    
    for (int i = 0; i < numFarms; i++)
    {
        time += C/(2 + i * F);
    }
    return time;
}