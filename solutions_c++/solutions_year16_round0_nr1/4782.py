#include <iostream>

using namespace std;

typedef long long ll;

ll GetCount(ll num)
{
    if (num == 0)
    {
        return 0;
    }
    int goal = (1 << 10) - 1;
    int digitsHit = 0;
    
    int count = 0;
    
    for (; digitsHit != goal && ++count; )
    {
        ll temp = num * count;
        if (temp < 0)
        {
            throw "Fk";
        }
        
        while (temp)
        {
            digitsHit |= 1 << (temp % 10);
            temp /= 10;
        }
    }
    
    
    return count * num;
}

int main()
{
    int T;
    cin >> T;
    
    for (int t = 1; t <= T; ++t)
    {
        ll num;
        cin >> num;
        
        ll count = GetCount(num);
        if (count == 0)
            cout << "Case #" << t << ": INSOMNIA\n";
        else
            cout << "Case #" << t << ": " << count << "\n";
    }
}