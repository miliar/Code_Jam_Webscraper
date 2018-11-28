#include <iostream>
#include <string>
int main()
{
    int T;
    int N;
    std::cin >> T;
    N = T;
    while(T--)
    {
        int max;
        std::string data;
        std::cin >> max >> data;
        int current = data[0]-'0';
        int addition = 0;
        for(int i = 1; i < data.length(); ++i)
        {
            if (i <= current)
                current+=data[i]-'0';
            else 
            {
                int t = i - current;
                addition += t;
                current += (t + data[i]-'0');
            }
            
        }
        std::cout << "Case #" <<N-T<<": "<< addition << std::endl;
    }
}