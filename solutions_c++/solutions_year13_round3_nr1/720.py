#include <algorithm>
#include <fstream>
#include <iostream>
#include <vector>

#define BUFFER_SIZE 1000010

long long solveProblemA(long n, char* data)
{
    long long result = 0;
    long last = 0;
    long count = 0;
    long i = 1;

    while (*data != '\0')
    {
        switch (*data)
        {
            case 'a' : case 'e' : case 'i' : case 'o' : case 'u' :
                count = 0;
                break;
            default :
                ++count;
                break;
        }

        if (count >= n)
            last = i - n + 1;

        result += last;

        ++data;
        ++i;
    }

    return result;
}

void problemA(std::ifstream& fin)
{
    std::ofstream fout("C:\\CodeJam\\problemA.out");

    int t = 0;
    fin >> t;

    char buffer[BUFFER_SIZE];
    long n;

    for (int i = 1; i <= t; ++i)
    {
        fin.getline(buffer, BUFFER_SIZE);
        fin.get(buffer, BUFFER_SIZE, ' ');
        fin >> n;
        fout << "Case #" << i << ": " << solveProblemA(n, buffer) << std::endl;
    }

    fout.close();
}
