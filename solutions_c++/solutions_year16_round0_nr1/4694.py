#include <iostream>
#include <string.h>

using namespace std;

int main( )
{

    ios::sync_with_stdio(false);

    // ifstream fin ("file.in");
    // ofstream fout ("file.out");
    // fin >> interval;
    // fout << endl;

    int full[10] = {1,1,1,1,1,1,1,1,1,1};
    int hash[10];
    int N, curr;
    long orig;
    long counter;

    bool correct;
    cin >> N;

    for(long i = 1; i <= N; i++)
    {
        counter = 0;
        memset(hash, 0, sizeof(hash));
        cin >> curr;

        if(curr == 0)
        {
            cout << "Case #" << i << ": INSOMNIA" << endl;
            continue;
        }

        orig = curr;
        while(++counter)
        {

            curr = orig;
            curr *= counter;

            while(curr > 0)
            {
                hash[curr%10] = 1;
                curr /= 10;
            }

            correct = true;
            for(long j = 0; j < 10; j++)
                if(hash[j] == 0)
                {
                    correct = false;
                    break;
                }

            if(correct)
            {
                cout << "Case #" << i << ": " << orig * counter << endl;
                counter = 0;
                break;
            }

        }

    }

    return 0;

}
