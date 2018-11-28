#include<iostream>
#include<fstream>
using namespace std;

string flip (string pancake)
{
    for (int i = 0; i < pancake.length(); i++)
    {
        if (pancake[i] == '+') pancake[i] = '-';
        else pancake[i] = '+';
    }
    return pancake;
}

int main()
{
    ifstream fin ("B-large.in");
    ofstream fout ("B-largeoutput.out");
    string pancakes, partpancakes, otherpartpancakes;
    int numhappy = 0, numflips, t;
    fin >> t;
    int output[t];
    for (int i = 0; i < t; i++)
    {
        numflips = 0;
        fin >> pancakes;
        for (int k = pancakes.length() - 1; k > -1; k--)
        {
            if (pancakes[k] == '-')
            {
                partpancakes = pancakes.substr(0, k + 1);
                otherpartpancakes = pancakes.substr(k + 1, pancakes.length() - k - 1);
                partpancakes = flip(partpancakes);
                numflips++;
                pancakes = partpancakes + otherpartpancakes;
            }
        }
        output[i] = numflips;
    }
    for (int i = 0; i < t; i++)
        fout << "Case #" << i + 1 << ": " << output[i] << endl;
}
