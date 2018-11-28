#include <iostream>
#include <vector>

using namespace std;

#define int long long

#define ROOT_OF_MAX (10 * 1000 * 1000)

bool check_pal(int n)
{
    int x = n, y = 0;

    while (true)
    {
        y += x % 10;
        x /= 10;

        if (!x)
            break;

        y *= 10;
    }

    return (y == n);
}

vector <int> res;

void preprocess(int root_of_max)
{
    for (int i = 1; i < root_of_max; i++)
        if (check_pal(i) && check_pal(i * i))
            res.push_back(i * i);
}

main()
{
    preprocess(ROOT_OF_MAX);

    int NN;
    cin >> NN;

    for (int CC = 0; CC < NN; CC++)
    {
        int a, b;
        cin >> a >> b;

        int count = 0;
        for (int i = 0; i < res.size(); i++)
            if (res[i] >= a && res[i] <= b)
                count ++;

        cout << "Case #" << CC + 1 << ": " << count << endl;
    }
}

