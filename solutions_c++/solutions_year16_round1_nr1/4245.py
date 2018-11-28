#include <iostream>
#include <fstream>
#include <inttypes.h>
#include <cmath>
#include <string>
#include <cstdlib>

using namespace std;

void find_small(char array[], char small[])
{
    for (int i = 0; array[i] != '\0'; i++)
    {
        for (int j = 0; j < 26; j++)
        {
            if (array[i] == small[j])
                break;
            if (small[j] == 0)
            {
                small[j] = array[i];
                break;
            }
        }
    }
    return;
}

void sort_this (char small[])
{
    char max = '\0';
    int index;
    char temp;
    for (int i = 0; small [i] != '\0'; i++)
    {
        index = i;
        for (int j = i; small[j] != '\0'; j++)
        {
            if (small[j] > max)
            {
                max = small[j];
                index = j;
            }
        }
        temp = small [index];
        small [index] = small [i];
        small [i] = temp;
        max = 0;
    }
}

int main()
{
    int64_t T, i, j, k, l, left, right;
    char array[1001], small[27], copy[1001], final [2001];
    int matrix_index[1001];
    int matrix[27][1001];
    ifstream fin;
    ofstream fout;
    fin.open ("input.txt");
    fout.open ("output.txt");
    fin >> T;
    for (i = 0; i < T; i++)
    {
        fout << "Case #" << i + 1 << ": ";
        fin >> array;
        for (j = 0; j < 27; j++)
            for (k = 0; k < 1001; k++)
                matrix[j][k] = -1;
        for (j = 0; array[j] != '\0'; j++)
            copy[j] = array[j];
        for (j = 0; j < 2001; j++)
            final[j] = 'a';
        for (j = 0; j < 26; j++)
            small[j] = '\0';
        for (j = 0; j < 1001; j++)
            matrix_index [j] = -1;
        find_small (array, small);
        sort_this (small);
        for (k = 0; small[k] != '\0'; k++)
        {
            l = 0;
            for (j = 0; copy[j] != '\0'; j++)
            {
                if (copy[j] == small[k])
                {
                    matrix[k][l] = j;
                    l++;
                }
            }
            copy[matrix[k][0]] = '\0';
        }
        l = 0;
        for (j = 26; j >= 0; j--)
        {
            for (k = 0; k < 1001 && matrix[j][k] != -1; k++)
            {
                matrix_index[l] = matrix [j][k];
                l++;
            }
        }
        left = 1000;
        right = 1001;
        l = 0;
        for (j = 0; array[j] != '\0'; j++)
        {
            if (j == matrix_index[l])
            {
                final[left] = array[j];
                left--;
                l++;
            }
            else
            {
                final[right] = array[j];
                right++;
            }
        }
        for (j = left; j < right; j++)
        {
            if (final[j] != 'a')
            {
                fout << final[j];
            }
        }
        fout << endl;
    }
    fin.close ();
    fout.close ();
    return 0;
}
