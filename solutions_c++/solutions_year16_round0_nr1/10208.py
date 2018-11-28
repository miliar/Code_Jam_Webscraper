#include <iostream>

using namespace std;

int CountSheep(int N)
{
    if(N == 0)
    {
        return -1;
    }

    int ret = 0;
    int nCount = 0;
    bool arrbTable[10] = {false,};

    for (int nSeq = 1; nCount < 10; nSeq++)
    {
        ret = N * nSeq;

        char strN[10] = {0,};
        snprintf(strN, sizeof(strN), "%d", ret);

        int nStrN = strlen(strN);

        for (int i = 0; i < nStrN; i++)
        {
            int nVal = strN[i] - '0';

            if (arrbTable[nVal] == true)
            {
                continue;
            }

            arrbTable[nVal] = true;
            nCount++;
        }
    }

    return ret;
}

int main() {

    int nTestCase;
    cin >> nTestCase;

    for(int i=0; i<nTestCase; i++)
    {
        int N;
        cin >> N;

        int result = CountSheep(N);

        cout << "Case #" << (i+1) << ": ";

        if(result < 0)
        {
            cout << "INSOMNIA";
        }
        else
        {
            cout << result;
        }

        cout << endl;
    }
}