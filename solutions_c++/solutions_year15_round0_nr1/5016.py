#include <iostream>
#define ll long long

ll howMany (ll smax, std::string people)
{
    // How many are already standing.
    ll standing = 0;
    ll added = 0;
    for (ll i = 0; i <= smax; i++)
    {
        //std::cout << standing << std::endl;
        if (i > standing)
        {
            added += i - standing;
            standing += i - standing;
        }
        standing += (ll)(people[i] - '0');
    }
    return added;
}

int main()
{
    ll tests;
    ll smax;
    std::string people;   
    std::cin >> tests;
    for (ll i = 1; i <= tests; i++)
    {
        std::cin >> smax >> people;
        std::cout << "Case #" << i << ": "<< howMany(smax, people) << std::endl;
    }
}