#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int y(vector<int>& m)
{
    int result = 0;
    for (int i = 0; i < m.size() - 1; ++i)
    {
        int diff = m[i] - m[i+1];
        if (diff > 0)
        {
            result += diff;
        }
    }
    return result;
}
  
int z(vector<int>& m)
{
    int speed = 0;
    for (int i = 0; i < m.size() - 1; ++i)
    {
        speed = max(speed, (m[i] - m[i+1]));
    }
    int result = 0;
    for (int i = 0; i < m.size() - 1; ++i)
    {
        result += min(speed, m[i]);
    }
    return result;
}

int main()
{
    ifstream inputFile("input.txt");
    ofstream outputFile("output.txt");

    int T;
    inputFile >> T;
    for (int c = 0; c < T; ++c)
    {
        int N;
        inputFile >> N;
        vector<int> m(N);
        for (int i = 0; i < N; ++i)
        {
            inputFile >> m[i];
        }
        
        outputFile << "Case #" << (c + 1) << ": " << y(m) << " " << z(m) << "\n";
    }
    
    return 0;
}
