#include <iostream>
#include <cstring>

int Work(int n)
{
    bool d[10];
    std::memset(d, 0, sizeof d);

    for (int j = 1; j < 1000; j++) {
        for (int z = j * n; z; z /= 10)
            d[z % 10] = true;
        for (int i = 0; i < 10; i++)
            if (!d[i])
                goto next;
        return j * n;
next:;
    }
    return 0;
}

int main()
{
    using std::cin;
    int z;
    cin >> z;
    for (int x = 1; x <= z; x++) {
        int t, n;
        cin >> n;
        std::cout << "Case #" << x << ": ";
        if ((t = Work(n)))
            std::cout << t << std::endl;
        else
            std::cout << "INSOMNIA" << std::endl;
    }
}
