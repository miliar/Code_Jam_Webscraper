#include <iostream>

void read_digit(int n, unsigned short int* result);

int main()
{
    int t;
    int previous_number;
    int current_number;
    int mul;
    unsigned short int result = 0;

    std::cin >> t;
    for (int i = 1; i <= t; ++i) {
        std::cin >> previous_number;
        mul = 1;
        current_number = -1;
        result = 0;
        while(true)
        {
            current_number = mul * previous_number;
            if(current_number == previous_number && mul > 1)
            {
                std::cout<< "Case #" << i << ": " << "INSOMNIA" << std::endl;
                break;
            }
            read_digit(current_number, &result);
            if(result == 1023)
            {
                std::cout << "Case #" << i << ": " << current_number << std::endl;
                break;
            }
            mul++;
        }
    }
    return 0;
}

void read_digit(int n, unsigned short int* result)
{
    int digit;
    do {
    digit = n % 10;
    *result |= (1<<digit);
    n /= 10;
} while (n > 0);
}
