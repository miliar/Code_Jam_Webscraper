#include <cstdio>
#include <iostream>

using namespace std;

void readInput(int& answer, int* grid)
{
    cin >> answer;
    answer--;
    
    for(int i = 0; i < 16; i++)
    {
        cin >> grid[i];
    }
}

void solveCase()
{
    //read input
    float C, F, X;
    cin >> C >> F >> X;
    
    //compute time
    float tc = C / 2;
    float tx = X / 2;
    float r = 2;
    
    do
    {
        r += F;
        float t = X / r + tc;
        
        if (t < tx)
        {
            tx = t;
            tc += C / r;
        }
        else
        {
            break;
        }
    }
    while(true);
    
    //output result
    printf("%.7f", tx);
}

int main()
{
    int caseCount;
    cin >> caseCount;

    for(int i = 1; i <= caseCount; i++)
    {
        cout << "Case #" << i << ": ";
        solveCase();
        cout << endl;
    }

    return 0;
}
