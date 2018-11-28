#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <map>

using namespace std;

bool finished(int count[])
{
    for (int i = 0 ; i < 10 ; i++)
    {
        if (!count[i])
            return false;
    }
    return true;
}

long long int cal(map <unsigned long long int, long long int> &m, long long int n)
{
    auto it = m.find(n);

    int count[10] = {0};
    map <long long int, bool> process; 

    if (it != m.end())
        return it->second;

    int i = 1;

    while (true)
    {
        long long int tmp = i++ * n;   
        long long int target = tmp;

        auto it = process.find(tmp);

        if (it != process.end())
            return -1;
        else
            process[tmp] = true;

        while (tmp > 0)
        {
            count[tmp%10] = 1;
            tmp /= 10;
        }

        if (finished(count))
        {
            m[n] = target;
            return target;
        }
    }
}


int main()
{
    ios_base::sync_with_stdio(false);

    int t;

    long long int n;

    map <unsigned long long int, long long int> m;

    m[0] = -1;

    cin >> t;

    for (int i = 0 ; i < t ; i++)
    {
        cin >> n;

        cout << "Case #" << i+1 << ": ";
        
        if (n == 0)
        {
            cout << "INSOMNIA";
        }
        else
        {
            auto result = cal(m, n);

            if (result == -1)
                cout << "INSOMNIA";
            else
                cout << result; 
        }


        if (i != t-1)
            cout << endl;
    }

    exit(EXIT_SUCCESS);
}
