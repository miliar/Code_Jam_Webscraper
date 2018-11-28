#include <iostream>

using namespace std;

int T;
int TestCase;
int S;
int ANSWER;
int sum;


int main()
{
    if (freopen("A-large.in", "r", stdin) == NULL) return 0;
    if (freopen("result.out", "w", stdout) == NULL) return 0;
    cin >> T;
    while (T > TestCase)
    {
        ANSWER = 0;
        sum = 0;

        cin >> S;

        getchar();

        int in;
        for (int i = 0; i <= S; i++)
        {
            in = getchar() - '0';
            //in = getchar();
            sum += in;
            if (sum < i+1)
            {
                ANSWER = ANSWER + i + 1 - sum;
                sum = i + 1;
            }
        }

        cout << "Case #" << TestCase + 1 << ": ";
        cout << ANSWER << endl;
        TestCase++;
    }

    return 0;
}