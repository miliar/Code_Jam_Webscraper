#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

vector<int> getDigits(int n)
{
    vector<int> v;

    while(n != 0)
    {
        v.push_back(n % 10);
        n /= 10;
    }

    return v;
}

int getLastNumber(int N)
{
    bool digit[10] = {false};

    for(int j = 0 ; j < 10 ; j++)
        digit[j] = false;

    int i = 1, curr = N;

    while(true)
    {
        vector<int> d = getDigits(curr);

        for(vector<int>::iterator it = d.begin() ; it != d.end() ; it++)
            digit[*it] = true;

        curr += N;
        i++;

        bool allFound = true;

        for(int j = 0 ; j < 10 ; j++)
            if(!digit[j])
            {
                allFound = false;
            }

        if(allFound)
            return curr-N;
    }
}

int main(int argc, char** argv)
{
    ifstream file(argv[1]);
    ofstream output(argv[2]);

    if(!file)
        return -1;

    int T = 0;

    file >> T;

    for(int i = 0 ; i < T ; i++)
    {
        int N;
        file >> N;
        
        if(N == 0)
            output << "Case #" << i+1 << ": INSOMNIA" << endl;
        else
            output << "Case #" << i+1 << ": " << getLastNumber(N) << endl;
    }

    file.close();
    output.close();

    return 0;
}
