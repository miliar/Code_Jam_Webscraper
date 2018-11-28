#include <fstream>
#include <cmath>

using namespace std;

bool isPalindrome(long long x)
{
    int temp = x;
    char line[20];
    int i = 0;
    for (i = 0;temp != 0;i++) { line[i] = temp % 10; temp /= 10; }
    line[i] = 0;
    for (int t = 0;t <= i - t - 1;t++)
    {
        if (line[t] != line[i - 1 - t]) return false;
    }
    return true;
}

int main()
{
    ifstream in("DB.in");
    ofstream out("DB.out");

    int times = 0;
    in >> times;

    for (int num = 0;num < times;num++)
    {
        long long a,b,ans;
        ans = 0;
        in >> a >> b;
        a = ceil(sqrt(a));
        b = floor(sqrt(b));
        for (int i = a;i <= b;i++)
        {
            if (isPalindrome(i))
            {
                if (isPalindrome(i * i)) ans++;
            }
        }
        out << "Case #" << num + 1 << ": " << ans << '\n';
    }
    return 0;
}
