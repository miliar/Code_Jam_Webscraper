#include <iostream>
#include <string>

int main()
{
    int t, k, c, s;
    std::string result;
    std::cin >> t;
    for (int i = 1; i <= t; ++i) {
        std::cin >> k >> c >> s;
        result = "";
        std::cout << "Case #" << i << ": ";
        for(int z = 1; z <= s; z++)
        {
            std::cout<<z;
            if(z<s)
                std::cout<<" ";
        }
         std::cout<< std::endl;
    }
    return 0;
}
