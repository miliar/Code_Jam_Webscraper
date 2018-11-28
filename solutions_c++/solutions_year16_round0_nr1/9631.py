#include <iostream>

void inp_digit(int * ten, int & tot, int digit)
{
    int t = ten[digit] ^ 0x1;
    ten[digit] += t;
    tot += t;
}

bool inp_num(int * ten, int & tot, long num)
{
    while(num)
    {
        inp_digit(ten, tot, int(num%10L));
        num /= 10L;
        if (tot == 10)
            return true;
    }
    return false;
}

int main()
{
    int T;
    std::cin >> T;
    for(int t=0; t<T; t++)
    {
        long N;
        std::cin >> N;
        if(N)
        {
            long num = N;
            int ten[10] = {0};
            int tot = 0;
            while(true)
            {
                if(inp_num(ten, tot, num)) break;
                else num += N;
            }
            std::cout << "Case #" << (t+1) << ": " << num << std::endl;
        }
        else std::cout << "Case #" << (t+1) << ": INSOMNIA" << std::endl;
    }
    return 0;
}
