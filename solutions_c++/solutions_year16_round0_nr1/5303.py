#include <iostream>
#include <fstream>
#include <vector>


using namespace std;

void setDigits (vector<bool>& numbers, long long N)
{
    while (N > 0)
    {
        numbers[N%10] = true;
        N = N /10;
    }
}

bool canISleep (vector<bool>& numbers)
{
    for (int i=0; i<numbers.size(); i++)
    {
        if (numbers[i] == false)
            return false;
    }
    return true;
}

int main(int argc, char *argv[])
{
    ifstream infile(argv[1]);
    ofstream outfile("output.txt", fstream::trunc);
    int T;
    infile >> T;
    for (int i=0; i<T; i++)
    {
        long long N,K;
        bool slept=false;
        infile >> N;
        K=N;
        if (K == 0)
            outfile << "Case #" << i+1 << ": INSOMNIA" << endl;
        else
        {
            vector<bool> numbers(10, 0);
            while (!slept)
            {
                setDigits(numbers, K);
                slept = canISleep(numbers);
                K = K+N;
            }
            outfile << "Case #" << i+1 << ": " << K-N << endl;
        }
    }
    return 0;
}
