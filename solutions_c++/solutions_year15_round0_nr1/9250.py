#include <iostream>
#include <string>

int chartoint(char a)
{
    return (int)(a-48);
}

int main()
{
    int t;
    std::cin >> t;
    int smax, sum, res;
    char str, m;
    for(int i = 0; i < t; i++)
    {
        sum = res = 0;
        std::cin >> smax;
        for(int j = 0; j < smax; j++)
        {
            std::cin >> str;
            sum += chartoint(str);
            if(sum < j+1)
            {
                res += (j+1)-sum;
                sum += (j+1)-sum;
            }
        }
        std::cin >> m;
        std::cout << "Case #" << i+1 << ": " << res << std::endl;
    }
    return 0;
}
