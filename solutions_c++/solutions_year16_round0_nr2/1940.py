#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

int calc(const string& pancakes)
{
    int resp = (pancakes.back() == '+') ? -1 : 0;
    auto it = pancakes.begin();
    do {
        ++resp;
        it = find_if_not(it, pancakes.end(), [&](auto c) {return c == *it;});
    } while(it != pancakes.end());

    return resp;
}

int main()
{
    int t;
    cin >> t;
    for(int lp=1;lp<=t;++lp)
    {
        string pancakes;
        cin >> pancakes;
        cout << "Case #" << lp << ": " << calc(pancakes) << "\n";
    }

    return 0;
}
