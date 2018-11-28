#include <iostream>
#include <vector>

using namespace std;

#define debug cout
typedef long long int ll;
const int nb_of_digits = 10;
vector<bool> v;

void RemoveDigits(ll n)
{
    do 
    {
        int d = n % 10;
        v[d] = true;
        n /= 10;
    } while (n > 0);
}

bool AllDigitsAreChecked()
{
    for (int i = 0; i < nb_of_digits; i++)
        if (!v[i])
            return false;
    return true;
}

void RunInstance()
{
    ll N = 0;
    ll total = 0;
    v = vector<bool>(nb_of_digits, false);
    
    cin >> N;
    
    if (N == 0)
    {
        cout << "INSOMNIA";
    }
    else
    {
        do 
        {
            total += N;
            RemoveDigits(total);
        }
        while (!AllDigitsAreChecked());
        
        cout << total;
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