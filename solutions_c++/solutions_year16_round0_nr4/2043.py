#include <iostream>
#include <math.h>

using namespace std;

#define debug cout

typedef long long int ll;

int K, C, S;
ll start_mul;

ll compute_simple()
{
    ll pos = K-1;
    ll mul = 1;
    ll total = 0;

    for (int i = 1; i <= K; i++)
    {
        total += pos * mul;
        
        pos--;
        mul *= K;
    }
    
    total++;
    
    return total;
}

ll compute(int pos)
{
    ll mul = start_mul;
    ll total = 0;
    
    pos--;
    
    for (int i = 1; i <= C; i++)
    {    
        total += pos * mul;
    
        mul /= K;
        if (pos < K-1)
            pos++;
    }
    
    total++;
    
    return total;
}

void RunInstance()
{
    cin >> K >> C >> S;
    
    start_mul = pow(K, C-1);
    
    if (C == 1)
    {
        if (K > S)
            cout << "IMPOSSIBLE";
        else
            for (int i = 1; i <= K; i++)
                cout << i << " ";
    }
    else if (K > S*C)
        cout << "IMPOSSIBLE";
    else if (C >= K)
    {
        cout << compute_simple();
    }
    else
    {
        for (int i = 1; i <= K; i += C)
        {
            cout << compute(i) << " ";
        }
    }
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