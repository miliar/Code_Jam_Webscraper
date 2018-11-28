#include <cstdlib>
#include <fstream>
#include <iostream>
#include <cmath>

using namespace std;

char* itoa(long int value, char* result, long int base);
long int is_prime (long int num);

int main()
{
    ifstream in;
    in.open("in.txt");
    ofstream out;
    out.open("out.txt");

    long int case_num;
    in >> case_num;

    for (long int i_case = 1; i_case <= case_num; i_case++)
    {

        out << "Case #" << i_case << ":" << endl;

        long int coin_length, coins_needed;
        in >> coin_length >> coins_needed;

        //going through all jamcoins
        long int coin_count = 0;
        unsigned long int coin_number_repr = pow(2, coin_length-1);
        while (coin_count < coins_needed && coin_number_repr < pow(2, coin_length))
        {
            coin_number_repr++;
            char coin[coin_length];
            itoa(coin_number_repr, coin, 2);
            //cout << coin << endl;

            long int divisors[9];
            bool is_coin = true;
            if (coin[coin_length-1] != '1')
            {
                is_coin = false;
            }
            else
            {

                //converting in bases 2 to 10;
                for (long int base = 2; base <= 10; base++)
                {
                    long int num = 0, mult = 1;
                    for (long int i = coin_length-1; i >= 0; i--)
                    {
                        if (coin[i] == '1')
                            num += mult;
                        mult *= base;
                    }

                    cout << num << " " << is_prime(num) << endl;

                    //finding divizors in each base
                    divisors[base-2] = is_prime(num);

                    //testing if its prime in 2 to 10 bases
                    if (divisors[base-2] == 0)
                    {
                        is_coin = false;
                        break;
                    }
                }
            }

            if (is_coin)
            {
                coin_count++;
                out << coin << " ";
                for (long int base = 0; base <= 8; base++)
                    out << divisors[base] << " ";
                out << endl;
            }

        }

    }

    in.close();
    out.close();

    return 0;
}

char* itoa(long int value, char* result, long int base) {
		// check that the base if valid
		if (base < 2 || base > 36) { *result = '\0'; return result; }

		char* ptr = result, *ptr1 = result, tmp_char;
		long int tmp_value;

		do {
			tmp_value = value;
			value /= base;
			*ptr++ = "zyxwvutsrqponmlkjihgfedcba9876543210123456789abcdefghijklmnopqrstuvwxyz" [35 + (tmp_value - value * base)];
		} while ( value );

		// Apply negative sign
		if (tmp_value < 0) *ptr++ = '-';
		*ptr-- = '\0';
		while(ptr1 < ptr) {
			tmp_char = *ptr;
			*ptr--= *ptr1;
			*ptr1++ = tmp_char;
		}
		return result;
	}

long int is_prime (long int num)
{
    if (num <=1)
        return 1;
    else if (num == 2)
        return 0;
    else if (num % 2 == 0)
        return 2;
    else
    {
        long int prime = 0;
        long int divisor = 3;
        double num_d = static_cast<double>(num);
        long int upperLimit = static_cast<long int>(sqrt(num_d) +1);

        while (divisor <= upperLimit)
        {
            if (num % divisor == 0)
            {
                prime = divisor;
                break;
            }
            divisor +=2;
        }
        return prime;
    }
}








