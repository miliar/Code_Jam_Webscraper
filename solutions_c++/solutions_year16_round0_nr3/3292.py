#include "Libs.h"

using namespace std;

long long int nTests;
long long int dividers[9] = { 0, 0, 0, 0, 0, 0, 0, 0, 0 };


string toBinary(long long int N, string str)
{
    if (N / 2 != 0)
        str = toBinary(N / 2, str);

    return str + to_string(N % 2);
}

long long int toBinary(long long int N)
{
    return atoll(toBinary(N, "").c_str());
}

long long int convertBto10(long long int N, long long int b)
{
    long long int output = 0;
    long long int compteur = 0;
    
    while (N > 0)
    {
        output += (N % 10) * pow(b, compteur++);
        N /= 10;
    }

    return output;
}

long long int getMax(long long int N)
{
    string str = "";

    for (long long int i = 0; i < N; ++i)
        str += "1";

    return convertBto10(atoll(str.c_str()), 2) + 1;
}

long long int getMin(long long int N)
{
    string str = "1";

    for (long long int i = 0; i < N - 2; ++i)
        str += "0";

    str += "1";

    return convertBto10(atoll(str.c_str()), 2) + 1;
}

long long int isPrime(long long int N)
{
    for (long long int i = 2; i < sqrt(N); ++i)
        if (N % i == 0) return i;

    return 0;
}

int main()
{
	ofstream out("output.txt");
	ifstream in("input.txt");

    long long int J, N, nbTrouves = 0;

    in >> nTests >> J >> N;

    long long int max = getMax(J);
    long long int min = getMin(J);
    out << "Case #1: " << endl;
    for (long long int j = min; j < max && nbTrouves < N; ++j)
    {
        long long int coinJam = toBinary(j);
        bool isGood = true;

        if (coinJam % 2 == 1)
        {
            for (long long int base = 2; base <= 10 && isGood; ++base)
            {
                if (coinJam == 100011)
                    cout << "";
                long long int nbInDecimal = convertBto10(coinJam, base);
                long long int divider = isPrime(convertBto10(coinJam, base));

                if (divider != 0)
                    dividers[base - 2] = divider;
                else
                    isGood = false;
            }

            if (isGood)
            {
                out << coinJam;
                for (long long int i = 2; i <= 10; ++i)
                    out << " " << dividers[i - 2];
                out << endl;
                ++nbTrouves;
            }
        }
    }

	return 0;
}