#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <fstream>

using namespace std;

bool count(int N, string& digitsSeen)
{
    stringstream ss;

    ss << N;

    auto digits = ss.str();

    for (auto i : digits)
    {
        if (digitsSeen.find(i) == string::npos)
        {
            digitsSeen += i;
        }
    }

    string digitsToSee = "0123456789";

    bool seenEmAll = true;

    for (auto i : digitsToSee)
    {
        if (digitsSeen.find(i) == string::npos)
        {
            seenEmAll = false;
        }
    }

    return seenEmAll;
}

int main()
{
    string inputFilePath;

    cout << "enter input file path: ";
    cin >> inputFilePath;

    ifstream inputFile(inputFilePath);

    if (!inputFile)
    {
        cout << "unable to open\n";
        return 0;
    }

    int T;
    inputFile >> T;

    vector<int> results(T);

    for (int i = 0; i < T; i++)
    {
        int N;
        inputFile >> N;

        if (N == 0)
        {
            results[i] = -1;
            continue;
        }

        int i2 = 1;
        string digitsSeen = "";

        while (!count(N*i2, digitsSeen))
        {
            i2++;
        }

        results[i] = i2 * N;
    }

    inputFile.close();
    ofstream outputFile("output.out");

    for (int i = 0; i < T; i++)
    {
        outputFile << "Case #" << i + 1 << ": ";

        if (results[i] != -1)
        {
            outputFile << results[i]  << "\n";
        }
        else
        {
            outputFile << "INSOMNIA"  << "\n";
        }
    }
    outputFile.close();

    return 0;
}
