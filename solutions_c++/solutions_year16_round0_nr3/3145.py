#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

bool is_prime(uint64_t number);
void next_attempt(bool* array , int dim);
uint64_t convert_base_n(bool* array, int dim, int n);
uint64_t get_factor(uint64_t number);


int main(int argc, const char * argv[])
{

    int N = 16;
    int J = 50;

    bool current_number[N -2];
    int found = 0;
    fill_n(current_number, N-2, 0);
    ofstream output("C:/Users/Utente/Documents/Workspace/C/Coin Jam/bin/Debug/output.txt");
    output << "Case #1:" << endl;
    cout << "Case #1:" << endl;
    while(found < J)
    {
        bool tocontinue = true;
        for(int i = 2; i < 11 && tocontinue ; i ++)
        {
            if(is_prime(convert_base_n(current_number, N-2, i)))
            {
                tocontinue = false;
            }
        }
        if(tocontinue)
        {
            output << convert_base_n(current_number, N-2, 10) << " ";
            cout << convert_base_n(current_number, N-2, 10) << " ";
            for(int i = 2; i < 11; i ++)
            {
                output << get_factor(convert_base_n(current_number, N-2, i)) << " ";
                cout << get_factor(convert_base_n(current_number, N-2, i)) << " ";
            }
            output << endl;
            cout << endl;
            found ++;
        }
        next_attempt(current_number, N-2);
    }

    return 0;
}

bool is_prime(uint64_t number)
{
    bool tortn = true;
    for(int i = 2; i <= sqrt(number); i ++)
    {
        if((number % i) == 0)
        {
            tortn = false;
            break;
        }
    }
    return tortn;
}

uint64_t get_factor(uint64_t number)
{
    uint64_t tortn = number;
    for(int i = 2; i <= sqrt(number); i ++)
    {
        if((number % i) == 0)
        {
            tortn = i;
            break;
        }
    }
    return tortn;
}

void next_attempt(bool* array , int dim)
{
    bool carry = 1;
    for(int i = dim-1; i >=0 && carry; i--)
    {
        if(array[i] == 0)
        {
            array[i]= 1;
            carry = 0;
        }
        else
        {
            array[i]= 0;
        }
    }
}

uint64_t convert_base_n(bool* array, int dim, int n)
{
    uint64_t tortn = 1 + pow(n, dim + 1);
    for(int i = 0; i < dim; i ++)
    {
        tortn += pow(array[i] * n, dim - i);
    }
    return tortn;
}
