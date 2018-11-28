#include <iostream>

using namespace std;

int main()
{
    int numPeople;
    int count;
    string shyness;
    int T;

    cin >> T;

    for (int i = 0; i < T; i++)
    {
        numPeople = 0;
        count = 0;

        int n;
        cin >> n;
        cin >> shyness;

        for (int j = 0; j <= n; j++)
        {
            int tempNum;

            switch (shyness[j])
            {
            case '0':
                tempNum = 0;
                break;

            case '1':
                tempNum = 1;
                break;

            case '2':
                tempNum = 2;
                break;

            case '3':
                tempNum = 3;
                break;

            case '4':
                tempNum = 4;
                break;

            case '5':
                tempNum = 5;
                break;

            case '6':
                tempNum = 6;
                break;

            case '7':
                tempNum = 7;
                break;

            case '8':
                tempNum = 8;
                break;

            case '9':
                tempNum = 9;
                break;

            }

            if (tempNum != 0 && numPeople < j) {
                count += (j - numPeople);
                numPeople += (j - numPeople);
            }

            numPeople += tempNum;
        }

        cout << "Case #" << i+1 << ": " << count << endl;
    }
}
