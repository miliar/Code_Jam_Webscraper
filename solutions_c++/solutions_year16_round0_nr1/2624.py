#include <iostream>
#include <cstdio>

using namespace std;

bool used[10];

int f(int n){
    if (n == 0)
        return -1;

    int x = 0, y = 0, cnt = 0;

    for (int i = 0; i < 10; ++i)
        used[i] = false;

    while (cnt != 10){
        x += n;
        y = x;
        while (y != 0){
            if (!used[y % 10])
                cnt++;
            used[y % 10] = true;
            y /= 10;
        }
    }

    return x;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t, d, x;
    cin >> t;
    for (int i = 1; i <= t; ++i){
        cin >> x;
        d = f(x);
        cout << "Case #" << i << ": ";
        if (d == -1)
            cout << "INSOMNIA" << endl;
        else
            cout << d << endl;
    }

    fclose(stdout);
    return 0;
}
