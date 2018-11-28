#include <iostream>
#include <fstream>
#include <queue>
#include <climits>
#include <cmath>

using namespace std;


int findBest(priority_queue<int>& q, int max, int steps = 0)
{
    int top = q.top();
    int res = INT_MAX, min = top;

    int zero = 1;

    if(steps > max)
        return max;

    int nb;

    for(nb = 0 ; !q.empty() && q.top() == top ; nb++)
        q.pop();

    for(int j = 0 ; j < nb ; j++)
        q.push(top);


    for(int i = 2 ; ceil((double)top/(double)i) + nb*(i - 1) < top ; i++)
    {
        zero = 0;

        priority_queue<int> q2 = q;

        for(int j = 0 ; j < nb ; j++)
        {
            q2.pop();
            q2.push(top/i);
            q2.push(top - top/i);
        }

        res = findBest(q2, max, steps+nb);

        if(res < min)
            min = res;
        else if(res > min)
            break;
    }

    return (top < nb+min) ? top : nb+min;
}


int main()
{
    ifstream input;
    ofstream output;
    input.open("input.txt");
    output.open("output.txt");

    int nbTests = 0, D = 0, P = 0;

    input >> nbTests;

    for(int i = 0 ; i < nbTests ; i++)
    {
        priority_queue<int> q;

        // Load data

        input >> D;

        for(int j = 0 ; j < D ; j++)
        {
            input >> P;
            q.push(P);
        }

        // Find solution

        output << "Case #" << i+1 << ": " << findBest(q, q.top()) << endl;
    }

    input.close();
    output.close();

    return 0;
}
