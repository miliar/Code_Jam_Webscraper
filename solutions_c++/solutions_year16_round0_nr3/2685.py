#include <fstream>
#include <iostream>
#include <cmath>
#include <cstdio>

using namespace std;

long long numbers[501][10];

char temp_name[51];

long long go_to_base(long long number, long long base)
{
    long long power = 1;
    long long result_number = 0;
    while (number > 0)
    {
        result_number += (number & 1) * power;
        power *= base;
        number >>= 1;
    }
    return result_number;
}

long long divisor(long long number)
{
    int limit = sqrt(number) + 1;
    if (number % 2 == 0)
        return 2;
    for (int i = 3; i < limit; i += 2)
        if (number % i == 0)
            return i;
    return -1;
}

void generate_numbers(int length, int number_of_numbers)
{
    long long number = (1ll << (length - 1)) + 1;
    int i;
    int counter = 0;
    long long number_in_base_i;
    long long div;
    while (counter <= number_of_numbers)
    {
        numbers[counter][0] = number;
        for (i = 2; i < 11; i++)
        {
            number_in_base_i = go_to_base(number, i);
            div = divisor(number_in_base_i);
            if (div < 0)
                break;
            numbers[counter][i - 1] = div;
        }
        if (i > 10)
            counter++;
        number += 2;
        if (number == 32945)
            number = 32945;
    }
}

void write_solution(int number_of_numbers)
{
    ofstream g(temp_name);
    int j;
    g << number_of_numbers << '\n';
    for (int i = 0; i < number_of_numbers; i++)
    {
        g << go_to_base(numbers[i][0], 10) << " ";
        for (j = 1; j < 10; j++)
            g << numbers[i][j] << " ";
        g << '\n';
    }
    g.close();
}

void precalculations()
{
    int length = 16;
    int number_of_numbers = 50;
    generate_numbers(length, number_of_numbers);
    sprintf(temp_name, "%d.txt", length);
    write_solution(number_of_numbers);
}

void solve()
{
    int test, n, j, number_of_numbers;
    int i, l;
    long long precalculated_number;
    ifstream f("coinjam.in");
    ofstream g("coinjam.out");
    f >> test;
    for (int k = 1; k <= test; k++)
    {
        f >> n >> j;
        sprintf(temp_name, "%d.txt", n);
        ifstream temp(temp_name);
        temp >> number_of_numbers;
        g << "Case #" << k << ":\n";
        for (i = 0; i < j; i++)
        {
            for (l = 0; l < 10; l++)
            {
                temp >> precalculated_number;
                g << precalculated_number << " ";
            }
            g << '\n';
        }
        temp.close();
    }
    f.close();
    g.close();
}

int main()
{
    //precalculations();
    solve();
    return 0;
}
