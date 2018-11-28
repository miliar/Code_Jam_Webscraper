#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
#include <set>
#include <unordered_map>
#include <random>

using namespace std;

int n;

long long power_it(long long x, int b)
{
    long long a = x; x = 1;
    for (int i = 0; i < b; ++i)
        x *= a;

    return x;
}

long long check_in_base(string str, int base)
{
    reverse(str.begin(), str.end());

    long long tmp = 0;
    for (int i = 0; i < str.length(); ++i) {
        if ((int)str[i]-48 == 0)
            continue;

        tmp += power_it(base, i);
    }

    for (long long i = 2; i * i <= tmp; ++i) {
        if (tmp % i == 0)
            return i;
    }

    return -1;
}

int main()
{
    random_device rd;
    mt19937 mt(rd());

    scanf("%d", &n);

    for (int i = 1; i <= n; ++i) {
        int a, b;
        scanf("%d %d", &a, &b);
        printf("Case #%d:\n", i);



        int found = 0;
        while (found < b) {
            std::uniform_int_distribution<> dis(1, 2);

            string str = "1";
            for (int i = 0; i < a - 2; ++i)
                str += (dis(mt) == 1 ? "1" : "0");

            str += "1";

            vector<int> result;
            for (int base = 2; base <= 10; ++base) {
                long long res = check_in_base(str, base);
                if (res <= 0)
                    break;

                result.push_back(res);
            }

            if (result.size() == 9) {
                cout << str;
                for (auto x : result)
                    cout << " " << x;

                cout << endl;
                found++;
            }
        }
    }
    return 0;
}
