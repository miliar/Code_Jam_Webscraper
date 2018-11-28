#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <cstring>
#include <math.h>
using namespace std;

int main()
{
    FILE *fin = freopen("B-small.in", "r", stdin);
    assert( fin!=NULL );
    FILE *fout = freopen("B-small.out", "w", stdout);
    int tries, result, len, j, count;
    string N;
    cin >> tries;
    for (int i = 1; i <= tries; i++)
    {
        cin >> N;
        result = 0;
        len = N.length();
        j = len-1;
        char str[len+1];
        strcpy (str,N.c_str());
        while(j>=0)
        {
            if (str[j] == '-')
            {
                if (str[0] == '+')
                {
                    count = 0;
                    result++;
                    while (str[count] == '+')
                    {
                        str[count] = '-';
                        count++;
                    }
                }
                result++;
                for (int k = 0; k < ceil((j+1)/2.0);k++)
                {
                    if ((str[k] == '+') && (str[j-k] == '+'))
                    {
                        str[k] = '-';
                        str[j-k] = '-';
                    }
                    else if ((str[k] == '-') && (str[j-k] == '-'))
                    {
                        str[k] = '+';
                        str[j-k] = '+';
                    }
                }
            }
            else
                j--;
        }
        cout << "Case #" << i << ": " << result << endl;
    }
    return 0;
}
