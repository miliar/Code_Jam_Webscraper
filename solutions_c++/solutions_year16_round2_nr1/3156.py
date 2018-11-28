#include <iostream>
#include <stdio.h>
#include <string>

using namespace std;

int alphaArr[26];
int copyArr[26];
int filter[26];

int collect[26];

void AddNumber(string number, int realNumber, string& result)
{
    int min = 3000;

    if (filter[realNumber])
        return;

    for (int i = 0; i < number.length(); i++)
    {
        if (min > alphaArr[number[i] - 'A'])
        {
            min = alphaArr[number[i] - 'A'];
        }
    }

    if (min > 0 && number == "THREE")
    {
        min = alphaArr['E' - 'A'] / 2;
    }
    else if (min > 0 && number == "SEVEN")
    {
        min = alphaArr['E' - 'A'] / 2;
    }
    else if (min > 0 && number == "NINE")
    {
        min = alphaArr['N' - 'A'] / 2;
    }

    if (min > 0)
    {
        for (int i = 0; i < min; i++)
        {
            result += ('0' + realNumber);
        }

        for (int i = 0; i < number.length(); i++)
        {
            alphaArr[number[i] - 'A'] -= min;
        }
    }
}

void SetFilter()
{
    filter[0] += 1;
    for (int i = 0; i < 10; i++)
    {
        if (filter[i] == 2)
        {
            filter[i] = 0;
            filter[i + 1] += 1;
        }
    }
}

int main()
{
    int testN;
    char str[3000];
    string result;
    cin >> testN; cin.ignore();

    for (int test = 1; test <= testN; ++test)
    {
        int strLength;
        int tem = true;
        result.clear();

        for (int i = 0; i < 26; i++)
            collect[i] = filter[i] = alphaArr[i] = 0;

        cin >> str; cin.ignore();

        strLength = strlen(str);

        for (int i = 0; i < strLength; ++i)
        {
            alphaArr[str[i] - 'A'] += 1;
        }

        if (alphaArr['Z' - 'A'] > 0) // ZERO
        {
            collect[0] = tem = alphaArr['Z' - 'A'];
            alphaArr['Z' - 'A'] -= tem;
            alphaArr['E' - 'A'] -= tem;
            alphaArr['R' - 'A'] -= tem;
            alphaArr['O' - 'A'] -= tem;
        }

        if (alphaArr['W' - 'A'] > 0) // TWO
        {
            collect[2] = tem = alphaArr['W' - 'A'];
            alphaArr['T' - 'A'] -= tem;
            alphaArr['W' - 'A'] -= tem;
            alphaArr['O' - 'A'] -= tem;
        }

        if (alphaArr['U' - 'A'] > 0) // FOUR
        {
            collect[4] = tem = alphaArr['U' - 'A'];
            alphaArr['F' - 'A'] -= tem;
            alphaArr['O' - 'A'] -= tem;
            alphaArr['U' - 'A'] -= tem;
            alphaArr['R' - 'A'] -= tem;
        }

        if (alphaArr['O' - 'A'] > 0) // ONE
        {
            collect[1] = tem = alphaArr['O' - 'A'];
            alphaArr['O' - 'A'] -= tem;
            alphaArr['N' - 'A'] -= tem;
            alphaArr['E' - 'A'] -= tem;
        }

        if (alphaArr['F' - 'A'] > 0) // FIVE
        {
            collect[5] = tem = alphaArr['F' - 'A'];
            alphaArr['F' - 'A'] -= tem;
            alphaArr['I' - 'A'] -= tem;
            alphaArr['V' - 'A'] -= tem;
            alphaArr['E' - 'A'] -= tem;
        }

        if (alphaArr['X' - 'A'] > 0) // SIX
        {
            collect[6] = tem = alphaArr['X' - 'A'];
            alphaArr['S' - 'A'] -= tem;
            alphaArr['I' - 'A'] -= tem;
            alphaArr['X' - 'A'] -= tem;
        }

        if (alphaArr['S' - 'A'] > 0) // SEVEN
        {
            collect[7] = tem = alphaArr['S' - 'A'];
            alphaArr['S' - 'A'] -= tem;
            alphaArr['E' - 'A'] -= tem;
            alphaArr['V' - 'A'] -= tem;
            alphaArr['E' - 'A'] -= tem;
            alphaArr['N' - 'A'] -= tem;
        }

        if (alphaArr['G' - 'A'] > 0) // EIGHT
        {
            collect[8] = tem = alphaArr['G' - 'A'];
            alphaArr['E' - 'A'] -= tem;
            alphaArr['I' - 'A'] -= tem;
            alphaArr['G' - 'A'] -= tem;
            alphaArr['H' - 'A'] -= tem;
            alphaArr['T' - 'A'] -= tem;
        }

        if (alphaArr['H' - 'A'] > 0) // THREE
        {
            collect[3] = tem = alphaArr['H' - 'A'];
            alphaArr['T' - 'A'] -= tem;
            alphaArr['H' - 'A'] -= tem;
            alphaArr['R' - 'A'] -= tem;
            alphaArr['E' - 'A'] -= tem;
            alphaArr['E' - 'A'] -= tem;
        }

        if (alphaArr['I' - 'A'] > 0) // NINE
        {
            collect[9] = tem = alphaArr['I' - 'A'];
            alphaArr['N' - 'A'] -= tem;
            alphaArr['I' - 'A'] -= tem;
            alphaArr['N' - 'A'] -= tem;
            alphaArr['E' - 'A'] -= tem;
        }

        for (int i = 0; i < 26; i++)
        {
            for (int j = 0; j < collect[i]; j++)
                result += ('0' + i);
        }

        printf("Case #%d: %s\n", test, result.c_str());
    }
}