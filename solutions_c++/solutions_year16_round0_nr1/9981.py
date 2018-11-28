#include <iostream>
#include <vector>

using namespace std;

bool areAllDigitsSeen(vector<bool> &seenDigits)
{
    bool allSeen = true;

    for(int i = 0 ; i < 10 && allSeen ; i++)
    {
        allSeen = seenDigits[i];
    }

    return allSeen;
}

void updateSeenDigits(vector<bool> &seenDigits, int N)
{
    while( N != 0)
    {
        seenDigits[N % 10] = true;
        N /= 10;
    }
}


int main(int argc, char *argv[])
{
    int T, N, currentN;
    vector<bool> seenDigits;
    cin >> T;

    for(int i = 0 ; i < T ; i++)
    {
        cin >> N;
        currentN = N;

        if(N == 0)
        {
            cout << "Case #" << i+1 << ": " << "INSOMNIA" << endl;
        }
        else
        {
            seenDigits.assign(10, false);
            updateSeenDigits(seenDigits, N);

            while(!areAllDigitsSeen(seenDigits))
            {
                currentN += N;
                updateSeenDigits(seenDigits, currentN);
            }

            cout << "Case #" << i+1 << ": " << currentN << endl;
        }
    }

    return 0;
}
